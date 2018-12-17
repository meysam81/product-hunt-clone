from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'product/index.html')

@login_required
def add(request):
    return render(request, 'product/add_product.html')
