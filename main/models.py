from django.db import models

class Micro(models.Model):
    title = models.CharField('Название', max_length=50)
    micro = models.TextField('Описание')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'
    
