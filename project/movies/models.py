from django.db import models
import datetime
from django.contrib.auth.models import User


class Director(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, null=True)
    hit_or_flop = models.CharField(
        max_length=20,
        choices=[
            ('Hit', 'Hit'),
            ('Flop', 'Flop'),
            ('Blockbuster', 'Blockbuster'),
            ('Industry Hit', 'Industry Hit'),
        ],
        default='Hit'  
    )


    def __str__(self):
        return self.name
    
class Genre(models.Model):
    genre = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.genre


class Movieinfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Actor_name=models.CharField(max_length=250,help_text="Name",default=0)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    year = models.IntegerField()
    release_date=models.DateField(default=0)
    Awards=models.CharField(max_length=250,help_text="Awards",default=0)
    image = models.ImageField(upload_to='movies/', blank=True, null=True)
    budget=models.CharField(max_length=100,help_text="Budget",default=0)
    total_collections=models.CharField(max_length=100,help_text="Total Collections",default=0)
    review=models.CharField(max_length=250, help_text="Review",default=0)

    def __str__(self):
        return self.title


class Indistry(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name    


class Awards(models.Model):
    Award = models.CharField(max_length=250, help_text="Awards")

    def __str__(self):
        return self.Award

class Actor(models.Model):
    industry = models.ForeignKey(Indistry, on_delete=models.CASCADE, related_name='actors')
    hero = models.CharField(max_length=250, help_text="Hero's name")
    awards = models.ManyToManyField(Awards, related_name='actors', blank=True)
    img = models.ImageField(upload_to='movies/', blank=True, null=True)
    dob = models.CharField(max_length=100,default=0)
    bio = models.CharField(max_length=1060,default=0)
    def __str__(self):
        return self.hero

