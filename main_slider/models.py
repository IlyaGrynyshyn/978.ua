from django.db import models


class Slider(models.Model):
    title = models.CharField(verbose_name='Назва', max_length=100)
    image = models.ImageField(verbose_name='Фотокартка', upload_to='main_slider/')
    slug = models.SlugField(unique=True, db_index=True)
    post = models.BooleanField(default=False, verbose_name='Опубліковано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайдер на головній сторінці'
        verbose_name_plural = 'Слайдер на головній сторінці'
