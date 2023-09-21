'''
Created on Jul 31, 2020

@author: groupe5
'''
from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone

class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=128)
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('X','X'),
        )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    acheteur = models.BooleanField(default = False)
    vendeur = models.BooleanField(default = False)
    admin = models.BooleanField (default= False)
    def __str__(self):
        return self.firstname +' '+ self.lastname
    
class Annonce(models.Model):
    titre = models.CharField(max_length=30)
    descript = models.CharField(max_length=1000)
    prix = models.FloatField(default=0,blank=True, null=True)
    id_annonce=models.IntegerField(default=0,blank=True)
    created_at=DateTimeField(default=timezone.now)
    createur = models.ForeignKey("User", blank=True, null=True,on_delete=0)
    #enchere = models.ManyToManyField("Enchere",blank=True,null=True)
    reservation = models.ForeignKey("User",blank=True, null=True,related_name="mehdi")
    ETAT_CHOICES = (
        ("D", "Disponible"),
        ("R", "Réservée"),
        ("V", "Vendu")
        )
    etat=models.CharField(max_length=1, choices=ETAT_CHOICES, default="D")
    def __str__(self):
        return self.titre

class Enchere(models.Model):
    encherisseur = models.ForeignKey("User",blank=True,null=True)
    produit = models.ForeignKey("Annonce",blank=True,null=True)
    date_creation = DateTimeField(default=timezone.now)   
    prix_enchere = models.FloatField(default=0,blank=True,null=True)
    def __str__(self):
        return str(self.prix_enchere)
    
class Banword(models.Model):
    wordinit=models.CharField(max_length=30)
    wordfinal=models.CharField(max_length=30)
    def __str__ (self):
        return self.wordinit + " a changé pour " + self.wordfinal 
    
class Block (models.Model):
    blockeur = models.ForeignKey("User")
    blocked = models.ForeignKey("User",related_name = "blocked") 
    def __str__(self):
        return self.blockeur.firstname + " bloqué " + self.blocked.firstname    


# class Message (models.Model):
#     sender = models.ForeignKey(User,related_name ="sender")
#     reciever = models.ForeignKey(User,related_name = "reciever")
#     message = models.CharField(max_length = 5000)
#     created = models.DateTimeField(auto_now_add = False)

    
    
    
    