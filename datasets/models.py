from django.db import models

# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=255)
    field = models.CharField('Discipline', max_length=255)
    space = models.CharField('Spatial scale', max_length=255, null=True)
    time = models.CharField('Temporal scale', max_length=255, null=True)
    sc1, sc2, sc3 = models.PositiveIntegerField('Linking SC', null=True), models.PositiveIntegerField('Layout SC', null=True), models.PositiveIntegerField('Pragmatic SC', null=True)
    fc1, fc2, fc3, fc4 = models.PositiveIntegerField('Quantitative FC', null=True), models.PositiveIntegerField('Relational FC', null=True), models.PositiveIntegerField('Mechanistic FC', null=True), models.PositiveIntegerField('Propagation FC', null=True)
    icon = models.ImageField('Icon', blank=True, upload_to='conn_browser/datasets/images/icons')
    slug = models.SlugField(default="", null=False)
    def __str__(self):
        return f'{self.name}'

#    matrix = models.ForeignKey(Dataset, on_delete=models.CASCADE)
#    network = models.ForeignKey(Dataset, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)

