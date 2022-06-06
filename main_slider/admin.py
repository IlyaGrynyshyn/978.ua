from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'post')
    search_fields = ('title', 'post')

    def image_show(self, obj):
        if obj.img:
            return mark_safe(f"<img src='{obj.img.url}' width='60' /> ")
        return None

    image_show.__name__ = 'Фотокартка'


admin.site.register(Slider, SliderAdmin)
