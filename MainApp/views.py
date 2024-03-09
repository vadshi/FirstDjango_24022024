from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.ru",
    }
    return render(request, "index.html", context)


def about(request):
    author = {
        "Имя": "Иван",
        "Отчество": "Петрович",
        "Фамилия": "Иванов",
        "телефон": "8-923-600-01-02",
        "email": "vasya@mail.ru",
    }
    text = f"""
    <header>
        / <a href="/"> Home </a> / <a href="/items"> Items </a> / <a href="/about"> About </a>
    </header>
    Имя: <b>{author["Имя"]}</b><br>
    Отчество: <b>{author["Отчество"]}</b><br>
    Фамилия: <b>{author["Фамилия"]}</b><br>
    телефон: <b>{author["телефон"]}</b><br>
    email: <b>{author["email"]}</b><br>
    """
    return HttpResponse(text)


def get_item(request, item_id: int):
    """По указанному id возвращаем имя элемента и кол-во"""
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Item with id={item_id} not found.")
    else:
        context = {
            "item": item
        }
        return render(request, "item_page.html", context)


def get_items(request):
    items = Item.objects.all()
    context = {
        "items": items,
    }
    return render(request, "items_list.html", context)
