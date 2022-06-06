from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PhotoAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_show', 'category', 'product_code', 'qty_product', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'product_code', 'product_code')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PhotoAdmin]

    def image_show(self, obj):
        if obj.img:
            return mark_safe(f"<img src='{obj.img.url}' width='60' /> ")
        return None

    image_show.__name__ = 'Фотокартка'


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    search_fields = ('id', 'user')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
