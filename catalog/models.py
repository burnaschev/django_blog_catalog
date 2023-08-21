from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='Наименование')
    description_category = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f"{self.name_category} {self.description_category}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    preview = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    create_date = models.DateField(max_length=50, **NULLABLE, verbose_name='Дата создания')
    date_change = models.DateField(max_length=50, **NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f"{self.name} {self.description} {self.preview} {self.price}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
