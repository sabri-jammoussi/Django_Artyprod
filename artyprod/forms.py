from django import forms
from datetime import date
from django.forms import ModelForm
from .models import Projet,Personnel,Service,Equipe,ProjetUtilisateur
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import CheckboxSelectMultiple, ModelForm, ModelMultipleChoiceField

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telephone = forms.DecimalField(label='tel',max_digits=8,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name', 'last_name' , 'email','password1','password2')
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
class PersonnelForm(ModelForm):
    class Meta : 
        model=Personnel
        fields = "__all__"      
class ProjetForm(ModelForm):
    class Meta : 
        model = Projet
        fields = "__all__" 
class ServiceForm(ModelForm):
    class Meta : 
        model = Service
        fields = "__all__" 
class EquipeForm(ModelForm):
    personnels = ModelMultipleChoiceField(queryset=Personnel.objects.all(), widget=CheckboxSelectMultiple)
    
    class Meta : 
        model = Equipe
        fields = "__all__" 
class ProjetUtilisateurForm(forms.ModelForm):
    projet = forms.ModelMultipleChoiceField(queryset=Projet.objects.filter(date_debut=date.today()), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = ProjetUtilisateur

        fields = "__all__"
        