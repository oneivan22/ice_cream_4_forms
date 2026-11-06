from django.db import models


class Contest(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.TextField('Описание')
    price = models.IntegerField('Цена')
    comment = models.TextField('Комментарий', blank=True)

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.title