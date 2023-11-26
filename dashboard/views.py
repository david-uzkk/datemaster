from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.models import User
from datetime import date, timedelta
from .forms import ProductForm

# Create your views here.
@login_required
def index(request):
    #TODOS OS PRODUTOS
    items = Product.objects.raw('SELECT * FROM dashboard_product')
    item_countp = len(items)

    #TODOS OS PRODUTOS ALTOS
    current_date = date.today()
    three_months_ago = current_date + timedelta(days=3*30)
    items = Product.objects.raw('SELECT * FROM dashboard_product WHERE expiration_date > %s', [three_months_ago])
    item_counta = len(items)

    #TODOS OS PRODUTOS MEDIOS
    current_date = date.today()
    thirty_days_ago = current_date + timedelta(days=30)
    ninety_days_ago = current_date + timedelta(days=90)
    query = ''' SELECT * FROM dashboard_product WHERE expiration_date BETWEEN %s AND %s'''
    items = Product.objects.raw(query, [thirty_days_ago, ninety_days_ago])
    item_countm = len(items)

    #TODOS OS PRODUTOS MEDIOS BAIXAS
    current_date = date.today()
    thirty_days_from_now = current_date + timedelta(days=30)
    items = Product.objects.filter(expiration_date__gt=current_date, expiration_date__lt=thirty_days_from_now)
    item_countb = len(items)

    #TODOS OS PRODUTOS COMIDA
    items = Product.objects.raw("SELECT * FROM dashboard_product WHERE category='Comida'")
    item_countcc = len(items)

    #TODOS OS PRODUTOS MEDICAMENTO
    items = Product.objects.raw("SELECT * FROM dashboard_product WHERE category='Medicamentos'")
    item_countcm = len(items)

    #TODOS OS PRODUTOS ELETRONICOS
    items = Product.objects.raw("SELECT * FROM dashboard_product WHERE category='Eletrônicos'")
    item_countce = len(items)

    #TODOS OS PRODUTOS OUTROS
    items = Product.objects.raw("SELECT * FROM dashboard_product WHERE category='Outros'")
    item_countco = len(items)

    #TODOS OS PRODUTOS 1 MES
    current_date = date.today()
    days_count1 = current_date + timedelta(days=0)
    days_count2 = current_date + timedelta(days=30)
    query = ''' SELECT * FROM dashboard_product WHERE expiration_date BETWEEN %s AND %s'''
    items = Product.objects.raw(query, [days_count1, days_count2])
    item_countm1 = len(items)

    #TODOS OS PRODUTOS 2 MES
    current_date = date.today()
    days_count1 = current_date + timedelta(days=30)
    days_count2 = current_date + timedelta(days=60)
    query = ''' SELECT * FROM dashboard_product WHERE expiration_date BETWEEN %s AND %s'''
    items = Product.objects.raw(query, [days_count1, days_count2])
    item_countm2 = len(items)

    #TODOS OS PRODUTOS 3 MES
    current_date = date.today()
    days_count1 = current_date + timedelta(days=60)
    days_count2 = current_date + timedelta(days=90)
    query = ''' SELECT * FROM dashboard_product WHERE expiration_date BETWEEN %s AND %s'''
    items = Product.objects.raw(query, [days_count1, days_count2])
    item_countm3 = len(items)

    #TODOS OS PRODUTOS 4 MES
    current_date = date.today()
    days_count1 = current_date + timedelta(days=90)
    days_count2 = current_date + timedelta(days=120)
    query = ''' SELECT * FROM dashboard_product WHERE expiration_date BETWEEN %s AND %s'''
    items = Product.objects.raw(query, [days_count1, days_count2])
    item_countm4 = len(items)

    #TODOS OS PRODUTOS 5 MES
    current_date = date.today()
    days_count1 = current_date + timedelta(days=120)
    days_count2 = current_date + timedelta(days=150)
    query = ''' SELECT * FROM dashboard_product WHERE expiration_date BETWEEN %s AND %s'''
    items = Product.objects.raw(query, [days_count1, days_count2])
    item_countm5 = len(items)

    #TODOS OS PRODUTOS 6 MES
    current_date = date.today()
    three_months_ago = current_date + timedelta(days=6*30)
    items = Product.objects.raw('SELECT * FROM dashboard_product WHERE expiration_date > %s', [three_months_ago])
    item_countm6 = len(items)

    context = {
        'items': items,
        'item_countp': item_countp,
        'item_counta': item_counta,
        'item_countm': item_countm,
        'item_countb': item_countm,
        'item_countcc': item_countcc,
        'item_countcm': item_countcm,
        'item_countce': item_countce,
        'item_countco': item_countco,
        'item_countm1': item_countm1,
        'item_countm2': item_countm2,
        'item_countm3': item_countm3,
        'item_countm4': item_countm4,
        'item_countm5': item_countm5,
        'item_countm6': item_countm6,
    }
    return render(request, 'dashboard/index.html', context)

