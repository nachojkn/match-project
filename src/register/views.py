from django.shortcuts import render, HttpResponse
from register import varyfun


def register(request):
 
    return HttpResponse(varyfun.navBar+varyfun.var1+varyfun.SaltoLinea+varyfun.var1)



