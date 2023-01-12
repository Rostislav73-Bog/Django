from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.MenuListView.as_view(), name='menu'),
    # path(r'^menu/(?P<pk>\d+)$', views.MenuDetailView.as_view(), name='menu-detail'),
]


