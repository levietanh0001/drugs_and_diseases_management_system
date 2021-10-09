from django.contrib import admin
from django.urls import path, include
# local
from .views import base, dashboard
from drugs.views import destroy, edit, update, delete_selected, DrugListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('drug-list/', DrugListView.as_view(), name='drug-list'),
    path('drugs/', include('drugs.urls')),
    path('update/<drug_id>/', update), 
    path('edit/<drug_id>/', edit), 
    path('delete/<drug_id>/', destroy), 
    path('delete_selected/', delete_selected), 
]
