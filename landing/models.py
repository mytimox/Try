from django.db import models

# Create your models here


class PIB(models.Model):

    first_name = models.CharField(max_length=22, verbose_name="Ім'я")
    last_name = models.CharField(max_length=33, verbose_name='Прізвище')
    email = models.EmailField(verbose_name='E-mail', default='example@email.co')

    def __str__(self):
        st = '{} {}'.format(self.first_name, self.last_name)
        return st
    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'