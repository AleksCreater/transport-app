from django.db import models

class User(models.Model):
    user_name = models.CharField(null=True, max_length=50, verbose_name='Имя пользователя')
    user_surname = models.CharField(null=True, max_length=100, verbose_name='Фамилия пользователя')
    user_number = models.IntegerField(null=True, blank=True, verbose_name='Номер телефона')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
        
