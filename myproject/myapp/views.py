from django.shortcuts import render

# Create your views here.
def my_view(request):
    context = {
        'title': 'Mi Proyecto Django',
        'items': ['Manzana', 'Banana', 'Naranja'],
        'show_items': True,
    }
    return render(request, 'myapp/index.html', context)