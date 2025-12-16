from django import forms
from .models import Student

class StudentRegistration (forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        
        # widgets we use to pass extra info to form, i.e to add class to field, add validation to field etc
        widgets = { 
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={ 'class':'form-control'}), #render_value=True will fill value in password filled, otherwise it will show blank all the time
        }