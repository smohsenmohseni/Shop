from django.views.generic import TemplateView
from app_product.models import Category
from .models import SlideShowImage


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = SlideShowImage.objects.all()
        context['categories'] = Category.objects.filter(parent=None)
        return context
