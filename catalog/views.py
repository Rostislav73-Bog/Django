from django.shortcuts import render
from django.http import Http404
from .models import My_model

from django.views import generic






def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_menu=My_model.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_menus': num_menu},
    )

class MenuListView(generic.ListView):
    model = My_model

    def get_queryset(self):
        return My_model.objects.all()


    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(MenuListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['some_data'] = 'This is just some data'
        return context

# class MenuDetailView(generic.DetailView):
#     model = My_model
#
#     def book_detail_view(request, pk):
#         try:
#             menu_id = My_model.objects.get(pk=pk)
#         except My_model.DoesNotExist:
#             raise Http404("Menu does not exist")
#
#         # book_id=get_object_or_404(Book, pk=pk)
#
#         return render(
#             request,
#             'catalog/menu_detail.html',
#             context={'menu': menu_id}
#         )
