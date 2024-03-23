from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Category, Contact, Product


def index(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'object_list': products,
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


def product_create(request):
    context = {
        'categories': Category.objects.all(),
        'title': 'Добавление нового товара',
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        if category == 'Выберите категорию товара':
            category = None
        price = request.POST.get('price')
        print(123, category)
        Product.objects.create(
            name=name,
            description=description,
            image=image,
            category_id=category,
            price=price,
        )
        context['info'] = f'Товар {name} добавлен'
    return render(request, 'catalog/product_create.html', context)


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
