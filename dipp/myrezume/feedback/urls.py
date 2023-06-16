from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedbacks, name ='feedback'),
    # path('<int:feed_id/>', views.detail, name='detail'),

]