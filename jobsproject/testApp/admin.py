from django.contrib import admin
from testApp.models import Hydjobs,Punejobs,Begjobs,Channaijobs

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phone']


class BegjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phone']


class PunejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phone']


class ChannaijobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phone']

admin.site.register(Hydjobs,HydjobsAdmin)
admin.site.register(Begjobs,BegjobsAdmin)
admin.site.register(Punejobs,PunejobsAdmin)
admin.site.register(Channaijobs,ChannaijobsAdmin)