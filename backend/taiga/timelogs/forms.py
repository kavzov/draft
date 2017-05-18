from django import forms
from .models import Timelog


class TimelogForm(forms.ModelForm):
    class Meta:
        model = Timelog
        fields = ['issue', 'user']

