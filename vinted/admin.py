'''
Created on Jul 31, 2020

@author: groupe5
'''
from django.contrib import admin
from vinted.models import User,Annonce,Banword,Enchere,Block

admin.site.register(User)
admin.site.register(Annonce)
admin.site.register(Banword)
admin.site.register(Enchere)
admin.site.register(Block)
