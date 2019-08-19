from django.contrib import admin
from . import models
# Register your models here.


class SlideImageInline(admin.TabularInline):
    model = models.SlideImage
    extra = 1


@admin.register(models.Slide)
class SlideAdmin(admin.ModelAdmin):
    inlines = [SlideImageInline]
    pass
