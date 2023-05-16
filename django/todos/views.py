from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect

from .models import Todo
from .forms import TodoForm


class TodoMixin:
    queryset = Todo.objects.all()
    success_url = reverse_lazy('create-todo')


class CreateTodoView(TodoMixin, generic.CreateView, generic.ListView):
    form_class = TodoForm
    template_name = 'index.html'
    context_object_name = 'todos'


class DeleteTodoView(TodoMixin, generic.DeleteView):
    pass


class CompleteTodoView(TodoMixin, generic.UpdateView):
    
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        self.object = self.get_object()
        self.object.done = True
        self.object.save()

        return redirect(self.get_success_url())
