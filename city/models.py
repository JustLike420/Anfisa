from django.db import models

# Create your models here.
class Citys(models.Model):
    name = models.CharField('Имя', max_length=50)
    city = models.TextField('Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'