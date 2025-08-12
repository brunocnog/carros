# from django.shortcuts import render, redirect
from .models import Car
# from .forms import CarForm
from .forms import CarModelForm
# from django.views import View
from django.views.generic import ListView, CreateView

# def cars_view(request):

#     # cars = Car.objects.all()
#     # cars = Car.objects.filter(brand__name='Hyundai')
#     # cars = Car.objects.filter(model='Gol')
#     # cars = Car.objects.filter(model__contains='Gol Bola')

#     # colocar na url do navegador: http://127.0.0.1:8000/cars/?search=Teste123&nome=PycodeBR
#     # O print retorna <QueryDict: {'search': ['Teste123'], 'nome': ['PycodeBR']}>
#     # print(request.GET)

#     # Permite que o usuário faça uma busca pela URL: http://127.0.0.1:8000/cars/?search=opala
#     # search = request.GET.get('search')
#     # cars = Car.objects.filter(model__contains=search)

#     cars = Car.objects.all().order_by('model') # Ordena de A à Z
#     # cars = Car.objects.all().order_by('-model') # Ou assim para de Z à A
#     search = request.GET.get('search')

#     if search:
#         # cars = Car.objects.filter(model__contains=search)
#         # O icontains ignora o upper casa ou lower case
#         cars = Car.objects.filter(model__icontains=search)

#     return render(request,'cars.html',{'cars': cars})

# def cars_view(request):
#     cars = Car.objects.all().order_by('model')
#     search = request.GET.get('search')

#     if search:
#         cars = Car.objects.filter(model__icontains=search)
#     return render(request,'cars.html',{'cars': cars})


# class CarsView(View):

#     def get(self, request):
#         cars = Car.objects.all().order_by('model')
#         search = request.GET.get('search')

#         if search:
#             cars = Car.objects.filter(model__icontains=search)
#         return render(request,'cars.html',{'cars': cars})


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        # Subscreve a get_queryset() padrão que seria Car.objects.all() por um filtro que é .order_by('model')
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)
        return cars


# def new_car_view(request):
#     if request.method == 'POST':
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#     else:
#         new_car_form = CarModelForm()
#     return render(request, 'new_car.html', { 'new_car_form': new_car_form })


# class NewCarView(View):

#     def get(self, request):
#         new_car_form = CarModelForm()
#         return render(request, 'new_car.html', {'new_car_form': new_car_form})

#     def post(self, request):
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#         return render(request, 'new_car.html', {'new_car_form': new_car_form})


class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/' # Não utiliza a name da url que está em app.urls e sim a url dirata.  
