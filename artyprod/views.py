from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.template import loader
from .forms import UserRegistrationForm
from .models import Projet,Personnel,Service,Equipe
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth import login, authenticate
from .forms import PersonnelForm,ProjetForm,ServiceForm,EquipeForm,ProjetUtilisateur,ProjetUtilisateurForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.core.mail import send_mail

def projet(request):
    projet= Projet.objects.all()
    context={'projet':projet}
    return render( request,'projet/listProjet.html',context )

def listservice(request):
    service= Service.objects.all()
    context={'service':service}
    return render( request,'service/listService.html',context )


def personnel(request):
    personel= Personnel.objects.all()
    context={'personel':personel}
    return render( request,'personnel/listpersonnel.html',context )
def listequipe(request):
    equipe= Equipe.objects.all()
    context={'equipe':equipe}
    return render( request,'equipe/listEquipe.html',context )
def register(request):
     if request.method == 'POST' :
          form = UserRegistrationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password1')
               user = authenticate(username=username, password=password)
               login(request,user)
               messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
               return redirect('login')
     else :
          form = UserRegistrationForm()
     return render(request,'registration/register.html',{'form' : form})
############### CRUD personnel ##################
def ADD_personnel(request):
     if request.method == "POST" :
          form = PersonnelForm(request.POST,request.FILES)
          if form.is_valid():
               form.save()
               return redirect('personnel')
     else :
         form = PersonnelForm() #créer formulaire vide
         personnel=Personnel.objects.all()
     return render(request,'personnel/ajouterPersonnel.html',{'personnel':personnel , 'form':form})
def delete_post(request, id):
    post = get_object_or_404(Personnel, pk=id)
    context = {'post': post}    
    
    if request.method == 'GET':
        return render(request, 'personnel/confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('personnel')
def edit_post(request, id):
    post = get_object_or_404(Personnel, id=id)

    if request.method == 'GET':
        context = {'form': PersonnelForm(instance=post), 'id': id}
        return render(request,'personnel/editPersonnel.html',context)
    elif request.method == 'POST':
         form = PersonnelForm(request.POST , request.FILES, instance=post) ## zedt hethi : request.FILES bech walla ybedel el photo 
         if form.is_valid():
              form.save()
              messages.success(request, 'The post has been updated successfully.')
              return redirect('personnel')
         else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'personnel/editPersonnel.html',{'form':form})
class TaskDetail(DetailView):
    model = Personnel
    context_object_name = 'personnel'
    template_name ='personnel_detail.html'
    ############### CRUD projet ##################
def ADD_Projet(request):
     if request.method == "POST" :
          form = ProjetForm(request.POST,request.FILES)
          if form.is_valid():
               form.save()
               return redirect('home')
     else :
          form = ProjetForm() #créer formulaire vide
     Produits=Projet.objects.all()
     return render(request,'projet/ajouterProjet.html',{'Produits':Produits , 'form':form})
def delete_projet(request, id):
    post = get_object_or_404(Projet, pk=id)
    context = {'post': post}    
    
    if request.method == 'GET':
        return render(request, 'projet/confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('home')
def edit_projet(request, id):
    post = get_object_or_404(Projet, id=id)

    if request.method == 'GET':
        context = {'form': ProjetForm(instance=post), 'id': id}
        return render(request,'projet/editProjet.html',context)
    elif request.method == 'POST':
         form = ProjetForm(request.POST , request.FILES, instance=post) ## zedt hethi : request.FILES bech walla ybedel el photo 
         if form.is_valid():
              form.save()
              messages.success(request, 'The post has been updated successfully.')
              return redirect('home')
         else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'projet/editProjet.html',{'form':form})
def product_det(request,id):
    p = get_object_or_404(Projet, id=id)
    return render(request, 'projet_detail.html', {'projet': p})
    ############### CRUD Service ##################
