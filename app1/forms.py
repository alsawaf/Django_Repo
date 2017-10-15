from django import forms
from app1.models import user

#this is a file to create the forms classes just as we did with models
#
# class BasicFrom(forms.Form):
#
#     Name = forms.CharField() # creating attribute will automatically generate the html for it
#     Email = forms.EmailField()
#     Text = forms.CharField(widget=forms.Textarea)



class RegisterUserForm(forms.ModelForm):
    class Meta():
        model = user
        fields = '__all__'   #this means all fields or you can include or exculde whatever fields you want
