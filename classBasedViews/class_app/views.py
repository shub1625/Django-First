from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models
# Create your views here.


class Indexview(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        context = TemplateView.get_context_data(self, **kwargs)
        context['ineject'] = "Hey I'm context"
        return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'schools_details'
    model = models.School

    Template_name = r'class_app/school_detail.html'
