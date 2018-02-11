# from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView
from django.urls import reverse, reverse_lazy

from . models import List
# Create your views here.


class ListCreateView(CreateView):
    model = List
    template_name = 'home.html'
    fields = ['text']

    def get_success_url(self):
        return reverse('to:create')


class NoteListView(ListView):
    model = List
    template_name = 'list.html'


class ListDeleteView(DeleteView):
    model = List
    success_url = reverse_lazy('to:create')
