from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name='homeview'),
    path('save/', view=views.save_info, name='savedata'),
]
