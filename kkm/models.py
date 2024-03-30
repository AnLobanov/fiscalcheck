from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group, User
from django.core.validators import MaxValueValidator, MinValueValidator

class KKM(models.Model):
    reg = models.TextField(verbose_name="Регистрационный номер", primary_key=True, unique=True, null=False, blank=False)
    ser = models.TextField(verbose_name="Серийный номер", unique=True, null=False, blank=False)
    name = models.TextField(null=False, verbose_name="Имя компьютера")
    exp = models.DateField(verbose_name="Срок действия ФН", null=False, blank=False)
    adr = models.TextField(null=False, blank=False, verbose_name="Адрес магазина")
    yl = models.TextField(null=False, blank=False, verbose_name="Юридическое лицо")
    
    def __str__(self):
        return str(self.reg)
    
    @property
    def days(self):
        return (self.exp - datetime.now().date()).days

    class Meta:
        verbose_name_plural = "ККМ"
        verbose_name = "ККМ"

class ClientError(models.Model):
    name = models.TextField(null=False, blank=False, verbose_name="Имя компьютера")
    message = models.TextField(null=True, blank=True, verbose_name="Сообщение")
    dt = models.DateTimeField(verbose_name="Время ошибки", null=False, blank=False)
    
    def __str__(self):
        return 'Ошибка'

    class Meta:
        verbose_name_plural = "Ошибки"
        verbose_name = "ошибки"

class Settings(models.Model):
    id = models.IntegerField(primary_key=True, default=0, unique=True, blank=False, null=False)
    days = models.IntegerField(verbose_name="Количество дней до истечения ФН для включения уведомлений",
                               validators=[
                                   MaxValueValidator(60),
                                   MinValueValidator(0)
                               ]
                               )
    notify = models.BooleanField(verbose_name="Посылать уведомления", default=True)
    
    def __str__(self):
        return 'Значения по умолчанию'

    class Meta:
        verbose_name_plural = "Настройки"
        verbose_name = "настройки"

def user_created(sender, instance, created, **kwargs):
    instance.groups.add(Group.objects.get(name='django'))

post_save.connect(user_created, sender=User, dispatch_uid="user_created")