@login_required()
def staff(request):
    # Obtém todos os usuários
    users = User.objects.all()
    user_count = users.count()

    # Cria o contexto
    context = {
        'users': users,
        'user_count': user_count,
    }
    return render(request, 'dashboard/staff.html', context)

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
    #TODOS OS PRODUTOS
    items = Product.objects.raw('SELECT * FROM dashboard_product')
    item_countp = len(items)

    #TODOS OS PRODUTOS ALTOS
    
    current_date = date.today()
    thirty_days_from_now = current_date + timedelta(days=30)
    items = Product.objects.filter(expiration_date__gt=current_date, expiration_date__lt=thirty_days_from_now)
    item_countb = len(items)

    #TODOS OS PRODUTOS MEDIOS
    current_date = date.today()
    thirty_days_ago = current_date + timedelta(days=30)
    ninety_days_ago = current_date + timedelta(days=90)
    query = ''' SELECT * FROM dashboard_product WHERE expiration_date BETWEEN %s AND %s'''
    items = Product.objects.raw(query, [thirty_days_ago, ninety_days_ago])
    item_countm = len(items)

    #TODOS OS PRODUTOS MEDIOS BAIXAS
    current_date = date.today()
    three_months_ago = current_date + timedelta(days=3*30)
    items = Product.objects.raw('SELECT * FROM dashboard_product WHERE expiration_date > %s', [three_months_ago])
    item_counta = len(items)

    context = {
        'items': items,
        'item_countp': item_countp,
        'item_counta': item_counta,
        'item_countm': item_countm,
        'item_countb': item_countm,
    }
    return render(request, 'dashboard/alta.html', context)

@login_required
def media(request):
    #TODOS OS PRODUTOS
    items = Product.objects.raw('SELECT * FROM dashboard_product')
    item_countp = len(items)

    #TODOS OS PRODUTOS ALTOS
    current_date = date.today()
    thirty_days_from_now = current_date + timedelta(days=30)
    items = Product.objects.filter(expiration_date__gt=current_date, expiration_date__lt=thirty_days_from_now)
    item_countb = len(items)

    #TODOS OS PRODUTOS MEDIOS
    current_date = date.today()
    three_months_ago = current_date + timedelta(days=3*30)
    items = Product.objects.raw('SELECT * FROM dashboard_product WHERE expiration_date > %s', [three_months_ago])
    item_counta = len(items)

    #TODOS OS PRODUTOS MEDIOS BAIXAS
    current_date = date.today()
    thirty_days_ago = current_date + timedelta(days=30)
    ninety_days_ago = current_date + timedelta(days=90)
    query = ''' SELECT * FROM dashboard_product WHERE expiration_date BETWEEN %s AND %s'''
    items = Product.objects.raw(query, [thirty_days_ago, ninety_days_ago])
    item_countm = len(items)

    context = {
        'items': items,
        'item_countp': item_countp,
        'item_counta': item_counta,
        'item_countm': item_countm,
        'item_countb': item_countm,
    }
    return render(request, 'dashboard/media.html', context)

@login_required
def baixa(request):
#TODOS OS PRODUTOS
    items = Product.objects.raw('SELECT * FROM dashboard_product')
    item_countp = len(items)

    #TODOS OS PRODUTOS ALTOS
    current_date = date.today()
    three_months_ago = current_date + timedelta(days=3*30)
    items = Product.objects.raw('SELECT * FROM dashboard_product WHERE expiration_date > %s', [three_months_ago])
    item_counta = len(items)

    #TODOS OS PRODUTOS MEDIOS
    current_date = date.today()
    thirty_days_ago = current_date + timedelta(days=30)
    ninety_days_ago = current_date + timedelta(days=90)
    query = ''' SELECT * FROM dashboard_product WHERE expiration_date BETWEEN %s AND %s'''
    items = Product.objects.raw(query, [thirty_days_ago, ninety_days_ago])
    item_countm = len(items)

    #TODOS OS PRODUTOS MEDIOS BAIXAS
    current_date = date.today()
    thirty_days_from_now = current_date + timedelta(days=30)
    items = Product.objects.filter(expiration_date__gt=current_date, expiration_date__lt=thirty_days_from_now)
    item_countb = len(items)

    context = {
        'items': items,
        'item_countp': item_countp,
        'item_counta': item_counta,
        'item_countm': item_countm,
        'item_countb': item_countm,
    }
    return render(request, 'dashboard/baixa.html', context)