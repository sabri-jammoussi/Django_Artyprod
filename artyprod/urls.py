from django.urls import path,include,URLPattern
from .views import TaskDetail,product_det,service_det
from . import views
from django.contrib.auth.views import ( 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
urlpatterns = [	
    path('', views.projet,name='home'),
    path('projet/',views.projet,name="projet"),
    path('service/',views.listservice,name="listservice"),
    path('equipe/',views.listequipe,name="listequipe"),
    path('personnel/',views.personnel,name="personnel"),
    path('register/',views.register, name = 'register'), 
    ########## contact us ###########################
    path('contact/', views.contact, name='cont'),
    path('send/', views.send_email, name='contact_form'), 
    ##########CRUD Personnel##########################
    path('ADD_personnel/',views.ADD_personnel,name='ADD_personnel'),
    path('Personnel/delete/<int:id>/', views.delete_post, name='deletePersonnel'),
    path('Personnel/edit/<int:id>/', views.edit_post, name='editPersonnel'),
    path('Personnel/detail/<int:pk>/',TaskDetail.as_view(),name='detail'),
     ##########CRUD projet##########################
    path('ADD_projet/',views.ADD_Projet,name='addprojet'),
    path('projet/delete/<int:id>/', views.delete_projet, name='deleteProjet'),
    path('Projet/edit/<int:id>/', views.edit_projet, name='editProjet'),
    path('Projet/detail/<id>/',views.product_det,name='detail_projet'),
     ##########CRUD equipe##########################
    path('ADD_equipe/',views.ADD_Equipe,name='add_equipe'),
    path('equipe/delete/<int:id>/', views.delete_Equipe, name='deleteEquipe'),
    path('equipe/edit/<int:id>/', views.edit_equipe, name='editEquipe'),
    path('equipe/detail/<id>/',views.equipe_det,name='detail_equipe'),
     ##########CRUD Service##########################
    path('ADD_service/',views.ADD_Service,name='addservice'),
    path('service/delete/<int:id>/', views.delete_service, name='deleteService'),
    path('service/edit/<int:id>/', views.edit_service, name='editService'),
    path('service/detail/<id>/',views.service_det,name='detail_Service'),
    ###########acheve####################
    path('projets-non-acheves/', views.projets_non_acheves,name='Projets_non_acheves'),
    path('projets-achevé', views.projets_acheves, name='achevé'),
    ######### demande projet #############
    path('projets/', views.projet_utilisateur_list, name='projet_utilisateurlist'),
    path('projetsajouter/', views.ajouter_projet_utilisateur, name='ajouterprojetutilisateur'),
    ##########Reset Password ##########################
    path('password-reset/', PasswordResetView.as_view(template_name='password/password_reset.html',html_email_template_name='password/password_reset_email.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'),name='password_reset_complete'),
    ]
