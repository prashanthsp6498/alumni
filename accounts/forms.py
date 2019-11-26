from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import AlumniProfile, JobOpenings, Account


class Registration(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='First Name')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = Account
        fields = ("email", "usn", 'first_name', 'last_name', "pass_out_batch", "dept", "password1", "password2",)


class UserDetails(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['profile_img', 'phone', 'designation', 'li_link', 'github_link', 'insta_link', 'facebook_link', 'pf_link']

    def __init__(self, *args, **kwargs):
        super(UserDetails, self).__init__(*args, **kwargs)
        self.fields['pf_link'].label = "Portfolio Link"
        self.fields['pf_link'].required = False
        self.fields['facebook_link'].required = False
        self.fields['insta_link'].required = False
        self.fields['github_link'].required = False
        self.fields['li_link'].label = "LinkedIn"
        self.fields['li_link'].required = False


class UserProfile(forms.ModelForm):
    class Meta:
        model = AlumniProfile
        fields = ['profile_img']


class JobUpdate(ModelForm):
    class Meta:
        model = JobOpenings
        fields = ['job_title', 'description', 'salary', 'company', 'hr_email']
