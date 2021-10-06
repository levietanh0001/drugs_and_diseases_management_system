from django.urls import path, re_path
from .views import (
    DrugListView, 
    add_drug,
    destroy   
)

urlpatterns = [
    path('add-drug/', add_drug, name='add-drug'),
    path('drug-list/', DrugListView.as_view(), name='drug-list'),
    path('delete/<str:drug_id>/', destroy), 
]