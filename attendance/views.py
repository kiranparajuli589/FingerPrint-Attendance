from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, date, timedelta
from django.contrib import messages
import pytz
from bikram import samwat
from bikram.constants import BS_YEAR_TO_MONTHS
from django.utils import timezone
from .forms import ScanForm, SearchForm
from .models import Attendance
from accounts.models import User

ktm = pytz.timezone('Asia/Kathmandu')
now = ktm.localize(datetime.now())


@login_required
def user_attend_search(request):
    title = 'Search Attendance'
    form = SearchForm(request.POST or None)
    user = request.user
    if form.is_valid():
        year = form.cleaned_data.get('year')
        month = form.cleaned_data.get('month')
        day = form.cleaned_data.get('day')
        if day:
            bs_date = samwat(year=year, month=month, day=day)
            str_bs = str(bs_date)
            try:
                attend = Attendance.objects.get(user=user, date_bs__exact=str_bs)
                return render(request, 'attendance/search_result_day.html', {'attend': attend,
                                                                             'user': user,
                                                                             'title': title})
            except ObjectDoesNotExist:
                messages.error(request, 'No entry matched!!!')
                return render(request, 'attendance/search_form.html', {'form': form,
                                                                       'title': title})
        if not day:
            bs_date = samwat(year=year, month=month, day=1)
            ad_date = bs_date.ad
            days_in_month = BS_YEAR_TO_MONTHS[year][month]
            ad_end = ad_date + timedelta(days=days_in_month)

            try:
                attend = Attendance.objects.filter(user=user, date_ad__range=(ad_date, ad_end))
                return render(request, 'attendance/search_result.html', {'attends': attend,
                                                                         'user': user,
                                                                         'title': title})
            except ObjectDoesNotExist:
                messages.error(request, '11No entry matched!!!')
                return render(request, 'attendance/search_form.html', {'form': form,
                                                                       'title': title})
    return render(request, 'attendance/search_form.html', {'form': form,
                                                           'title': title})


@login_required
def user_attend_log(request):
    title = 'Attendance Log'
    user = request.user
    attend = Attendance.objects.filter(user=user)
    return render(request, 'attendance/user_attend_log.html', {'attends': attend,
                                                               'user': user,
                                                               'title': title})


def checkout_view(request):
    title = 'Check Out'
    form = ScanForm(request.POST)
    if form.is_valid():
        fingercode = form.cleaned_data.get('fingercode')
        try:
            user = User.objects.get(fingercode=fingercode)
            attend = Attendance.objects.get(user=user, date_ad=now.date())
            attend.end_time = now
            attend.check_out = True
            attend.status = True
            attend.save()
            return render(request, 'attendance/check_out_done.html', {'user': user,
                                                                      'attend': attend,
                                                                      'title': title})
        except:
            messages.error(request, 'Fingercode not registered with any user')
            # raise ValidationError('Fingercode not registered with any user')
            return render(request, 'attendance/scan.html', {'form': form,
                                                            'title': title})
    return render(request, 'attendance/scan.html', {'form': form,
                                                    'title': title})


def break_view(request):
    title = 'Break View'
    form = ScanForm(request.POST)
    if form.is_valid():
        fingercode = form.cleaned_data.get('fingercode')
        try:
            user = User.objects.get(fingercode=fingercode)
            attend = Attendance.objects.get(user=user, date_ad=now.date())
            attend.break_time = now
            attend.o_break = True
            attend.save()

            return render(request, 'attendance/checkout_view.html', {'user': user, 'attend': attend, 'title': title})
        except:
            messages.error(request, 'Fingercode not registered with any user')
            # raise ValidationError('Fingercode not registered with any user')
            return render(request, 'attendance/scan.html', {'form': form, 'title': title})
    return render(request, 'attendance/scan.html', {'form': form, 'title': title})


def step_two(request):
    form = ScanForm(request.POST)
    if form.is_valid():
        fingercode = form.cleaned_data.get('fingercode')
        try:
            user = User.objects.get(fingercode=fingercode)
            attend = Attendance.objects.get(user=user, date_ad=date.today())
            return render(request, 'attendance/step2.html', {'user': user, 'attend': attend})
        except:
            messages.error(request, 'Fingercode not registered with any user')
            # raise ValidationError('Fingercode not registered with any user')
            return render(request, 'attendance/scan.html', {'form': form})


def fingerscan(request):
    title = 'Finger Scan'
    form = ScanForm(request.POST)
    if form.is_valid():
        fingercode = form.cleaned_data.get('fingercode')
        try:
            user = User.objects.get(fingercode=fingercode)
            print(user.full_name)
            try:
                attend = Attendance.objects.get(user=user, date_ad=date.today())
                print(attend.start_time)
                if attend.check_in and not attend.o_break and not attend.check_out:
                    return render(request, 'attendance/step2.html', {'user': user,
                                                                     'attend': attend})
                elif attend.check_in and attend.o_break and not attend.check_out:
                    return render(request, 'attendance/checkout_view.html', {'user': user,
                                                                             'attend': attend})
                elif attend.check_out:
                    return render(request, 'attendance/check_out_done.html', {'user': user,
                                                                              'attend': attend})
            except ObjectDoesNotExist:
                attend = Attendance.objects.create(user=user,
                                                   date_ad=date.today(),
                                                   date_bs=str(samwat.from_ad(date.today())),
                                                   start_time=now,
                                                   check_in=True)
                messages.success(request, 'Welcome %s' % user.full_name)
                return render(request, 'attendance/step2.html', {'user': user,
                                                                 'attend': attend})
        except ObjectDoesNotExist:
            messages.error(request, 'Fingercode not registered with any user')
            # raise ValidationError('Fingercode not registered with any user')
            return render(request, 'attendance/scan.html', {'form': form})
    return render(request, 'attendance/scan.html', {'form': form, 'title': title})
