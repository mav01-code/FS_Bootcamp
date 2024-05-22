from django.urls import path

from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('add/', views.add, name='add'),
   path('complete/<int:id>', views.complete, name='complete'),
   path('delete/<int:id>', views.delete, name='delete'),
   path('api/listallTodoItems',views.listallTodoItems.as_view(),name='listallTodoItems'),
   path('api/api_add_todo',views.api_add_todo,name='api_add_todo'),
   path('api/task-change-status/<str:pk>/', views.change_status, name='change-status'),  # New endpoint
   path('api/todos/<int:pk>/', views.delete_todo, name='delete-todo'),
]