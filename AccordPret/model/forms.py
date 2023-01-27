from django import forms

etats = [('IN', 'IN'),('CT', 'CT'),('FL', 'FL'),('NC', 'NC'),('IL', 'IL'),('OK', 'OK'),('AR', 'AR'),('MN', 'MN'),('CA', 'CA'),('SC', 'SC'),('TX', 'TX'),('LA', 'LA'),('IA', 'IA'),('TN', 'TN'),('MS', 'MS'),('OH', 'OH'),('MD', 'MD'),('VA', 'VA'),('MA', 'MA'),('PA', 'PA'),('OR', 'OR'),('ME', 'ME'),('KS', 'KS'),('MI', 'MI'),('AK', 'AK'),('WA', 'WA'),('CO', 'CO'),('WY', 'WY'),('UT', 'UT'),('MO', 'MO'),('AZ', 'AZ'),('ID', 'ID'),('RI', 'RI'),('NJ', 'NJ'),('NH', 'NH'),('NM', 'NM'),('NV', 'NV'),('NY', 'NY'),('ND', 'ND'),('VT', 'VT'),('WI', 'WI'),('MT', 'MT'),('AL', 'AL'),('GA', 'GA'),('KY', 'KY'),('NE', 'NE'),('WV', 'WV'),('SD', 'SD'),('DE', 'DE'),('DC', 'DC'),('HI', 'HI')]

class ModelForm(forms.Form):
    Name = forms.CharField(label="Nom de votre entreprise",required=False)
    City = forms.CharField(label="Ville",required=False)
    Zip = forms.IntegerField(label="Code Postal", min_value=10000, max_value=99999,required=False)
    State = forms.CharField(label="Etat", widget=forms.Select(choices=etats))
    NoEmp = forms.IntegerField(label="Nombre d'employés", min_value=1, max_value=9999)
    FranchiseCode = forms.CharField(label="Franchisé ?", widget=forms.Select(choices=[(1,"oui"),(0,"non")]))
    NAICS = forms.IntegerField(label="Code NAICS (Laisser vide si vous n'en avez pas)")
    NewExist = forms.CharField(label="A t-elle plus de 2ans ?", widget=forms.Select(choices=[("Existing","oui"),("New","non")]))
    UrbanRural = forms.CharField(label="Zone Rurale ou Urbaine", widget=forms.Select(choices=[("Urban","Urban"),("Rural","Rural"),("Undefined","Undefined")]))
   
   

    # Objectifs
    CreateJob = forms.IntegerField(label="Nombre de poste créés", min_value=1, max_value=5621,required=False)
    RetainedJob = forms.IntegerField(label="Nombre de poste sauvegardés", min_value=1, max_value=9500,required=False)

    # Infos crédit
    Bank = forms.CharField(label="Nom de votre banque",required=False)
    BankState = forms.CharField(label="Etat", widget=forms.Select(choices=etats))

    LowDoc = forms.CharField(label="Suivez vous le programme 'LowDoc' ?", widget=forms.Select(choices=[(1,"oui"),(0,"non")]))
    RevLineCr = forms.CharField(label="Crédit renouvelable", widget=forms.Select(choices=[(1,"oui"),(0,"non")]),required=False)
    Term = forms.IntegerField(label="Nombre d'échéances en mois", min_value=1, max_value=569)
    GrAppv = forms.IntegerField(label="Montant accordé par la banque", min_value=1000, max_value=5472000)
    in_recession = forms.CharField(label="En recession ?", widget=forms.Select(choices=[(1,"oui"),(0,"non")]))