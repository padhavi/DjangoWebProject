from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.farmerr, name='farmerr'),
    url(r'^RegisterUser$', views.RegisterUser, name='RegisterUser'),
    url(r'^About_us$', views.About_us, name='About_us'),


    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login,name='login'),
    url(r'^logoutt/$', views.logoutt, name='logoutt'),

    url(r'^retailer_register/$', views.retailer_register, name='retailer_register'),
    url(r'^retailer_login/$', views.retailer_login,name='retailer_login'),
    url(r'^retailerlogoutt/$', views.retailerlogoutt, name='retailerlogoutt'),

    url(r'^farmer_register/$', views.farmer_register, name='farmer_register'),
    url(r'^farmer_login/$', views.farmer_login,name='farmer_login'),
    url(r'^farmerlogoutt/$', views.farmerlogoutt, name='farmerlogoutt'),

    url(r'^loginpage$', views.loginpage, name='loginpage'),

    url(r'^create_farmer_extra$', views.create_farmer_extra, name='create_farmer_extra'),

    url(r'^create_farmer$', views.create_farmer, name='create_farmer'),
    url(r'^farmer_dash$', views.farmer_dash, name='farmer_dash'),
    url(r'^sell_crop$', views.sell_crop, name='sell_crop'),
    url(r'^complain$', views.complain, name='complain'),
    url(r'^crop_ad_details$', views.crop_ad_details, name='crop_ad_details'),
    url(r'^Checkcomplain$', views.Checkcomplain, name='Checkcomplain'),
    url(r'^viewcomplainfarmer$', views.viewcomplainfarmer, name='viewcomplainfarmer'),

    url(r'^create_retailer$', views.create_retailer, name='create_retailer'),
    url(r'^retailer_dash$', views.retailer_dash, name='retailer_dash'),
    url(r'^complain_retailer$', views.complain_retailer, name='complain_retailer'),
    url(r'^post_advertisement$', views.post_advertisement, name='post_advertisement'),
    url(r'^CheckcomplainRetailer$', views.CheckcomplainRetailer, name='CheckcomplainRetailer'),
    url(r'^viewcomplainretailer$', views.viewcomplainretailer, name='viewcomplainretailer'),
    url(r'^farmer_ads$', views.farmer_ads, name='farmer_ads'),

    url(r'^material$', views.material, name='material'),
    url(r'^index$', views.index, name='index'),

]

