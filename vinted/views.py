'''
Created on Jul 31, 2020

@author: groupe5
'''
#from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from random import randint
from vinted.models import User, Annonce,Banword,Enchere,Block




def login(request):
    current_datetime = datetime.now()
    b=Block.objects.all()
    if 'email' in request.GET and 'password' in request.GET :
        entered_email=request.GET['email']
        entered_password=request.GET['password']
        if len(User.objects.filter(email=entered_email).filter(password=entered_password))==1:
            if len(b.filter(blocked=User.objects.get(email=entered_email)))==0:
                request.session['email'] = request.GET['email']
                return redirect('/welcome')
            else:
                template_values = {'error': 'Vous avez été bloqué pour abus et corruption.','datetime':current_datetime}
            return render(request, 'login.html', template_values)
        else:
            template_values = {'error': 'Bad login or password.','datetime':current_datetime}
            return render(request, 'login.html', template_values)
    else:
        dico = {'datetime':current_datetime}
        response = render(request,'login.html',dico)
        return response

def logout(request):
    del request.session['email']
    return redirect ('/login')
    
def welcome(request):
    u1=User.objects.get(email=request.session['email'])
    utilisateur_now=u1.firstname
    current_datetime = datetime.now()
    if u1.acheteur==True and u1.admin != True and u1.vendeur != True:
        dico={"mehdi":"mehdi",'datetime':current_datetime,'nom':utilisateur_now}
        return render(request,'welcome.html',dico)
    elif u1.acheteur==True and u1.admin==True and u1.vendeur != True:
        dico={"juju":"juju",'datetime':current_datetime,'nom':utilisateur_now}
        return render(request,'welcome.html',dico)
    elif u1.vendeur==True and u1.admin != True and u1.acheteur!=True:
        dico={"anto":"anto",'nom':utilisateur_now}
        return render(request,'welcome.html',dico)
    elif u1.vendeur==True and u1.admin==True and u1.acheteur!=True:
        dico={"geo":"geo",'datetime':current_datetime,'nom':utilisateur_now}
        return render(request,'welcome.html',dico)
    elif u1.acheteur==True and u1.vendeur==True and u1.admin==True:
        dico={"tout":"tout",'datetime':current_datetime,'nom':utilisateur_now}
        return render(request,'welcome.html',dico)
    else:
        dico={"rien":"rien",'datetime':current_datetime,'nom':utilisateur_now}
        return render(request,'welcome.html',dico)

def registration(request):
    a=User.objects.all()
    if 'email' in request.GET:
        adminmdp="adminoui"
        e=[]
        for u in a:
            e.append(u.email)
        if request.GET['email']not in e:   
            newUser = User(firstname=request.GET['firstname'],
                          lastname=request.GET['lastname'], 
                          email=request.GET['email'], 
                          password=request.GET['password'],
                          gender=request.GET['gender'],
                          acheteur=True,
                          admin = (adminmdp==request.GET['admin']))
            newUser.save()
            return redirect('/login')
        else:
            return render (request,'registration.html',{'error':"l'email rentré existe déjà, appelé le service technique"})
    else: 
        return render(request,'registration.html')
    
def registration_vendeur(request):
    if 'email' in request.GET:
        adminmdp="adminoui"
        achat="oui"
        newUser = User(firstname=request.GET['firstname'],
                      lastname=request.GET['lastname'], 
                      email=request.GET['email'],  
                      password=request.GET['password'],
                      gender=request.GET['gender'],
                      vendeur=True,
                      admin = (adminmdp==request.GET['admin']))
                     #acheteur = (achat==request.GET['acheteur']))
        newUser.save()
        return redirect('/login')
    else:
        return render(request,'registration_vendeur.html')
    
