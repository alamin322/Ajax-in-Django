from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name='homeview'),
    path('save/', view=views.save_info, name='savedata'),
    path('update/', view=views.update_info, name='updatedata'),
    path('delete/', view=views.delete_info, name='deletedata'),
]
