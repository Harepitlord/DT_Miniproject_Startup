from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth import get_user_model
from .models import *


class CustomUserCreationForm(UserCreationForm):
    gender = forms.ChoiceField(choices=('Male', 'Female', 'Other'),
                               widget=forms.Select())

    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'mobile', 'userName')


class CustomUserChangeForm(UserChangeForm):
    gender = forms.ChoiceField(choices=('Male', 'Female', 'Other'),
                               widget=forms.Select())

    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'mobile', 'userName')


class NewUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    gender = forms.ChoiceField(choices=('Male', 'Female', 'Other'))
    gender.widget = forms.Select(attrs={'class': 'signRadio'})

    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'mobile', 'userName')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'signupForm',
                'placeholder': _('Name')}),
            'email': forms.EmailInput(attrs={
                'class': 'signupForm',
                'placeholder': _('Email')}),
            'mobile': forms.TextInput(attrs={
                'class': 'signupForm',
                'placeholder': _('Mobile')}),
            'userName': forms.TextInput(attrs={
                'class': 'signupForm',
                'placeholder': _('UserName')})
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()


class NewPost(forms.ModelForm):
    class Meta:
        model = FeedPost
        fields = ('heading', 'description', 'websiteURL', 'media')
        labels = (_('Heading:'), _('Description'), _('Website URL'), _('Media'))
        widgets = {
            'heading': forms.TextInput(attrs={
                'placeholder': _('Heading')}),
            'description': forms.Textarea(attrs={
                'placeholder': _('Description')}),
            'websiteURL': forms.URLInput(attrs={
                'placeholder': _('Website URL')}),
            'media': forms.FileInput(attrs={
                'placeholder': _('Media')}),
        }


class CompanyProfile(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('companyName', 'speciality', 'productName', 'websiteURL')
        labels = (_('Company Name:'), _('Speciality:'), _('Product Name:'), _('website URL: '))
        widgets = {
            'companyName': forms.TextInput(attrs={
                'placeholder': _('Company Name: ')}),
            'speciality': forms.TextInput(attrs={
                'placeholder': _('Speciality: ')}),
            'productName': forms.TextInput(attrs={
                'placeholder': _('Product Name: ')}),
            'websiteURL': forms.URLInput(attrs={
                'placholder': _('Websie URL')}),
        }
