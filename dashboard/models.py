from django.db import models

# Create your models here.
CATEGORY = (
    ('Comida', 'Comida'),
    ('Medicamentos', 'Medicamentos'),
    ('Eletrônicos', 'Eletrônicos'),
    ('Outros', 'Outros'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    lot = models.CharField(max_length=20, null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=False, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    observation = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.lot} - {self.name}'