from django.shortcuts import render
from ice_cream.models import IceCream


def index(request):
    template = "homepage/index.html"
    # Только нужные поля + проверка флагов публикации:
    ice_cream_list = IceCream.objects.values(
        "id", "title", "price", "description"
    ).filter(
        is_published=True,  # сорт разрешён к публикации
        is_on_main=True,  # и разрешён на главной
        category__is_published=True,  # и категория разрешена к публикации
    )
    context = {"ice_cream_list": ice_cream_list}
    return render(request, template, context)
