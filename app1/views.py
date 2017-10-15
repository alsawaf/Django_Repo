from django.shortcuts import render
from app1.models import user
from app1 import forms
from app1.forms import RegisterUserForm

# Create your views here.



def index(request):
    return render(request,'app1/MainHomePage.html')


def users(request):
    Users_Dict = {"Users_Dict" : user.objects.order_by('First_Name')}
    return render(request,'app1/users.html',context=Users_Dict)


def RegisterUser(request):

    RegisterFrom = RegisterUserForm()
    if request.method == 'POST' : #checks if the post requset was sent " means the user succssesfully presses submit "
        RegisterFrom = RegisterUserForm(request.POST) #we are passing the requset to this form object so it now contains the data


        if RegisterFrom.is_valid():
            RegisterFrom.save(commit=True) # commit means commit this to the database
            return index(request) # this calls the index func from views.py so it moves us back to the home page


        else:
            print("Error !!")


    return render(request,'app1/Form.html',{'RegisterFrom':RegisterFrom})








def form(request):
    form = forms.BasicFrom()

    if request.method == 'POST': #check if the post request was sent " submit button clicked "
        form = forms.BasicFrom(request.POST)# passing that request with its data to the form object

        if form.is_valid(): #checking if the form submition is vaild
            print("Name : " + form.cleaned_data ['Name'])
# accessing data within the form object with variable name we made in the class such as Name , Email , etc
            print("Email : " + form.cleaned_data['Email'])
            print("Text : " + form.cleaned_data['Text'])

    return render(request,"app1/Form.html",{'form':form})
