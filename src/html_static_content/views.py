from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'html_static_content/index.html'
