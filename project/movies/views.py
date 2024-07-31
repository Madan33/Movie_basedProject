from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Movieinfo,Actor,Indistry,Awards,Director,Genre
from .forms import MovieForm,ActorForm,DirectorForm,AwardsForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, Page
from django.views.generic import TemplateView
from .serializers import MovieinfoSerializer
from django.urls import reverse_lazy
from rest_framework import generics


def index(request):
     return render(request, 'index.html')

@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user  
            movie.save()
            return redirect('list')
    else:
        form = MovieForm()
    return render(request, 'create.html', {'form': form})

@login_required(login_url='login')
def list(request):
    query = request.GET.get('q')
    movies = Movieinfo.objects.filter(user=request.user)
    
    if query:
        movies = movies.filter(title__icontains=query)
    
    # Pagination
    paginator = Paginator(movies, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'list.html', {'movies': page_obj})

@login_required
def edit(request, pk):
    movie = get_object_or_404(Movieinfo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit.html', {'form': form})

@login_required
def delete(request, pk):
    movie = get_object_or_404(Movieinfo, pk=pk, user=request.user)
    if request.method == 'POST':
        movie.delete()
        return redirect('list')
    return render(request, 'delete.html', {'movie': movie})

#About Hero

def hero_list(request):
    hero_list = Actor.objects.all()
    
    # Pagination
    paginator = Paginator(hero_list, 4)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'hero_list': page_obj,
    }
    return render(request, 'hero/hero_list.html', context)



def hero_detail(request, pk):
    hero = get_object_or_404(Actor, pk=pk)
    industry = hero.industry
    awards = hero.awards.all()

    context = {
        'hero': hero,
        'industry': industry,
        'awards': awards,
    }

    return render(request, 'hero/hero_details.html', context)

def add_actor(request):
    if request.method == 'POST':
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hero_list')  
    else:
        form = ActorForm()
    return render(request, 'hero/curd/add_actor.html', {'form': form})

def edit_actor(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    if request.method == 'POST':
        form = ActorForm(request.POST, request.FILES, instance=actor)
        if form.is_valid():
            form.save()
            return redirect('hero_detail', pk=pk)  
    else:
        form = ActorForm(instance=actor)
    return render(request, 'hero/curd/edit_actor.html', {'form': form})

def delete_actor(request, pk):
    try:
        actor = get_object_or_404(Actor, pk=pk)
        return redirect(reverse('heros_detail', kwargs={'pk': actor.pk}))
    except ValueError:
        return redirect('hero_list')


#About Industury

def industry_list(request):
    industries = Indistry.objects.all()
    return render(request, 'industry/industry_list.html', {'industries': industries})


def industry_heroes(request, pk):
    industry = get_object_or_404(Indistry, pk=pk)  
    heroes = Actor.objects.filter(industry=industry)  

    awards = []  
    for hero in heroes:
        awards.extend(hero.awards.all())  
    
    context = {
        'industry': industry,
        'heroes': heroes,
        'awards': awards,  
    }
    return render(request, 'industry/industry_heros.html', context)


#About Awards

def award_list(request):
    awards = Awards.objects.all()
    context = {
        'awards': awards
    }
    return render(request, 'awards/award_list.html', context)


def award_detail(request, pk):
    award = get_object_or_404(Awards, pk=pk)
    actors = award.actors.all()  
    context = {
        'award': award,
        'actors': actors
    }
    return render(request, 'awards/award_detail.html', context)

def award_create(request):
    if request.method == 'POST':
        form = AwardsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('award-list')  
    else:
        form = AwardsForm()
    return render(request, 'awards/award_form.html', {'form': form})


def award_update(request, pk):
    award = get_object_or_404(Awards, pk=pk)
    if request.method == 'POST':
        form = AwardsForm(request.POST, instance=award)
        if form.is_valid():
            form.save()
            return redirect('award-list')  
    else:
        form = AwardsForm(instance=award)
    return render(request, 'awards/award_form.html', {'form': form})


def award_delete(request, pk):
    award = get_object_or_404(Awards, pk=pk)
    if request.method == 'POST':
        award.delete()
        return redirect('award-list')  
    return render(request, 'awards/award_confirm_delete.html', {'award': award})



#Director

def director_list(request):
    directors = Director.objects.all()
    return render(request, 'director/director_list.html', {'directors': directors})

def director_detail(request, pk):
    director = get_object_or_404(Director, pk=pk)
    actors = Actor.objects.all()  
    return render(request, 'director/director_detail.html', {'director': director, 'actors': actors})

def director_create(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('director-list') 
    else:
        form = DirectorForm()
    return render(request, 'director/director_form.html', {'form': form})

def director_update(request, pk):
    director = get_object_or_404(Director, pk=pk)
    if request.method == 'POST':
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            return redirect('director-detail', pk=pk)  
    else:
        form = DirectorForm(instance=director)
    return render(request, 'director/director_form.html', {'form': form})


def director_delete(request, pk):
    director = get_object_or_404(Director, pk=pk)
    if request.method == 'POST':
        director.delete()
        return redirect('director-list')  
    return render(request, 'director/director_confirm_delete.html', {'director': director})


#About django restframework

class AllDetailView(TemplateView):
    template_name = 'all_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movieinfo.objects.all()
        context['directors'] = Director.objects.all()
        context['awards'] = Awards.objects.all()
        return context
    
