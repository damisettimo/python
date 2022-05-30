from django.urls import path

from app_coder import views

app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Home'),
<<<<<<< HEAD
    path('profesors', views.profesors, name='Profesors'),
    path('categorias', views.categorias, name='categoria-list'),
    path('students', views.students, name='Students'),
    path('homeworks', views.homeworks, name='Homeworks'),
    path('formHTML', views.form_hmtl),
    path('categoria-django-forms', views.categoria_forms_django, name='CategoriaDjangoForms'),
    path('profesor-django-forms', views.profesor_forms_django, name='ProfesorDjangoForms'),
    path('profesor/<int:pk>/update', views.update_profesor, name='UpdateProfesor'),
    path('profesor/<int:pk>/delete', views.delete_profesor, name='DeleteProfesor'),
=======
    path('entrenadores', views.entrenadores, name='Entrenadores'),
    # path('courses', views.courses, name='course-list'),
    path('students', views.students, name='Students'),
    path('homeworks', views.homeworks, name='Homeworks'),
    path('formHTML', views.form_hmtl),
    path('course-django-forms', views.course_forms_django, name='CourseDjangoForms'),
    path('entrenador-django-forms', views.entrenador_forms_django, name='EntrenadorDjangoForms'),
    path('entrenador/<int:pk>/update', views.update_entrenador, name='UpdateEntrenador'),
    path('entrenador/<int:pk>/delete', views.delete_entrenador, name='DeleteEntrenador'),
>>>>>>> pr/2
    path('homework-django-forms', views.homework_forms_django, name='HomeworkDjangoForms'),
    path('search', views.search, name='Search'),


    Dajngo documentation -->  https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
    Confirmo la url de la documentación es correcta, deben hacer scroll hasta esta parte:
    #
    from django.urls import path
    from myapp.views import AuthorCreateView, AuthorDeleteView, AuthorUpdateView

    # urlpatterns = [
    #     # ...
    #     path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    #     path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    #     path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    # ]
    #
    # Acá se ve la forma clara cómo Django realiza de forma stándar los nombres para urls, views y name del path.

    path('categorias', views.CategoriaListView.as_view(), name='categoria-list'),
    path('categoria/add/', views.CategoriaCreateView.as_view(), name='categoria-add'),
    path('categoria/<int:pk>/detail', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('categoria/<int:pk>/update', views.CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categoria/<int:pk>/delete', views.CategoriaDeleteView.as_view(), name='categoria-delete'),
]
