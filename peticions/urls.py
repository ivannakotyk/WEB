from . import views
from django.urls import path

urlpatterns = [
    path('', views.petitions, name = 'peticions'),
    path('create/', views.create, name = "create"),
    path('<int:pk>', views.PeticionsDetailView.as_view(), name = 'detail'),
    path('<int:pk>/edit', views.PeticionUpdateView.as_view(), name='edit'),
    path('<int:id>/delete-item', views.deleteItem, name='delete-item'),
    path('<int:id>/vote', views.vote_petition, name='vote')
]