from django.db import models

# Create your models here.
class Dataset(models.Model):
    name, field = models.CharField(max_length=255), models.CharField('Discipline', max_length=255)
    space, time = models.CharField('Spatial scale', max_length=255, null=True), models.CharField('Temporal scale', max_length=255, null=True)
    icon = models.ImageField('Icon', blank=True)
    sc1, sc2, sc3 = models.ImageField('Relational SC', blank=True, upload_to='datasets/static/images/'), models.ImageField('Layout SC', blank=True, upload_to='datasets/static/images/'), models.ImageField('Pragmatic SC', blank=True, upload_to='datasets/static/images/')
    fc1, fc2, fc3, fc4 = models.ImageField('Quantitative FC', blank=True, upload_to='datasets/static/images/'), models.ImageField('Qualitative FC', blank=True, upload_to='datasets/static/images/'), models.ImageField('Mechanistic FC', blank=True, upload_to='datasets/static/images/'), models.ImageField('Propagation FC', blank=True, upload_to='datasets/static/images/')
    slug = models.SlugField(default="", null=False)
    def __str__(self):
        return f'{self.name}'

