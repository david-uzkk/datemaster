from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.
@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required
def product(request):
    items = Product.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'dashboard/product.html')

@login_required
def alta(request):
    return render(request, 'dashboard/alta.html')

@login_required
def media(request):
    return render(request, 'dashboard/media.html')

@login_required
def baixa(request):
    return render(request, 'dashboard/baixa.html')