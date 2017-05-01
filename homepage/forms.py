from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import farmer, retailer, sell, fcomplain, rcomplain, r_ad_details


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class FarmerForm(forms.ModelForm):

    class Meta:
        model = farmer
        fields = ('fname','crop_details','phone','address','aadhar_no')

class SellForm(forms.ModelForm):

    class Meta:
        model = sell
        fields = ['farmer_details','crop_details','retailer_details','qty_sold_at','crop_pic']



class FComplainForm(forms.ModelForm):

    class Meta:
        model = fcomplain
        fields = ['f','complain']






class RetailerForm(forms.ModelForm):

    class Meta:
        model = retailer
        fields = ('rname','phone','address')


class RComplainForm(forms.ModelForm):

    class Meta:
        model = rcomplain
        fields = ['r','complain']


class postadForm(forms.ModelForm):

    class Meta:
        model =r_ad_details
        fields = ['retailer_details','crop_details','qty_details','status_update']

