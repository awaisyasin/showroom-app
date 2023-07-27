from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'showroom'

urlpatterns = [
    path("", views.ShowRoom, name='showroom'),
    path("brand/<int:brand_id>", views.BrandDetail, name='brand_detail'),
    path("staff", views.Staff, name='staff'),
    path("staff/<int:staff_id>", views.StaffDetail, name='staff_detail'),
    path("brand/<int:brand_id>/model/<int:model_id>", views.ModelDetail, name='model_detail')
]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)