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
    path('payment_page/',views.payment,name='payment_page'),
    path('adm_dash/',views.admindashboard,name='adm_dash'),
    path('pickassign/<str:pickup_id>/',views.pickupassign,name='pickassign'),
    path('wastepick/',views.wastepickup,name='wastepick'),
    path('staff/',views.staffprofile,name='staff'),
    path('add_staff/',views.newstaff,name='add_staff'),
    path('staff_management/',views.deletestaff,name='staff_management'),
    path('edit/',views.staffedit,name='edit'),
    path('prev/',views.oldpickups,name='prev'),
    path('update-status/',views.update_status,name='update_status'),
    path('stafflog/',views.staffsignin,name='stafflog'),
    path('staff_out/',views.staff_logout,name='staff_out'),
    path('assign_pickup/<str:pickup_id>/<int:staff_id>/',views.assign_pickup_to_staff,name='assign_pickup_to_staff'),
    path('confirm_assign/<str:pickup_id>/',views.confirm_assign,name='confirm_assign'),
    path('finish_pickup/<str:pickup_id>/',views.finish_pickup,name='finish_pickup'),
    path('assigned_pickups/',views.assigned_pickups,name='assigned_pickups'),
    path('personal_pickup/',views.personal_pickup,name='personal_pickup'),
    path('completed/',views.completed_pickups,name='completed'),
    path('edit_user/',views.edituser,name='edit_user'),
    path('payment_success',views.successpayment,name='payment_success'),
]