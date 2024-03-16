from django.shortcuts import render

from .models import Product, Contact


def index(request):
    data = Product.objects.all().order_by('-id')[:5]
    for count, item in enumerate(data, start=1):
        print(f"{count}. {item}")
    return render(request, 'catalog/index.html')


def contacts(request):
    data = Contact.objects.last()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Новое обращение\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}")
    return render(request, 'catalog/contacts.html', {"data": data})
