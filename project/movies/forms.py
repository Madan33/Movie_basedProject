from django import forms
from .models import Movieinfo,Actor,Awards,Director

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movieinfo
        fields = ['title', 'Actor_name','description', 'year', 'image','release_date','Awards','budget','total_collections','review']

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['industry', 'hero', 'awards', 'img', 'dob', 'bio']
        widgets = {
            'awards': forms.CheckboxSelectMultiple,  
        }


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name' ,'title', 'hit_or_flop']


class AwardsForm(forms.ModelForm):
    class Meta:
        model = Awards
        fields = ['Award']