from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Detail(models.Model):
    fichier=models.FileField(upload_to='uploads/',max_length=255,default=None)#mediRoot

#Class service 
class Service(models.Model):
    types=[
        ('Design Graphique','DG'),
        ('Production Audiovisuelle','PA'),
        ('Conception 3D','C3D')
    ]   
    description=models.CharField(max_length=255,default=None)
    type=models.CharField(max_length=255,choices=types,default='dg')
    details=models.ForeignKey(Detail,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return "\nType : "+self.type+"\n"



#class Personnel
class Personnel(models.Model):
    nom=models.CharField(max_length=255,default=None)
    fichier_CV=models.FileField(upload_to='uploads/',max_length=255,default=None)
    fichier_photo=models.ImageField(upload_to='media/',max_length=255,default=None)
    lien_linkedln=models.CharField(max_length=255,default=None)
    def __str__(self):
        return "\nNom : "+self.nom+" Lien Linkedln : "+self.lien_linkedln


#Class Equipe
class Equipe(models.Model):
    #tableau des personnels !
    nom = models.CharField(max_length=255,null=True)
    personnels=models.ManyToManyField(Personnel)
    def __str__(self):
          personnel_list = ",".join(personnel.nom for personnel in self.personnels.all())
          return f"Equipe {str(self.id)} : ({personnel_list})"


#class Projet
class Projet(models.Model):
    acheve=[
        ('Achevé','oui'),
        ('Non achevé','non')
    ]
    libelle=models.CharField(max_length=255,default=None)
    photo=models.ImageField(upload_to='media/',max_length=255,default=None)
    description=models.CharField(max_length=255,default=None)
    date_debut=models.DateField(default=None)
    date_fin=models.DateField(default=None)
    acheve=models.CharField(max_length=255, choices=acheve,default='non')
    services=models.ForeignKey(Service,on_delete=models.CASCADE,default=None)
    equipe=models.OneToOneField(Equipe,on_delete=models.CASCADE,default=None)
    
    
    def __str__(self):
        return "\nLibelle : "+self.libelle+" DateFin : "+str(self.date_fin)+" Achevee : "+str(self.acheve)
class ProjetUtilisateur(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    projet = models.ManyToManyField(Projet)

    def __str__(self):
        return " "+self.libellai+" "+str(self.date_fin)+" "+str(self.utilisateur.username)
