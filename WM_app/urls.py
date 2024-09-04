from django.urls import path
from.import views
urlpatterns=[
    path('',views.indexpage),
    path('sign/',views.signuppage,name='sign'),
    path('log/',views.loginpage,name='log'),
    path('degradable/',views.biode,name='degradable'),
    path('logre/',views.requiredindex,name='logre'),
    path('relog/',views.relogin,name='relog'),
    path('logout/',views.logout_view,name='logout'),
    path('nb/',views.nonbiowaste,name='nb'),
    path('hz/',views.hazwaste,name='hz'),
    path('successpage/',views.success,name='successpage'),
]