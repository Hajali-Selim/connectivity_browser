from django.contrib import admin
from .models import Dataset
# Register your models here.

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    prepopulated_fields = {"slug": "name")}

