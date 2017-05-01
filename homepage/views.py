


# Create your views here.
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.db.models import Q
from homepage.forms import UserForm, RetailerForm, FarmerForm, FComplainForm, SellForm, RComplainForm, postadForm
from django.contrib.auth import login as auth_login

from .models import farmer, retailer, fcomplain,r_ad_details,f_ad_details

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    return render(request, "homepage/index.html",context_instance=RequestContext(request))
def About_us(request):
    return render(request, "homepage/About_us.html",context_instance=RequestContext(request))
def material(request):
    return render(request, "homepage/material.html",context_instance=RequestContext(request))
def loginpage(request):
    return render(request, "homepage/loginpage.html",context_instance=RequestContext(request))

def farmerr(request):
    return render(request, "homepage/farmer.html",context_instance=RequestContext(request))
def RegisterUser(request):
    return render(request, "homepage/RegisterUser.html",context_instance=RequestContext(request))

def create_farmer_extra(request):
    return render(request, "homepage/create_farmer_extra.html",context_instance=RequestContext(request))

def Checkcomplain(request):
    return render(request, "homepage/Checkcomplain.html",context_instance=RequestContext(request))

def CheckcomplainRetailer(request):
    return render(request, "homepage/CheckcomplainRetailer.html",context_instance=RequestContext(request))



def logoutt(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'homepage/login.html', context)

def retailerlogoutt(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'homepage/retailer_login.html', context)


def farmerlogoutt(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'homepage/farmer_login.html', context)




def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                farmers = farmer.objects.filter(user=request.user)
                return render(request, 'homepage/farmer.html', {'farmers': farmers})
            else:
                return render(request, 'homepage/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'homepage/login.html', {'error_message': 'Invalid login'})
    return render(request, 'homepage/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():

        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                farmers = farmer.objects.filter(user=request.user)
                return render(request, 'homepage/create_retailer.html', {'farmers': farmers})
    context = {
        "form": form,
    }
    return render(request, 'homepage/register.html', context)


def farmer_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                farmerss = farmer.objects.filter(user=request.user)
                return render(request, 'homepage/farmer_dash.html', {'farmerss': farmerss})
            else:
                return render(request, 'homepage/farmer_login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'homepage/farmer_login.html', {'error_message': 'Invalid login'})
    return render(request, 'homepage/farmer_login.html')

def farmer_register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():

        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user.set_password(password)
        user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                farmerss = farmer.objects.filter(user=request.user)
                return render(request, 'homepage/create_farmer_extra.html', {'farmerss': farmerss})
    context = {
        "form": form,
    }
    return render(request, 'homepage/farmer_register.html', context)





def retailer_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                retailers = retailer.objects.filter(user=request.user)
                return render(request, 'homepage/retailer_dash.html', {'retailers': retailers})
            else:
                return render(request, 'homepage/retailer_login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'homepage/retailer_login.html', {'error_message': 'Invalid login'})
    return render(request, 'homepage/retailer_login.html')

def retailer_register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():

        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user.set_password(password)
        user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                retailers = retailer.objects.filter(user=request.user)
                return render(request, 'homepage/create_farmer_extra.html', {'retailers': retailers})
    context = {
        "form": form,
    }
    return render(request, 'homepage/retailer_register.html', context)



def create_retailer(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/retailer_login.html')
    else:
        form = RetailerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            retailer_details = form.save(commit=False)
            retailer_details.user = request.user
            #details.rname = request.FILES['rname']
            #details.phone = request.FILES['phone']
            #details= request.POST.get('rname')
            #details.phone = request.POST.get('phone', False)
            retailer_details.save()
            return render(request, 'homepage/retailer_dash.html', {'retailer_details':retailer_details})
        context = {
            "form": form,
        }
        return render(request, 'homepage/create_retailer.html', context)

def create_farmer(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/farmer_login.html')
    else:
        form = FarmerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            farmer_details = form.save(commit=False)
            farmer_details.user = request.user
            #details.rname = request.FILES['rname']
            #details.phone = request.FILES['phone']
            #details= request.POST.get('rname')
            #details.phone = request.POST.get('phone', False)
            farmer_details.save()
            return render(request, 'homepage/farmer_dash.html', {'farmer_details':farmer_details})
        context = {
            "form": form,
        }
        return render(request, 'homepage/create_farmer.html', context)

def crop_ad_details(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/farmer_login.html')
    else:
     crop_ad = r_ad_details.objects.all();
     retailer_ads = {'user':request.user,'crop_ad': crop_ad}
     return render(request, 'homepage/crop_ad_details.html', retailer_ads)


def farmer_dash(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/farmer_login.html')
    else:
     posts = farmer.objects.all();

     args = {'user': request.user,'posts':posts}
     return render(request,'homepage/farmer_dash.html',args)

def viewcomplainfarmer(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/farmer_login.html')
    else:
     farcom = fcomplain.objects.filter(user=request.user);
     farmercomplain = {'farcom': farcom}
     print(farcom)
     return render(request, 'homepage/viewcomplainfarmer.html', farmercomplain)


def complain(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/farmer_login.html')
    else:
        form = FComplainForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            fcomplain_details = form.save(commit=False)
            fcomplain_details.user = request.user
            fcomplain_details.save();
            return render(request, 'homepage/farmer_dash.html', {'fcomplain_details': fcomplain_details})
        context = {
            "form": form,
        }
        return render(request, 'homepage/complain.html', context)

def sell_crop(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/farmer_login.html')
    else:
        form = SellForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            sell_details = form.save(commit=False)
            sell_details.user = request.user
            sell_details.save();
            return render(request, 'homepage/farmer_dash.html', {'sell_details': sell_details})
        context = {
            "form": form,
        }
        return render(request, 'homepage/sell_crop.html', context)



def retailer_dash(request):
    args = {'user': request.user}
    return render(request,'homepage/retailer_dash.html',args)

def farmer_ads(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/farmer_login.html')
    else:
     far_ad = f_ad_details.objects.all();
     farmer_ads = {'user':request.user,'far_ad': far_ad}
     return render(request, 'homepage/farmer_ads.html',farmer_ads)


def complain_retailer(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:
        form = RComplainForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            retailer_details = form.save(commit=False)
            retailer_details.user = request.user
            retailer_details.save();
            return render(request, 'homepage/retailer_dash.html', {'retailer_details': retailer_details})
        context = {
            "form": form,
        }
        return render(request, 'homepage/complain_retailer.html', context)

def viewcomplainretailer(request):
    retcom=rcomplain.objects.filter(user=request.user);
    retailercomplain={'retcom':retcom}
    print(retcom)
    return render(request, 'homepage/viewcomplainretailer.html', retailercomplain)




def post_advertisement(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:
        form = postadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            ad_details = form.save(commit=False)
            ad_details.user = request.user
            ad_details.save();
            return render(request, 'homepage/retailer_dash.html', {'ad_details': ad_details})
        context = {
            "form": form,
        }
        return render(request, 'homepage/post_advertisement.html', context)

