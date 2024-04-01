from django.db import models

# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=255)
    field = models.CharField('Discipline', max_length=255)
    space = models.CharField('Spatial scale', max_length=255, null=True)
    time = models.CharField('Temporal scale', max_length=255, null=True)
    nb_sc1, nb_sc2, nb_sc3 = models.PositiveIntegerField('Relational SC', null=True), models.PositiveIntegerField('Layout SC', null=True), models.PositiveIntegerField('Pragmatic SC', null=True)
    nb_fc1, nb_fc2, nb_fc3, nb_fc4 = models.PositiveIntegerField('Quantitative FC', null=True), models.PositiveIntegerField('Relational FC', null=True), models.PositiveIntegerField('Mechanistic FC', null=True), models.PositiveIntegerField('Propagation FC', null=True)
    icon = models.ImageField('Icon', blank=True, upload_to='datasets/static/images/icons')
    slug = models.SlugField(default="", null=False)
    def __str__(self):
        return f'{self.name}'

class SC1(models.Model):
    dataset, matrix, name = models.ForeignKey(Dataset, on_delete=models.CASCADE), models.ImageField('Relational SC figure', blank=True, upload_to='datasets/static/images/matrices/sc1'), models.CharField('Relational SC title', max_length=40, blank=True)

class SC2(models.Model):
    dataset, matrix, name = models.ForeignKey(Dataset, on_delete=models.CASCADE), models.ImageField('Layout SC figure', blank=True, upload_to='datasets/static/images/matrices/sc2'), models.CharField('Layout SC title', max_length=40, blank=True)

class SC3(models.Model):
    dataset, matrix, name = models.ForeignKey(Dataset, on_delete=models.CASCADE), models.ImageField('Pragmatic SC figure', blank=True, upload_to='datasets/static/images/matrices/sc3'), models.CharField('Pragmatic SC title', max_length=40, blank=True)

class FC1(models.Model):
    dataset, matrix, name = models.ForeignKey(Dataset, on_delete=models.CASCADE), models.ImageField('Quantitative SC figure', blank=True, upload_to='datasets/static/images/matrices/fc1'), models.CharField('Quantitative SC title', max_length=40, blank=True)

class FC2(models.Model):
    dataset, matrix, name = models.ForeignKey(Dataset, on_delete=models.CASCADE), models.ImageField('Qualitative SC figure', blank=True, upload_to='datasets/static/images/matrices/fc2'), models.CharField('Qualitative SC title', max_length=40, blank=True)

class FC3(models.Model):
    dataset, matrix, name = models.ForeignKey(Dataset, on_delete=models.CASCADE), models.ImageField('Mechanistic SC figure', blank=True, upload_to='datasets/static/images/matrices/fc3'), models.CharField('Mechanistic SC title', max_length=40, blank=True)

class FC4(models.Model):
    dataset, matrix, name = models.ForeignKey(Dataset, on_delete=models.CASCADE), models.ImageField('Propagation SC figure', blank=True, upload_to='datasets/static/images/matrices/fc4'), models.CharField('Propagation SC title', max_length=40, blank=True)

