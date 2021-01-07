from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SlideShowImage


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slide_images'] = SlideShowImage.objects.all()
        return context
