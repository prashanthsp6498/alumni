from django.contrib import admin
from .models import ImageSlider, JobOpenings, Account, BestAlumnis

# Register your models here.

admin.site.register(ImageSlider)
admin.site.register(JobOpenings)
admin.site.register(Account)
admin.site.register(BestAlumnis)
