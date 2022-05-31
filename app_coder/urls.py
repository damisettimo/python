from django.urls import path
from app_coder import views


app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Home'),
    path('entrenadores', views.entrenadores, name='Entrenadores'),
    path('categorias', views.categoriass, name='categoria-list'),
    path('jugadores', views.jugadores, name='Jugadores'),
    path('homeworks', views.homeworks, name='Homeworks'),
    path('formHTML', views.form_hmtl),
    path('course-django-forms', views.categoria_forms_django, name='CourseDjangoForms'),
    path('entrenador-django-forms', views.entrenador_forms_django, name='EntrenadorDjangoForms'),
    path('entrenador/<int:pk>/update', views.update_entrenador, name='UpdateEntrenador'),
    path('entrenador/<int:pk>/delete', views.delete_entrenador, name='DeleteEntrenador'),
    path('homework-django-forms', views.homework_forms_django, name='HomeworkDjangoForms'),
    path('search', views.search, name='Search'),
    ]

    # Dajngo documentation -->  https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
    # Confirmo la url de la documentación es correcta, deben hacer scroll hasta esta parte:
    #
from django.urls import path
from app_coder.views import * #AuthorCreateView, AuthorDeleteView, AuthorUpdateView

    
    #     # ...
    #     path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    #     path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    #     path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    # ]
    
urlpatterns = [
    path('categorias', views.CategoriaListView.as_view(), name='categoria-list'),
    path('categoria/add/', views.CategoriaCreateView.as_view(), name='categoria-add'),
    path('categoria/<int:pk>/detail', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('categoria/<int:pk>/update', views.CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categoria/<int:pk>/delete', views.CategoriaDeleteView.as_view(), name='categoria-delete'),
]
