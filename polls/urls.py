from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('loanform/', views.LoanFormView.as_view(), name='loanform'),
    path('decision/', views.DecisionView.as_view(), name='decision'),
    path('getLoan/', views.getLoan, name='getLoan'),
  #  path('answer/', views.answer, name='answer'),
]

#from django.urls import path

#from . import views

#urlpatterns = [
    # ex: /polls/
   # path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
   # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
   # path('<int:question_id>/vote/', views.vote, name='vote'),
#]