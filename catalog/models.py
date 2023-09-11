from django.conf import settings
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
    users = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Пользователь'
    )

    def __str__(self):
        return f"{self.name} {self.description} {self.preview} {self.price}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    SIGN_TRUE = True
    SIGN_FALSE = False
    SIGN = ((SIGN_TRUE, 'Активен',),
            (SIGN_FALSE, 'Неактивен'),)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версий')
    version_name = models.CharField(max_length=100, verbose_name='Название версий')
    version_sign = models.BooleanField(default=SIGN_TRUE, choices=SIGN, verbose_name='Признак версий')

    def __str__(self):
        return f'{self.version_name}/{self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версий'
