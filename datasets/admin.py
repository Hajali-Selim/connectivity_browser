from django.contrib import admin
from .models import Dataset, Structural, Functional
from .forms import DatasetAdminForm
# Register your models here.

class StructuralInline(admin.TabularInline):
    model, extra = Structural, 1

class FunctionalInline(admin.TabularInline):
    model, extra = Functional, 1

#@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    prepopulated_fields = {"slug": ("name", "icon", "field", "space", "time", "sc1", "sc2", "sc3", "fc1", "fc2", "fc3", "fc4")}
    form = DatasetAdminForm
    inlines = [StructuralInline, FunctionalInline, ]
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_figures(form.instance)

admin.site.register(Dataset, DatasetAdmin)


