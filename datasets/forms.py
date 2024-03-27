from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _
from .models import Dataset, Structural, Functional

class DatasetAdminForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ("name", "slug", "icon", "field", "space", "time", "sc1", "sc2", "sc3", "fc1", "fc2", "fc3", "fc4")
    figures = forms.FileField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), label=_("Add figures"), required=False, )
    def clean_figures(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("figures"):
            validate_image_file_extension(upload)
    def save_figures(self, figure):
        """Process each uploaded figure."""
        for upload in self.files.getlist("figures"):
            figure = Structural(dataset=dataset, figure=upload)
            figure.save()
