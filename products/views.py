from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.
def index(request):
    products = Product.latest_products()
    return render(request, 'products/index.html', {'products': products})

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
            url = url.lower()
            if not (url.startswith('http://') or url.startswith('https://')):
                url = 'http://' + url
            product = Product()
            product.init(title, url, body, icon, image, request.user)
            product.save()
            return redirect('product_detail', product.id)
        else:
            return render(request, 'products/add.html', {'error': 'All fields are mandatory'})
    return render(request, 'products/add.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    return render(request, 'products/detail.html', {'product': product})

@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk = product_id)
        product.upvote()
        return redirect('product_detail', product_id)
