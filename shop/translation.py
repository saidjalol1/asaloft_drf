from modeltranslation.translator import translator, TranslationOptions
from .models import Product, Category

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'material', 'paint_type', "frame")

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Product, ProductTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
