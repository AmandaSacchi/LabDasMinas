from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('cadastro/', views.fazer_cadastro),
    path('sobre/', views.sobre),
    path('cadastrados/', views.cadastrados),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
