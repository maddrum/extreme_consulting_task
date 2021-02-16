from django.conf.urls import url

app_name = 'html_static_content'
from html_static_content import views

urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='index_page'),
]