def showannonce(request):
    u1= User.objects.get(email=request.session['email'])
    id=randint(1,100000)
    x=Annonce.objects.filter(createur=u1).filter(etat="D")
    b=Banword.objects.all()
    e=Enchere.objects.all()
    list=[]
    for i in x:
        list.append(i.id_annonce)
    if id in list:
        id=randint(1,100000)
    replacing_word(x,b)
    if u1.vendeur==True or u1.acheteur!=True:
        if 'titre' in request.GET:
            if len(request.GET['titre'])==0 or len(request.GET['descript'])==0 or len(request.GET['prix'])==0:
                p=Annonce.objects.filter(etat="R").filter(createur=u1)
                replacing_word(p,b)
                dico={'post':x,"annonce":p,"enchere":e,'error':"Vous n'avez rien rempli olala"}
                return render(request,'showannonce.html',dico)
            newAnnonce = Annonce(titre=request.GET['titre'],
                                 descript=request.GET['descript'],
                                 prix=request.GET['prix'],
                                 createur=u1,
                                 id_annonce=id)
            newAnnonce.save()
            x=Annonce.objects.filter(createur=u1).filter(etat="D")
            p=Annonce.objects.filter(etat="R").filter(createur=u1)
            replacing_word(x,b)
            replacing_word(p,b)
            dico={'post':x,"succes":"félicitations votre annonce a bien été posté","annonce":p,"enchere":e}
            return render(request,'showannonce.html',dico)
        else:
            p=Annonce.objects.filter(etat="R").filter(createur=u1)
            replacing_word(p,b)
            dico={'post':x,"annonce":p,"enchere":e}
            return render(request,'showannonce.html',dico)    
    else:
        p=Annonce.objects.filter(etat="R").filter(createur=u1)
        replacing_word(x,b)  
        dico={'post':x,"annonce":p,"enchere":e}
        return render(request,'showannonce.html',dico)
    
def showannonce_filtre(request):
    a = Annonce.objects.filter(etat="D")
    b=Banword.objects.all()
    e=Enchere.objects.all()
    dico = {'annonce':a,"mehdi":"mehdi"} #pas utile, oubliez de l'enlever
    replacing_word(a,b)
    if 'descript' in request.GET and len(request.GET['descript'])>0:
        descript_contains=request.GET['descript'] #je tape juste un mot dans le filtre du coup j'ai juste un mot
        list = []  #liste avec les descriptions d'annonce disponible
        for t in a:
            x = t.descript
            list.append(x)
        d= matching_word(descript_contains,list) #j'obtiens une liste d'annonces correspondant au mot
        annonce_filtre = [] #j'aurais ici une liste d'annonce avec leurs objets(prix, id etc)
        for x in d:
            annonce_filtre.append(Annonce.objects.get(descript=x)) #je prends les annonces correspondant à la description filtré
        print(annonce_filtre)
        print(type(request.GET['prix']))
        if 'prix' in request.GET and len(request.GET['prix'])>0:
            annonce_filtre_prix=[]
            for x in annonce_filtre:
                if float(request.GET['prix'])>=x.prix:
                    annonce_filtre_prix.append(x)
            annonce_filtre=annonce_filtre_prix
        dico = {'annonce':annonce_filtre,"juju":"juju"}
        if len(annonce_filtre)==0:      
            dico = {'annonce':annonce_filtre,"juju":"juju","error":"oops,aucune annonce ne correspond à votre recherche"}           
        return render(request,'showannonce_filtre.html',dico)
    elif 'prix' in request.GET and len(request.GET['prix'])>0:
        prix_contains = request.GET['prix']
        if len(prix_contains) !=0:
#             a = a.filter(prix__lt = prix_contains)
            annonce_filtre_prix=[]
            for x in a:
                if float(prix_contains)>=x.prix:
                    annonce_filtre_prix.append(x)
            a=annonce_filtre_prix      
            dico = {'annonce':a,"anto":"anto"}
            if len(a)==0:      
                dico = {'annonce':a,"juju":"juju","error":"oops,aucune annonce ne correspond à votre recherche"}
            return render(request,'showannonce_filtre.html',dico)
    elif 'descript' in request.GET and len(request.GET['descript']) ==0 and 'prix' in request.GET and len(request.GET['prix'])==0:
        dico={'annonce':a,"error":"Veuillez rentrez dans les champs correspondant des valeurs adéquates"}
        return render (request,'showannonce_filtre.html',dico)
        
    else:
        dico={'annonce':a,"anto":"anto"}
        return render (request,'showannonce_filtre.html',dico)

def matching_word(x,list): # pas oublier x est un mot(str), et la liste des descriptions des annonces disponibles
    a = []   
    for t in list:
        if x in t:
            a.append(t)    # j'aurais une liste avec les descriptions qui correspondent au mot        
    return a 
