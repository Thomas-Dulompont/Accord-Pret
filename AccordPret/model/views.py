from django.shortcuts import render
from . import forms

# Create your views here.
def home_view(request):
    return render(request, "index.html")

def estimator_view(request):
    if request.method == 'POST':
        form = forms.ModelForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = forms.ModelForm()
    return render(request, 'model.html', {'form': form})