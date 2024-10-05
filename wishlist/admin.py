from django.contrib import admin
from .models import UserWishlist


class WishListAdmin(admin.ModelAdmin):
    pass
    # fields = ['user','registrations']
    # list_display = ['id','user']


admin.site.register(UserWishlist,WishListAdmin)