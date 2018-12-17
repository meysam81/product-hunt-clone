from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.
def index(request):
    products = Product.latest_products()
    return render(request, 'product/index.html', {'products': products})

@login_required
def add(request):
    if request.method == 'POST':
        formData = request.POST
        title = formData['title']
        body = formData['body']
        url = formData['url']
        icon = request.FILES['icon']
        image = request.FILES['image']
        print(title, body, url, icon, image, request.user)
        if title and body and url and icon and image:
            if not (url.startswith('http://') or url.startswith('https://')):
                url = 'http://' + url
            product = Product()
            product.init(title, url, body, icon, image, request.user)
            product.save()
            return redirect('index')
        else:
            return render(request, 'product/add_product.html', {'error': 'All fields are mandatory'})
    return render(request, 'product/add_product.html')
