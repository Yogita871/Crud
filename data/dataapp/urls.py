from django.urls import path
from dataapp import views
urlpatterns = [
    path('create',views.create),
    path('dash',views.dashboard),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
]
