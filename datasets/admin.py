from django.contrib import admin
from .models import Dataset, SC1, SC2, SC3, FC1, FC2, FC3, FC4
from .forms import DatasetAdminForm
# Register your models here.

class SC1Inline(admin.TabularInline):#Tabular
    model, extra = SC1, 1

class SC2Inline(admin.TabularInline):#Tabular
    model, extra = SC2, 1

class SC3Inline(admin.TabularInline):#Tabular
    model, extra = SC3, 1

class FC1Inline(admin.TabularInline):#Tabular
    model, extra = FC1, 1

class FC2Inline(admin.TabularInline):#Tabular
    model, extra = FC2, 1

class FC3Inline(admin.TabularInline):#Tabular
    model, extra = FC3, 1

class FC4Inline(admin.TabularInline):#Tabular
    model, extra = FC4, 1

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    prepopulated_fields = {"slug": ("name", "icon", "field", "space", "time", "nb_sc1", "nb_sc2", "nb_sc3", "nb_fc1", "nb_fc2", "nb_fc3", "nb_fc4")}
    form = DatasetAdminForm
    inlines = [SC1Inline, SC2Inline, SC3Inline, FC1Inline, FC2Inline, FC3Inline, FC4Inline, ]
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_figures(form.instance)
        #form.save_titles(form.instance)

#admin.site.register(Dataset, DatasetAdmin)


