from django.shortcuts import render


def index(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Новое обращение\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}")
    return render(request, 'catalog/contacts.html')
