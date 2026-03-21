from django.db import models

class Tipo(models.Model):
    nome = models.CharField(max_length=10)  # Tabela pai

    def __str__(self):
        return self.nome


class ConsultaVirusTotal(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)
    status = models.CharField(max_length=50)
    malicioso = models.IntegerField()
    inofensivo = models.IntegerField()
    suspeito = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url} - {self.status}"


class ConsultaIPInfo(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    regiao = models.CharField(max_length=100)
    pais = models.CharField(max_length=10)
    organizacao = models.CharField(max_length=200)
    timezone = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip} - {self.pais}"