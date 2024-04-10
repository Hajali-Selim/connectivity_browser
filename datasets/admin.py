from django.contrib import admin
from .models import Dataset
# Register your models here.

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    prepopulated_fields = {"slug": ("name", "icon", "field", "space", "time", "sc1", "sc2", "sc3", "fc1", "fc2", "fc3", "fc4", )}

