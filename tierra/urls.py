
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from tierra import urls as tierra_urls_module
from .views import inicio, tijeras, cultivador, plantador, azadilla, pala, rastrillo, manguera_alta_presion, manguera_aspersion, manguera_expandible, manguera_subterraneo, Manguera_estandar, manguera_goteo, tierra_enriquecida, tierra_maceteros, tierra_normal, tierra_tamizada, tierra_macetero_tamizada, tierra_acida, rosas, lavanda, helecho, macetero_mimbre, terracota, plastico, colgante, autorriego, ceramica, petunias, lirio, geranios, laurel, rosa, login, tienda, nosotros, contacto, registro, carrito, recuperar_contrasena, arbustos, libutrina, plantas, maceteros, tierra_hoja, mangueras, herramientas, boj, Forsythia, arbusto_mariposa, productos_arbustos, productos_plantas, productos_maceteros, productos_tierra, productos_mangueras, productos_herramientas


urlpatterns = [

    path('productos/arbustos/', productos_arbustos, name='productos_arbustos'),
    path('productos/plantas/', productos_plantas, name='productos_plantas'),
    path('productos/maceteros/', productos_maceteros, name='productos_maceteros'),
    path('productos/tierra/', productos_tierra, name='productos_tierra'),
    path('productos/mangueras/', productos_mangueras, name='productos_mangueras'),
    path('productos/herramientas/', productos_herramientas, name='productos_herramientas'),

    path('tijeras/',tijeras,name="tijeras"),
    path('cultivador/',cultivador,name="cultivador"),
    path('plantador/',plantador,name="plantador"),
    path('azadilla/',azadilla,name="azadilla"),
    path('pala/',pala,name="pala"),
    path('rastrillo/',rastrillo,name="rastrillo"),


    path('manguera_alta_presion/',manguera_alta_presion,name="manguera_alta_presion"),
    path('manguera_aspersion/',manguera_aspersion,name="manguera_aspersion"),
    path('manguera_expandible/',manguera_expandible,name="manguera_expandible"),
    path('manguera_subterraneo/',manguera_subterraneo,name="manguera_subterraneo"),
    path('Manguera_estandar/',Manguera_estandar,name="Manguera_estandar"),
    path('manguera_goteo/',manguera_goteo,name="manguera_goteo"),
 

    path('',inicio,name="inicio"),
    path('login/',login,name="login"),
    path('tienda/',tienda,name="tienda"),
    path('nosotros/',nosotros,name="nosotros"),
    path('contacto/',contacto,name="contacto"),
    path('registro/',registro,name="resgistro"),
    path('carrito/',carrito,name="carrito"),
    path('recuperar_contrasena/', recuperar_contrasena, name="recuperar_contrasena"),
    path('arbustos/',arbustos,name="arbustos"),
    path('libutrina/',libutrina,name="libutrina"),
    path('plantas/',plantas,name="plantas"),
    path('maceteros/',maceteros,name="maceteros"),


    path('tierra_hoja/',tierra_hoja,name="tierra_hoja"),
    path('mangueras/',mangueras,name="mangueras"),
    path('herramientas/',herramientas,name="herramientas"),
    path('boj/',boj,name="boj"),
    path('Forsythia/',Forsythia,name="Forsythia"),
    path('arbusto_mariposa/',arbusto_mariposa,name="arbusto_mariposa"),
    path('laurel/',laurel,name="laurel"),
    path('rosa/',rosa,name="rosa"),
    path('rosas/',rosas,name="rosas"),


    path('lavanda/',lavanda,name="lavanda"),
    path('lirio/',lirio,name="lirio"),
    path('helecho/',helecho,name="helecho"),
    path('geranios/',geranios,name="geranios"),
    path('macetero_mimbre/',macetero_mimbre,name="macetero_mimbre"),
    path('terracota/',terracota,name="terracota"),
    path('plastico/',plastico,name="plastico"),
    path('colgante/',colgante,name="colgante"),
    path('autorriego/',autorriego,name="autorriego"),

    path('ceramica/',ceramica,name="ceramica"),
    path('petunias/',petunias,name="petunias"),
    path('tierra_acida/',tierra_acida,name="tierra_acida"),
    path('tierra_macetero_tamizada/',tierra_macetero_tamizada,name="tierra_macetero_tamizada"),
    path('tierra_enriquecida/',tierra_enriquecida,name="tierra_enriquecida"),
    path('tierra_maceteros/',tierra_maceteros,name="tierra_maceteros"),
    path('tierra_normal/',tierra_normal,name="tierra_normal"),  
    path('tierra_tamizada/',tierra_tamizada,name="tierra_tamizada"),   



]

urlpatterns += [
    path('admin/', admin.site.urls),
]

path('', include(tierra_urls_module)),


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)