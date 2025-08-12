from django import forms
from .models import Brand, Car
from datetime import date


# class CarForm(forms.Form):
#     model = forms.CharField(max_length=200, label='Modelo')
#     brand = forms.ModelChoiceField(Brand.objects.all(), label='Marca')
#     factory_year = forms.DateField(label='Ano de Fabricação')
#     model_year = forms.DateField(label='Ano do Modelo')
#     plate = forms.CharField(max_length=10, label='Placa')
#     value = forms.FloatField(label='Preço')
#     photo = forms.ImageField(label='Imagem')

#     def save(self):
#         car = Car(
#             model = self.cleaned_data['model'],
#             brand = self.cleaned_data['brand'],
#             factory_year = self.cleaned_data['factory_year'],
#             model_year = self.cleaned_data['model_year'],
#             plate = self.cleaned_data['plate'],
#             value = self.cleaned_data['value'],
#             photo = self.cleaned_data['photo'],            
#         )
#         car.save()
#         return car
    

class CarModelForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = '__all__'

    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo R$20.000,00')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        year = factory_year.year
        if not (1975 <= year <= date.today().year):
            self.add_error('factory_year', 'O ano deve estar entre 1975 e o atual.e')
        return factory_year