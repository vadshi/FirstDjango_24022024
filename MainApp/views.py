from django.http import HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.ru",
    }
    return render(request, "index.html", context)


def about(request):
    author = {
        "first_name": "Иван",
        "middle_name": "Петрович",
        "last_name": "Иванов",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru",
    }
    context = {
        "author": author
    }
    return render(request, "about.html", context)


def get_item(request, item_id: int):
    """По указанному id возвращаем имя элемента и кол-во"""
    try:
        item = Item.objects.get(id=item_id)
        colors = []
        # Проверяем, что у элемента есть хоть один цвет
        if item.colors.exists():
            colors = item.colors.all()
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Item with id={item_id} not found.")
    else:
        context = {
            "item": item,
            "colors": colors,
        }
        return render(request, "item_page.html", context)


def get_items(request):
    items = Item.objects.all()
    context = {
        "items": items,
    }
    return render(request, "items_list.html", context)
