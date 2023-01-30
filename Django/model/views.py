from django.shortcuts import render
from . import forms,functions
import requests
import json

url="https://api-accord-pret.onrender.com/predict/"

def home_view(request):
    if request.method == 'POST':
        form = forms.ModelForm(request.POST)
        
        if form.is_valid():
            data ={
                "State" : form.data["State"],
                "BankState": form.data["BankState"],
                "Term" : form.data["Term"],
                "NoEmp" : form.data["NoEmp"],
                "NewExist" : form.data["NewExist"],
                "UrbanRural" :form.data["UrbanRural"],
                "LowDoc" :  form.data["LowDoc"],
                "GrAppv" : form.data["GrAppv"],
                "have_franchise" : form.data["FranchiseCode"],
                "sector" : functions.get_sector(form.data["NAICS"]),
                "in_recession": form.data["in_recession"]
                }
            data = json.dumps(data)
            reponse = requests.post(url,data=data)
            info = reponse.json()
            
            return render(request, 'index.html', context={'form' : form, 'info' : info["class"], "title" : "Estimateur"})

    else:
        form = forms.ModelForm()
    return render(request, 'index.html', {'form': form})