from django.urls import path
from .views import index, by_rubric, UserCreateView

urlpatterns = [
    #path('<int:delete_id>/',UserDeleteView.as_view(), name='delete'), 
    path('add/', UserCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    ]
