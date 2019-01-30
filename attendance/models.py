from django.db import models
from datetime import date
from accounts.models import User
from bikram import samwat
import pytz

ktm = pytz.timezone('Asia/Kathmandu')


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ad = models.DateField(null=True, blank=True)
    date_bs = models.CharField(max_length=255, null=True, blank=True)
    start_time = models.TimeField()  # default=ktm.localize(datetime.now()))
    break_time = models.TimeField(blank=True, null=True)  # default=ktm.localize(datetime.now()))
    end_time = models.TimeField(blank=True, null=True)  # default=ktm.localize(datetime.now()))

    check_in = models.BooleanField(default=False)
    o_break = models.BooleanField(default=False, verbose_name='Break')
    check_out = models.BooleanField(default=False)

    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.full_name


# class LeaveApplication(models.Model):
#     ch = {
#         ('1', 'Annual'),
#         ('2', 'Sick/Usual'),
#         ('3', 'PH'),
#         ('4', 'Other')
#     }
#     user = models.ForeignKey(User, on_delete=models.SET_NULL)
#     date = models.DateField(default=date.today())
#     type = models.CharField(max_length=10, choices=ch)
