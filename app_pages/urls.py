from django.urls import path
from app_pages.views import translation_example, greetings_page

urlpatterns = [
    path('example/', translation_example, name='example'),
    path('greetings_page/', greetings_page, name='greetings_page'),
]