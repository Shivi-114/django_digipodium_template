from django import forms
from django.db.models import fields
from .models import Profile, ServiceRequest

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Full_Name', 'gender', 'mobile', 'pic', 'address')


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ('durations', 'gender', 'age', 'request_for')
        
        