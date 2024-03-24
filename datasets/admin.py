from django.contrib import admin
from .models import Dataset
# Register your models here.

class DatasetAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Dataset, DatasetAdmin)


