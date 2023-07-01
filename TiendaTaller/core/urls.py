from django.urls import path
from .views import home, poblar_bd, vehiculo, vehiculo_tienda, vehiculo_ficha,nosotros,pag_caja,pag_electri,pag_suspe,contacto,registro,iniciosesion, index

urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('vehiculo/<action>/<id>', vehiculo, name="vehiculo"),
    path('vehiculo_tienda', vehiculo_tienda, name="vehiculo_tienda"),
    path('vehiculo_ficha/<id>', vehiculo_ficha, name="vehiculo_ficha"),
    path('contacto' ,contacto, name="contacto"),
    path('iniciosesion' ,iniciosesion, name= "iniciosesion"),
    path('nosotros',nosotros, name="nosotros"),
    path('pag_caja', pag_caja, name="pag_caja"),
    path('pag_electri', pag_electri, name="pag_electri"),
    path('pag_suspe', pag_suspe, name="pag_suspe"),
    path('registro', registro, name="registro"),
    path('index', index, name="index"),

]
