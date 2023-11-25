from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from datetime import date, timedelta
from .forms import ProductForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required()
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required
def product(request):
    items = Product.objects.all()
    #items = Product.objects.raw('SELECT * FROM dashboard_product')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/product.html', context)

@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST' :
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required
def alta(request):
    #items = Product.objects.all()
    current_date = date.today()

    # Calcula a data
    three_months_ago = current_date + timedelta(days=3*30)
    
    items = Product.objects.raw('SELECT * FROM dashboard_product WHERE expiration_date > %s', [three_months_ago])
    context = {
        'items': items,
    }
    return render(request, 'dashboard/alta.html', context)

@login_required
def media(request):
    current_date = date.today()

    # Calcula a data
    thirty_days_ago = current_date + timedelta(days=30)
    ninety_days_ago = current_date + timedelta(days=90)

    # Use a função NOW() ou CURDATE() dependendo do seu banco de dados
    query = '''
        SELECT * 
        FROM dashboard_product 
        WHERE expiration_date BETWEEN %s AND %s
    '''

    items = Product.objects.raw(query, [thirty_days_ago, ninety_days_ago])

    context = {
        'items': items,
    }
    return render(request, 'dashboard/media.html', context)

@login_required
def baixa(request):
    #items = Product.objects.all()
    current_date = date.today()

    # Calcula a data
    thirty_days_from_now = current_date + timedelta(days=30)

    # Filtra os produtos com menos de 30 dias até a data de expiração
    items = Product.objects.filter(expiration_date__gt=current_date, expiration_date__lt=thirty_days_from_now)
    context = {
        'items': items,
    }
    return render(request, 'dashboard/baixa.html', context)