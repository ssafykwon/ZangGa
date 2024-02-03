from django.urls import path

from myvidututorial.api.views import initialize_session, create_connection

app_name = 'myvidututorial'
urlpatterns = [
    path('sessions/', initialize_session, name='initialize_session'),
    path('sessions/<str:sessionId>/connections/',
         create_connection, name='create_connection'),
]
