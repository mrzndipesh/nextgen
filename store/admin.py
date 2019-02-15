from django.contrib import admin
from .models import Product,ProductImage,Shop,Category, SubCategory, SliderImage 
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SliderImage)
#admin.site.register(DailyEntry)