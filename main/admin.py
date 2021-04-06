from django.contrib import admin
from .models import *
# Register your models here.


class ImageInLineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 5

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [ImageInLineAdmin,]
    
admin.site.register(Genre)





