from django.urls import path
from .views import menu, acercade, carrousel, formulario, galeria, login_view, django_view, form_tattoo, eliminar, modificar, home

urlpatterns = [
    path('', menu, name='menu'),          # Ruta para la vista del menú (Página principal)
    path('acercade/', acercade, name='acercade'),  # Ruta para la vista de "acerca de"
    path('carrousel/', carrousel, name='carrousel'),  # Ruta para el carrusel
    path('formulario/', formulario, name='formulario'),  # Ruta para el formulario
    path('galeria/', galeria, name='galeria'),  # Ruta para la galería
    path('login/', login_view, name='login'),  # Ruta para el login
    path('django/', django_view, name='django' ),
    path('form_tattoo', form_tattoo, name='form_tattoo' ),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('home/',home, name='home'),
]
