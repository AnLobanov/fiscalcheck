from django.db import models

class KKM(models.Model):
    ser = models.IntegerField(verbose_name="Серийный номер")
    name = models.TextField(default='UNKNOWN', verbose_name="Имя компьютера")
    fn = models.ForeignKey('FN', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Фискальный накопитель")
    def __str__(self):
        return str(self.ser)
    
    class Meta:
        verbose_name_plural = "ККМ"

class FN(models.Model):
    reg = models.IntegerField(verbose_name="Регистрационный номер")
    exp = models.DateField(verbose_name="Срок действия")

    def __str__(self):
        return str(self.reg)
    
    class Meta:
        verbose_name_plural = "ФН"