def replacing_word(x,y): #pas oublier x et y sont des objets
    for w in x:
        for word in y:
            if word.wordinit in w.descript: 
                w.descript=w.descript.replace(word.wordinit,word.wordfinal)
            if word.wordinit in w.titre:
                w.titre=w.titre.replace(word.wordinit,word.wordfinal)
        
def reservation(request):
    u1= User.objects.get(email=request.session['email'])
    a=Annonce.objects.all()
    if 'idl' in request.GET:
        if len(request.GET['idl'])!=0:
            id=Annonce.objects.filter(id_annonce=request.GET['idl'])   
            if len(id)==1 and id[0].reservation== None:
                    new_etat="R"
                    #new_reservation=u1
                    current_annonce=Annonce.objects.get(id_annonce=request.GET['idl'])
                    current_annonce.etat=new_etat
                    current_annonce.reservation=u1
                    #current_annonce.reservation=new_reservation
                    current_annonce.save()
                    dico={'j':'j'}
                    e=Enchere.objects.all()
                    if 'enchere'in request.GET and len(request.GET['enchere'])!=0:
                        t=Enchere.objects.filter(produit=current_annonce)
                        if len(t)==0:  #uniquement pour voir si l'annonce a déja une enchère tout court
                            newEnchere=Enchere(encherisseur=u1,
                                               prix_enchere=request.GET['enchere'],
                                               produit=current_annonce,
                                               )
                            newEnchere.save()    
                            return render(request,'reservation.html',dico)
                        else:  #il y a deja plusieurs enchere, et je ne veux pas qu'un encherisseur encherisse deux fois
                            z=[] #on rajoute toutes les encheres que la personne connecté a faite, dans tout les cas y en aura que une 
                            for x in t: #Z egal a 1 ou 0
                                if x.encherisseur==u1:
                                    z.append(x)
                            if len(z)!=0:
                                dico={'error':"oh zebi tu petes les couilles"}
                                return render(request,'reservation.html',dico)
                            else:
                                newEnchere=Enchere(encherisseur=u1,
                                               prix_enchere=request.GET['enchere'],
                                               produit=current_annonce,
                                               )
                                newEnchere.save()
                                return render(request,'reservation.html',dico) 
                    return render(request,'reservation.html',dico)
            else:
                dico={'error':"le numéro rentré ne correspond à aucune annonce, ou sinon l'article est déjà réservé"}
                return render(request,'reservation.html',dico)
        else:
            dico={'error':"Vous n'avez rien rentré petit filou"}
            return render(request,'reservation.html',dico)
    else:
        return render(request,'reservation.html')
    
def showbanword(request):
    u1= User.objects.get(email=request.session['email'])
    c= Banword.objects.all()
    dico={'c':c}
    if 'wordinit' in request.GET:
        newBanword = Banword(wordinit=request.GET['wordinit'],
                             wordfinal=request.GET['wordfinal']
                             )
        newBanword.save()
        return render(request,'showbanword.html',dico)
    else:
        return render(request,'showbanword.html',dico)
    
def showblock(request):
    u1= User.objects.get(email=request.session['email'])
    h=User.objects.all()
    b=Block.objects.all()
#     dico={"user":h,"bloqué":list}
    if 'user' in request.GET:
        newBlock=Block(blockeur=u1,
                       blocked=User.objects.get(firstname=request.GET['user']))
        newBlock.save()
        list=[]
        for x in b:
            list.append(x.blocked)       
        dico={'bloque':"l'utilisateur a bien été bloqué","user":h,"bloqué":list}
        return render(request,'showblock.html',dico)
    else:
        list=[]
        for x in b:
            list.append(x.blocked)
        dico={"user":h,"bloqué":list,"user_connecte":u1}
        return render(request,'showblock.html',dico)

def showhistorique(request):
    u1 = User.objects.get(email=request.session['email'])
    c = Annonce.objects.filter(reservation=u1)
    total=0
    for x in c:
        a=x.prix
        total+=a #total=total+a
    print(total)
    b = Banword.objects.all()
    replacing_word(c,b)
    if len(c)== 0:
        dico={'sorry':"désolé vous n'avez rien réserver :/","juju":"juju","panier":total}
        return render(request,'showhistorique.html',dico)
    else:
        dico={'reserve':c,"panier":total}
        return render(request,'showhistorique.html',dico)
print("300lignes")







