from django import forms

class UserCreateForm(forms.Form):
   name =forms.CharField(label="Name", max_length=100, required=True)
   email=forms.EmailField(label="Email",max_length=100,required=True)
   password=forms.CharField(label='Password',max_length=100,required=True ,min_length=6)