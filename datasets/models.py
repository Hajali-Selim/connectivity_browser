from django.db import models

# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=255)
    field = models.CharField('Discipline', max_length=255)
    space = models.CharField('Spatial scale', max_length=255, null=True)
    time = models.CharField('Temporal scale', max_length=255, null=True)
    sc1, sc2, sc3 = models.PositiveIntegerField('Relational SC', null=True), models.PositiveIntegerField('Layout SC', null=True), models.PositiveIntegerField('Pragmatic SC', null=True)
    fc1, fc2, fc3, fc4 = models.PositiveIntegerField('Quantitative FC', null=True), models.PositiveIntegerField('Relational FC', null=True), models.PositiveIntegerField('Mechanistic FC', null=True), models.PositiveIntegerField('Propagation FC', null=True)
    icon = models.ImageField('Icon', blank=True, upload_to='datasets/static/images/icons')
    slug = models.SlugField(default="", null=False)
    def __str__(self):
        return f'{self.name}'

class Structural(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    sc1_matrix, sc2_matrix, sc3_matrix = models.ImageField('Relational SC matrices', blank=True, upload_to='datasets/static/images/matrices/sc1'), models.ImageField('Layout SC matrices', blank=True, upload_to='datasets/static/images/matrices/sc2'), models.ImageField('Pragmatic SC matrices', blank=True, upload_to='datasets/static/images/matrices/sc3')
    #slug = models.SlugField(default="", null=False)
    def __str__(self):
        return f'{self.name}'

class Functional(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    fc1_matrix, fc2_matrix, fc3_matrix, fc4_matrix = models.ImageField('Quantitative FC matrices', blank=True, upload_to='datasets/static/images/matrices/fc1'), models.ImageField('Relational FC matrices', blank=True, upload_to='datasets/static/images/matrices/fc2'), models.ImageField('Mechanistic FC matrices', blank=True, upload_to='datasets/static/images/matrices/fc3'), models.ImageField('Propagation FC matrices', blank=True, upload_to='datasets/static/images/matrices/fc4')
    #slug = models.SlugField(default="", null=False)
    def __str__(self):
        return f'{self.name}'

