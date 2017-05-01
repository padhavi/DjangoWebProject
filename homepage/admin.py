from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
#from homepage.models import profile
from .models import farmer, retailer, crop, rcomplain, sell, qty, fcomplain, f_ad_details, r_ad_details

# class UserProfileInline(admin.TabularInline):
    # model = profile
    #can_delete = True
    #verbose_name_plural = 'profile'


# Define a new User admin

# class UserAdmin(UserAdmin):
#     inlines = [
#         UserProfileInline,
#         ]


# Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

admin.site.register(farmer)
admin.site.register(retailer)
admin.site.register(crop)
admin.site.register(sell)
admin.site.register(qty)
admin.site.register(rcomplain)
admin.site.register(fcomplain)
admin.site.register(f_ad_details)
admin.site.register(r_ad_details)

