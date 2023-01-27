from django.shortcuts import render
from . import forms
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
            data = json.dumps(form.data)
            reponse = requests.post(url,data=data)
            info = reponse.text
            print(info,data)
            return render(request, 'model.html', context={'form' : form, 'info' : info})

    else:
        form = forms.ModelForm()
    return render(request, 'model.html', {'form': form})