from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views import View

from .models import (
    Drug,
)
from .forms import (
    DrugForm,
)
# Create your views here.
# Supplier views
# @login_required(login_url='login')
def add_drug(request):
    forms = DrugForm()
    if request.method == 'POST':
        forms = DrugForm(request.POST)
        if forms.is_valid():
            drug_id = forms.cleaned_data['drug_id']
            name = forms.cleaned_data['name']
            drug_type = forms.cleaned_data['drug_type']
            amount = forms.cleaned_data['amount']
            exp = forms.cleaned_data['exp']
            mfg = forms.cleaned_data['mfg']
            brand = forms.cleaned_data['brand']
            description = forms.cleaned_data['description']
            updated_date = forms.cleaned_data['updated_date']
            Drug.objects.create(drug_id=drug_id, name=name, 
                                drug_type=drug_type, amount=amount, exp=exp, mfg=mfg, brand=brand, description=description, updated_date=updated_date
                                )
            return redirect('drug-list')
    context = {
        'form': forms
    }
    return render(request, 'drugs/add_drug.html', context)    


def destroy(request, drug_id):  
    drug = get_object_or_404(Drug, drug_id=drug_id)
    drug.delete()
    return redirect("/")
def edit(request, drug_id):  
    drug = get_object_or_404(Drug, drug_id=drug_id)
    forms = DrugForm()
    context = {
        'form': forms
    }
    return render(request, 'drugs/edit_drug.html', context)
# @require_POST
# def destroy(request, drug_id):
#     d = get_object_or_404(Drug, drug_id=drug_id)
#     d.delete()
#     return redirect('/')
# def destroy(request, drug_id):  
#     Drug.objects.get(drug_id=drug_id).delete()
#     return redirect("/")
# def destroy(request, drug_id):  
#     d = Drug.objects.get(drug_id=drug_id)  
#     d.delete()  
#     return redirect("/")     


class DrugListView(ListView):
    model = Drug
    template_name = 'drugs/drug_list.html'
    context_object_name = 'drug'
    # def delete(self, request, pk, action=None):
    #     drug_data = self.get_object(pk)
    #     drug_data.delete()

    #     redirect_url = None
    #     if action == 'single':
    #         messages.success(request, 'Item deleted successfully')
    #         redirect_url = reverse('drug-list')

        # response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
        # return JsonResponse(response)
    
    
