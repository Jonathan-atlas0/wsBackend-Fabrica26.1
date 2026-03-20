from django.db import models

class Verificacao(models.Model):
    tipo = models.CharField(max_length=50)  
    url = models.CharField(max_length=500) 
    resultado = models.CharField(max_length=50)  
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.consulta}"