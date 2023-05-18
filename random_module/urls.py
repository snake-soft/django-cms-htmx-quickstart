from django.urls.conf import path
from .views import RandomModuleView


urlpatterns = [
    path('', RandomModuleView.as_view(), name='random-module'),
]
