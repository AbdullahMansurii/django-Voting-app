from django.urls import path
from . import views

# URL namespace for polls app
app_name = 'polls'

urlpatterns = [
    # Main page - shows all polls
    path('', views.index, name='index'),
    # Vote page - form to vote on a poll
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    # Results page - shows poll results
    path('<int:poll_id>/results/', views.results, name='results'),
]


