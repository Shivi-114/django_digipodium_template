
from app.models import Equipment
from django.urls import path  
from .views import homeview, welcomeview, ordering, view_hr, detail_hr, purchase, rent, service_request, user_profile, equipment
from .views import user_profileview, edit_profileview, about
urlpatterns = [
    path('', homeview, name='home'),
    path('welcome/',welcomeview, name='welcome'),
    path('ordering/',ordering,name='ordering'),
    path('hr/view',view_hr, name='view_hr'),
    path('hr/detail/<int:pk>',detail_hr, name='detail_hr'),
    path('purchase/',purchase, name='pc'),
    path('rent/',rent, name='rs'),
    path('service/request/<int:pk>',service_request, name='sr'),
    path('user/profile',user_profile, name='up'),
    path('euipment/',equipment, name='eq'),
    path('userprofile/', user_profileview, name='up'),
    path('editprofile/<int:pk>', edit_profileview, name='editpro'),
    path('about/',about, name='about')

]