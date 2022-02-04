from django.db import models

# Create your models here.
class Gasto(models.Model):
    concepto = models.TextField()
    valor = models.IntegerField()
    fecha = models.DateTimeField()

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'

    def __str__(self):
        return f"Objeto gasto {self.id}"