from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Marca')

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['name']

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, verbose_name='Modelo')
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='car_brand', verbose_name='Marca')
    factory_year = models.DateField(
        blank=True, null=True, verbose_name='Data de Fabricação')
    model_year = models.DateField(
        blank=True, null=True, verbose_name='Ano do Modelo')
    plate = models.CharField(max_length=10, unique=True,
                             blank=True, null=True, verbose_name='Placa')
    value = models.FloatField(blank=True, null=True, verbose_name='Preço')
    photo = models.ImageField(
        upload_to='cars/', blank=True, null=True, verbose_name='Imagem')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em')
    bio = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['model']

    def __str__(self):
        return self.model


class CarInventory(models.Model):
    cars_count = models.IntegerField(verbose_name='Quantidade')
    cars_value = models.FloatField(verbose_name='Preço')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Inventário'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
