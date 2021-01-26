from django.views.generic import TemplateView
from .models import SlideShowImage
from app_product.models import Shop, Category


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = SlideShowImage.objects.all()
        context['best_shops'] = Shop.objects.all()[:3]
        context['categories'] = Category.objects.filter(parent=None)
        return context


class SearchView(TemplateView):
    template_name = 'main/search.html'
