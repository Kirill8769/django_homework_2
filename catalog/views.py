from django.shortcuts import render, get_object_or_404

from .models import Product, Contact


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Главная',
    }
    return render(request, 'catalog/index.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product,
        'title': product.name,
    }
    return render(request, 'catalog/product_detail.html', context)


def contacts(request):
    context = {
        'contact': Contact.objects.get(pk=1),
        'title': 'Контакты',
    }
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Новое обращение\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}")
    return render(request, 'catalog/contacts.html', context)
