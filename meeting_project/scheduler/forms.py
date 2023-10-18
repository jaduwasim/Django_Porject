from django import forms

class BookingForm(forms.Form):
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    person_capacity = forms.IntegerField(min_value=2, max_value=20)

class AvailabilityForm(forms.Form):
    start_time = forms.TimeField()
    end_time = forms.TimeField()
