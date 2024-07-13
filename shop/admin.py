from django.contrib import admin
from .models import Product, ProductImages, Category, Discounts, ColorImages, Order

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1  # Number of extra empty forms to display

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
    list_display = ('name', 'dimensions', 'frame', 'material', 'paint_type', 'price', 'category', 'discount')


admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Discounts)
admin.site.register(ColorImages)