def ADD_Service(request):
     if request.method == "POST" :
          form = ServiceForm(request.POST,request.FILES)
          if form.is_valid():
               form.save()
               return redirect('listservice')
     else :
          form = ServiceForm() #créer formulaire vide
     Produits=Service.objects.all()
     return render(request,'service/ajouterService.html',{'Produits':Produits , 'form':form})
def delete_service(request, id):
    post = get_object_or_404(Service, pk=id)
    context = {'post': post}    
    
    if request.method == 'GET':
        return render(request, 'service/confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('listservice')
def edit_service(request, id):
    post = get_object_or_404(Service, id=id)

    if request.method == 'GET':
        context = {'form': ServiceForm(instance=post), 'id': id}
        return render(request,'service/editService.html',context)
    elif request.method == 'POST':
         form = ServiceForm(request.POST , request.FILES, instance=post) ## zedt hethi : request.FILES bech walla ybedel el photo 
         if form.is_valid():
              form.save()
              messages.success(request, 'The post has been updated successfully.')
              return redirect('listservice')
         else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'service/editService.html',{'form':form})
def service_det(request,id):
    p = get_object_or_404(Service, id=id)
    return render(request, 'service_detail.html', {'service': p})
############# contact ############
def send_email(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		send_mail(
			subject,
			'Contact from ' + name + ' (' + email + ')\n\n' + message,
			email,
			['sabrijm123@gmail.com'],
			fail_silently=False,
		)
		return render(request,'contact/contact_form.html',{'name':name})
	return render(request, 'contact/contact_form.html')
def contact(request):
     return render(request,'contact/contact_form.html')
   ############### CRUD Equipe ##################
def ADD_Equipe(request):
     if request.method == "POST" :
          form = EquipeForm(request.POST,request.FILES)
          if form.is_valid():
               form.save()
               return redirect('listequipe')
     else :
          form = EquipeForm()#créer formulaire vide
     Produits=Equipe.objects.all()
     return render(request,'equipe/ajouterEquipe.html',{'Produits':Produits , 'form':form})
def delete_Equipe(request, id):
    post = get_object_or_404(Equipe, pk=id)
    context = {'post': post}    
    
    if request.method == 'GET':
        return render(request, 'equipe/confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('listequipe')
def edit_equipe(request, id):
    post = get_object_or_404(Equipe, id=id)

    if request.method == 'GET':
        context = {'form': EquipeForm(instance=post), 'id': id}
        return render(request,'equipe/editEquipe.html',context)
    elif request.method == 'POST':
         form = EquipeForm(request.POST , request.FILES, instance=post) ## zedt hethi : request.FILES bech walla ybedel el photo 
         if form.is_valid():
              form.save()
              messages.success(request, 'The post has been updated successfully.')
              return redirect('listequipe')
         else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'service/editService.html',{'form':form})
def equipe_det(request,id):
    p = get_object_or_404(Equipe, id=id)
    return render(request, 'equipe_detail.html', {'equipe': p})
##### acheve ####
def projets_acheves(request):
    projets = Projet.objects.filter(acheve='Achevé')
    return render(request, 'portfolio/Portfolio.html', {'projets': projets})

def projets_non_acheves(request):
    projets = Projet.objects.filter(acheve='Non achevé')
    return render(request, 'portfolio/Portfolio_non_acheves.html', {'projets': projets})
###########demande projet ##############
def projet_utilisateur_list(request):
    projetutilisateurs = ProjetUtilisateur.objects.filter(utilisateur=request.user)
    context = {'projetutilisateurs': projetutilisateurs}
    return render(request, 'projet_utilisateur/projet_utilisateur_list.html', context)
def ajouter_projet_utilisateur(request):
    if request.method == 'POST':
        form = ProjetUtilisateurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projet')
    else:
        form = ProjetUtilisateurForm()
    return render(request, 'projet_utilisateur/ajouter_projet_utilisateur.html', {'form': form})
