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
    return render(request, 'dashboard/media.html')

@login_required
def baixa(request):
    return render(request, 'dashboard/baixa.html')