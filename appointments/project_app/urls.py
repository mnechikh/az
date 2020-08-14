from django.conf.urls import url 
from . import views
from django.contrib.auth import views as auth_views
from project_app.views import appointmentsdetail
from users import views as user_views
from django.urls import path, include

urlpatterns = [
		url(r'schedule',views.schedule ,name='schedule'),
		url(r'appointment/$',views.appointment ,name='appointment'),
		url(r'view/$',views.view,name='view'),
		url(r'appointmentsdetail/(?P<pk>\d+)$',views.appointmentsdetail.as_view() ,name='appointmentsdetail'),
		url(r'^post/new/$', views.post_new, name='post_new'),
		url(r'^view/(?P<pk>\d+)/remove/$', views.appoint_remove, name='appoint_remove'),
		path('contact.html', views.contact, name="contact"),
		path('', views.home, name="home"),
		path('about.html', views.about, name="about"),
		path('pricing.html', views.pricing, name="pricing"),
		path('service.html', views.service, name="service"),
		path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
		path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
		path('profile/', user_views.profile, name='profile'),
		url(r'^register/', user_views.register, name='register'),

]