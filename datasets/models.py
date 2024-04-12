from django.db import models

# Create your models here.
class Dataset(models.Model):
    image_folder = 'datasets/static/images/'
    image_folder = 'static/'
    name, field = models.CharField(max_length=255), models.CharField('Discipline', max_length=255)
    space, time = models.CharField('Spatial scale', max_length=255, null=True), models.CharField('Temporal scale', max_length=255, null=True)
    icon = models.ImageField('Icon', blank=True, upload_to=image_folder)
    sc1, sc2, sc3 = models.ImageField('Relational SC', null=True, blank=True,  upload_to=image_folder+'matrices/'), models.ImageField('Layout SC', null=True, blank=True,  upload_to=image_folder+'matrices/'), models.ImageField('Pragmatic SC', null=True, blank=True,  upload_to=image_folder+'matrices/')
    fc1, fc2, fc3, fc4 = models.ImageField('Quantitative FC', null=True, blank=True, upload_to=image_folder+'matrices/'), models.ImageField('Qualitative FC', null=True, blank=True,  upload_to=image_folder+'matrices/'), models.ImageField('Mechanistic FC', null=True, blank=True,  upload_to=image_folder+'matrices/'), models.ImageField('Propagation FC', null=True, blank=True, upload_to=image_folder+'matrices/')
    slug = models.SlugField(default="", null=False)
    def __str__(self):
        return f'{self.name}'

