from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.vista_panel_sustentabilidad,
        name="inicio",
    ),
    path(
        "sustentabilidad/",
        views.vista_panel_sustentabilidad,
        name="panel_sustentabilidad"
    ),
]