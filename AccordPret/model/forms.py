from django import forms
etats = [('IN', 'IN'),('CT', 'CT'),('FL', 'FL'),('NC', 'NC'),('IL', 'IL'),('OK', 'OK'),('AR', 'AR'),('MN', 'MN'),('CA', 'CA'),('SC', 'SC'),('TX', 'TX'),('LA', 'LA'),('IA', 'IA'),('TN', 'TN'),('MS', 'MS'),('OH', 'OH'),('MD', 'MD'),('VA', 'VA'),('MA', 'MA'),('PA', 'PA'),('OR', 'OR'),('ME', 'ME'),('KS', 'KS'),('MI', 'MI'),('AK', 'AK'),('WA', 'WA'),('CO', 'CO'),('WY', 'WY'),('UT', 'UT'),('MO', 'MO'),('AZ', 'AZ'),('ID', 'ID'),('RI', 'RI'),('NJ', 'NJ'),('NH', 'NH'),('NM', 'NM'),('NV', 'NV'),('NY', 'NY'),('ND', 'ND'),('VT', 'VT'),('WI', 'WI'),('MT', 'MT'),('AL', 'AL'),('GA', 'GA'),('KY', 'KY'),('NE', 'NE'),('WV', 'WV'),('SD', 'SD'),('DE', 'DE'),('DC', 'DC'),('HI', 'HI')]

class ModelForm(forms.Form):
    Name = forms.CharField(label="Nom de votre entreprise")
    City = forms.CharField(label="Ville")
    Zip = forms.IntegerField(label="Code Postal", min_value=10000, max_value=99999)
    State = forms.CharField(label="Etat", widget=forms.Select(choices=etats))
    NoEmp = forms.IntegerField(label="Nombre d'employés", min_value=1, max_value=9999)
    FranchiseCode = forms.BooleanField(label="Franchisé ?")
    NAICS = forms.IntegerField(label="Code NAICS (Laisser vide si vous n'en avez pas)")
    year_create = forms.IntegerField(label="Année de création")
    UrbanRural = forms.CharField(label="Zone Rurale ou Urbaine")

    # Objectifs
    CreateJob = forms.IntegerField(label="Nombre de poste créés", min_value=1, max_value=5621)
    RetainedJob = forms.IntegerField(label="Nombre de poste sauvegardés", min_value=1, max_value=9500)

    # Infos crédit
    Bank = forms.CharField(label="Nom de votre banque")
    BankState = forms.CharField(label="Etat", widget=forms.Select(choices=etats))

    LowDoc = forms.BooleanField(label="Suivez vous le programme 'LowDoc' ?")
    RevLineCr = forms.BooleanField(label="Crédit renouvelable")
    Term = forms.IntegerField(label="Nombre d'échéances en mois", min_value=1, max_value=569)
    GrAppv = forms.IntegerField(label="Montant accordé par la banque", min_value=1000, max_value=5472000)
    in_recession =forms.BooleanField(label="En recession ?")