from .models import Category


def navbar_menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
