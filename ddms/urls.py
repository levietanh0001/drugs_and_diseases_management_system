from django.contrib import admin
from django.urls import path, include
# local
from .views import base, dashboard
from drugs.views import destroy, edit


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('drugs/', include('drugs.urls')),
    path('edit/<drug_id>/', edit), 
    path('delete/<drug_id>/', destroy), 
]
