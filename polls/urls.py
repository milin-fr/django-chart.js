from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/get-votes/', views.get_votes, name='get_votes'),
    path('<int:question_id>/chart/', views.chart, name='chart'),
    path('generate-gamers/', views.generate_gamers_in_db, name='generate_gamers_in_db'),
    path('json-gamers/', views.get_gamers_json, name='get_gamers_json'),
    path('raw-chart-gamers/', views.raw_gamer_chart, name='raw_gamer_chart')
]
