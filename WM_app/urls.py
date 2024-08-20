from django.urls import path
from.import views
urlpatterns=[
    path('',views.indexpage),
    path('sign/',views.signuppage,name='sign'),
    path('log/',views.loginpage,name='log'),
    # path('sign/',views.signuppage,name='sign'),
]