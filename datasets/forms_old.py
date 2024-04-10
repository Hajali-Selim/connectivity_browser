from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _
from .models import Dataset, SC1, SC2, SC3, FC1, FC2, FC3, FC4

class DatasetAdminForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ("name", "slug", "icon", "field", "space", "time", "nb_sc1", "nb_sc2", "nb_sc3", "nb_fc1", "nb_fc2", "nb_fc3", "nb_fc4")
    SC1_fig, SC2_fig, SC3_fig = forms.FileField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), label=_("Add relational SC figure"), required=False, ), forms.FileField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), label=_("Add layout SC figure"), required=False, ), forms.FileField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), label=_("Add pragmatic SC figure"), required=False, )
    FC1_fig, FC2_fig, FC3_fig, FC4_fig = forms.FileField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), label=_("Add  quantitative FC figure"), required=False, ), forms.FileField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), label=_("Add  qualitative FC figure"), required=False, ), forms.FileField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), label=_("Add mechanistic FC figure"), required=False, ), forms.FileField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), label=_("Add propagation FC figure"), required=False, )
    SC1_txt, SC2_txt, SC3_txt = forms.CharField(widget=forms.TextInput(attrs={'size':'40'}), max_length=20, required=False, label=_("Add relational SC title")), forms.CharField(widget=forms.TextInput(attrs={'size':'40'}), max_length=20, required=False, label=_("Add layout SC title")), forms.CharField(widget=forms.TextInput(attrs={'size':'40'}), max_length=20, required=False, label=_("Add pragmatic SC title"))
    FC1_txt, FC2_txt, FC3_txt, FC4_txt = forms.CharField(widget=forms.TextInput(attrs={'size':'40'}), max_length=20, required=False, label=_("Add quantitative FC title")), forms.CharField(widget=forms.TextInput(attrs={'size':'40'}), max_length=20, required=False, label=_("Add qualitative FC title")), forms.CharField(widget=forms.TextInput(attrs={'size':'40'}), max_length=20, required=False, label=_("Add mechanistic FC title")), forms.CharField(widget=forms.TextInput(attrs={'size':'40'}), max_length=20, required=False, label=_("Add propagation FC title"))
    #def clean_figures(self, figure):
    #    """Make sure only images can be uploaded."""
    #    for upload_fig in self.files.getlist("SC1_fig"):
    #        validate_image_file_extension(upload_fig)
    def save_figures(self, figure):
        """Process each uploaded figure."""
        for upload_fig in self.files.getlist("SC1_fig"):
            figure = SC1(dataset=dataset, figure=upload_fig)
            figure.save()
        #for upload_txt in self.files.getlist("SC1_txt"):
        #    title = SC1(dataset=dataset, figure=upload_txt)
        #    title.save()
            
