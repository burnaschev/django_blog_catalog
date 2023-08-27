from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    header = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, **NULLABLE, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    create_date = models.DateField(max_length=50, **NULLABLE, verbose_name='Дата создания')
    is_public = models.BooleanField(default=True, verbose_name='Признак публикаций')
    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f"{self.header} {self.slug} {self.content} {self.count_views}"

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
