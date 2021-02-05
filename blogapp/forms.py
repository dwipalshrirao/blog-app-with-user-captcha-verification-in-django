from django import forms 
  
# import GeeksModel from models.py 
from .models import blog 
  
# create a ModelForm 
class blogForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = blog 
        # fields = "__all__"
        exclude = ('author',)