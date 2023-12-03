from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', get_profile),
    path('products/', get_product),

]
