from django.db import models

class Temperatura(models.Model):
    valor = models.FloatField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.valor} °C"
