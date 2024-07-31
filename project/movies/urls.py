from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),  
    path('delete/<int:pk>/', views.delete, name='delete'),
    

    
    #About Industry
    path('industries/', views.industry_list, name='industry_list'),
    path('industry/<int:pk>/', views.industry_heroes, name='industry_heroes'),

    #About Awards
    path('awards/', views.award_list, name='award-list'),
    path("awards_detail/<int:pk>/",views.award_detail,name="awards_detail"),
    path('awards/create/', views.award_create, name='award-create'),
    path('awards/<int:pk>/update/', views.award_update, name='award-update'),
    path('awards/<int:pk>/delete/', views.award_delete, name='award-delete'),
  


    #Actor
    path("heros/",views.hero_list,name="heros"),
    path('heros_detail/<int:pk>/',views.hero_detail,name="heros_detail"),
    path('add_actor/', views.add_actor, name='add_actor'),
    path('edit_actor/<int:pk>/', views.edit_actor, name='edit_actor'),
    path('delete_actor/<int:pk>/', views.delete_actor, name='delete_actor'),

    #Director
    path('directors/', views.director_list, name='director-list'),
    path('director/<int:pk>/', views.director_detail, name='director-detail'),
    path('director/create/', views.director_create, name='director-create'),
    path('director/update/<int:pk>/', views.director_update, name='director-update'),
    path('director/delete/<int:pk>/', views.director_delete, name='director-delete'),

    #Django Restframework
    path('all/', views.AllDetailView.as_view(), name='all_detail'),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
