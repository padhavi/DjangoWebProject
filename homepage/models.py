
from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import Permission, User


# Create your models here.
class crop(models.Model):

    cropid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=250)

    def __str__(self):
        return self.cname

class farmer(models.Model):
    user = models.ForeignKey(User, default=1)
    fname = models.CharField(max_length=250)
    crop_details = models.ForeignKey(crop)
    #cropname = models.CharField(max_length=250)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=500)
    aadhar_no = models.IntegerField(default=0)

    def __str__(self):
        return self.fname


class qty(models.Model):
    fid = models.CharField(max_length=250)
    crop_details =  models.ForeignKey(crop)
    q = models.IntegerField()
    price = models.IntegerField()


class retailer(models.Model):
    user = models.ForeignKey(User, default=1)
    rname = models.CharField(max_length=250)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=500)
    aadhar_no = models.IntegerField(default=0)
    def __str__(self):
        return self.rname

class r_ad_details(models.Model):
    retailer_details = models.ForeignKey(retailer)
    crop_details = models.ForeignKey(crop)
    qty_details = models.ForeignKey(qty)
    status_update = models.BooleanField(default=False)

class f_ad_details(models.Model):
    farmer_details = models.ForeignKey(farmer)
    crop_details = models.ForeignKey(crop)
    qty_details = models.ForeignKey(qty)
    status_update = models.BooleanField(default=False)

class sell(models.Model):
    farmer_details = models.ForeignKey(farmer)
    crop_details = models.ForeignKey(crop)
    retailer_details = models.ForeignKey(retailer)
    qty_sold_at = models.ForeignKey(qty)
    crop_pic = models.FileField()

class fcomplain(models.Model):
    user = models.ForeignKey(User, default=1)
    f = models.ForeignKey(farmer,on_delete=models.CASCADE,null=True,blank=True)
    complain = models.CharField(max_length=250)
    status_update = models.BooleanField(default=False)

class rcomplain(models.Model):
    r = models.ForeignKey(retailer)
    complain = models.CharField(max_length=250)
    status_update = models.BooleanField(default=False)
