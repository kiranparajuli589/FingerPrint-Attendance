from django import forms


class ScanForm(forms.Form):
    fingercode = forms.CharField(max_length=10)


class SearchForm(forms.Form):
    year = forms.IntegerField(label='Year',
                              max_value=2100,
                              min_value=2000)
    month = forms.IntegerField(label='Month',
                               max_value=12,
                               min_value=1)
    day = forms.IntegerField(label='Day',
                             max_value=32, min_value=1,
                             required=False)
