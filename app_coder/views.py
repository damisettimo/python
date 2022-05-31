from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict


from app_coder.models import Categoria, Jugador, Entrenador, Homework
from app_coder.forms import CategoriaForm, EntrenadorForm, HomeworkForm



def index(request):
    return render(request, "app_coder/home.html")


def entrenadores(request):
    entrenadores = Entrenador.objects.all()

    context_dict = {
        'entrenadores': entrenadores,
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/entrenadores.html"
    )


def categorias(request):
    categorias = Categoria.objects.all()

    context_dict = {
        'categorias': categorias
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/categorias.html"
    )


def jugadores(request):
    jugadores = Jugador.objects.all()

    context_dict = {
        'jugadores': jugadores
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/jugadores.html"
    )


def homeworks(request):
    homeworks = Homework.objects.all()

    context_dict = {
        'homeworks': homeworks
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/homeworks.html"
    )


def form_hmtl(request):

    if request.method == 'POST':
        categoria = Categoria(name=request.POST['name'], code=request.POST['code'])
        categoria.save()

        categorias = Categoria.objects.all()
        context_dict = {
            'categorias': categorias
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/categorias.html"
        )

    return render(
        request=request,
        template_name='app_coder/formHTML.html'
    )


def categoria_forms_django(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        if categoria_form.is_valid():
            data = categoria_form.cleaned_data
            categoria = Categoria(name=data['name'], code=data['code'])
            categoria.save()

            categorias = Categoria.objects.all()
            context_dict = {
                'categorias': categorias
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/categorias.html"
            )

    categoria_form = CategoriaForm(request.POST)
    context_dict = {
        'categoria_form': categoria_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/categoria_django_forms.html'
    )


def entrenador_forms_django(request):
    if request.method == 'POST':
        entrenador_form = EntrenadorForm(request.POST)
        if entrenador_form.is_valid():
            data = entrenador_form.cleaned_data
            entrenadores = Entrenador(
                name=data['name'],
                last_name=data['last_name'],
                email=data['email'],
                profession=data['profession'],
            )
            entrenadores.save()

            entrenadores = Entrenador.objects.all()
            context_dict = {
                'entrenadores': entrenadores,
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/entrenadores.html"
            )

    entrenador_form = EntrenadorForm(request.POST)
    context_dict = {
        'entrenador_form': entrenador_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/entrenador_django_forms.html'
    )

def update_entrenador(request, pk: int):
    entrenador = Entrenador.objects.get(pk=pk)

    if request.method == 'POST':
        entrenador_form = EntrenadorForm(request.POST)
        if entrenador_form.is_valid():
            data = entrenador_form.cleaned_data
            entrenador.name = data['name']
            entrenador.last_name = data['last_name']
            entrenador.email = data['email']
            entrenador.profession = data['profession']
            entrenador.save()

            entrenador = Entrenador.objects.all()
            context_dict = {
                'entrenador': entrenador,
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/entrenadores.html"
            )

    entrenador_form = EntrenadorForm(model_to_dict(entrenador))
    context_dict = {
        'entrenador': entrenador,
        'entrenador_form': entrenador_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/entrenador_form.html'
    )


def delete_entrenador(request, pk: int):
    entrenador = Entrenador.objects.get(pk=pk)
    if request.method == 'POST':
        entrenador.delete()

        entrenador = Entrenador.objects.all()
        context_dict = {
            'entrenador': entrenador,
        }
        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/entrenador.html"
        )

    context_dict = {
        'entrenador': entrenador,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/entrenador_confirm_delete.html'
    )


def homework_forms_django(request):
    if request.method == 'POST':
        homework_form = HomeworkForm(request.POST)
        if homework_form.is_valid():
            data = homework_form.cleaned_data
            homework = Homework(
                name=data['name'],
                due_date=data['due_date'],
                is_delivered=data['is_delivered'],
            )
            homework.save()

            homeworks = Homework.objects.all()
            context_dict = {
                'homeworks': homeworks
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/homeworks.html"
            )

    homework_form = HomeworkForm(request.POST)
    context_dict = {
        'homework_form': homework_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/homework_django_forms.html'
    )


def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        categorias = Categoria.objects.filter(name__contains=search_param)
        context_dict = {
            'categorias': categorias
        }
    elif request.GET['code_search']:
        search_param = request.GET['code_search']
        categorias = Categoria.objects.filter(code__contains=search_param)
        context_dict = {
            'categorias': categorias
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        categorias = Categoria.objects.filter(query)
        context_dict = {
            'categorias': categorias
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CategoriaListView(ListView):
    model = Categoria
    template_name = "app_coder/categoria_list.html"


class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = "app_coder/categoria_detail.html"


class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = "app_coder/categoria_form.html"
    success_url = "/app_coder/categorias"
    success_url = reverse_lazy('app_coder:categoria-list')
    fields = ['name', 'code']


class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = "app_coder/categoria_form.html"
    success_url = "/app_coder/categorias"
    success_url = reverse_lazy('app_coder:categoria-list')
    fields = ['name', 'code']


class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = "/app_coder/categorias"
    success_url = reverse_lazy('app_coder:categoria-list')
