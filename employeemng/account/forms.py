from django import forms
from .models import Department,Manager

class Regform(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()
    experience=forms.IntegerField()
    def clean(self):
        cleaned_data=super().clean()
        ex=cleaned_data.get('experience')
        if ex<0:
            msg="experienceb Invalid"
            self.add_error('experience',msg)



class DepForm(forms.ModelForm):
    class Meta:
        model=Department
        fields="__all__"
        widgets={ 
            'Deptno':forms.TextInput(attrs={'placeholder':'Enter Department Number','class':'form-control'}),
            'Deptname':forms.TextInput(attrs={'placeholder':'Enter Department Name','class':'form-control'}),            
            'Deptdescription':forms.TextInput(attrs={'placeholder':'Enter Department Description','class':'form-control'}),
        }



class ManageForm(forms.ModelForm):
    class Meta:
        model=Manager
        fields="__all__"        