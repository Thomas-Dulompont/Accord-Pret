from django.shortcuts import render
from . import forms,functions
import requests
import json

url="http://127.0.0.1:5000/predict/"
# Create your views here.
def home_view(request):
    return render(request, "index.html")

def estimator_view(request):
    if request.method == 'POST':
        form = forms.ModelForm(request.POST)
        
        if form.is_valid():
            data ={
                "State" : form.data["State"],
                "BankState": form.data["BankState"],
                "Term" : form.data["Term"],
                "NoEmp" : form.data["NoEmp"],
                "NewExist" : functions.is_new(form.data["NewExist"]),
                "UrbanRural" :form.data["UrbanRural"],
                "LowDoc" : functions.correction( form.data["LowDoc"]),
                "GrAppv" : form.data["GrAppv"],
                "have_franchise" : functions.correction(form.data["FranchiseCode"]),
                "sector" : functions.get_sector(form.data["NAICS"]),
                "in_recession": functions.correction(form.data["in_recession"])
                }
            print("\n data : \n",data)
            data = json.dumps(data)
            reponse = requests.post(url,data=data)
            info = reponse.text
            
            return render(request, 'model.html', context={'form' : form, 'info' : info})

    else:
        form = forms.ModelForm()
    return render(request, 'model.html', {'form': form})