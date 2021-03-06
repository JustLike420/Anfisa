from django.db import models

# БД мороженоеог название:описание:изображение
class Icecream(models.Model):
    name = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    img = models.ImageField(default='default.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'


