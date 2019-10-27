from django.conf.urls import include, url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'login',views.login, name="login"),
    url(r'logout',views.logout, name="logout"),
    url(r'register',views.register, name="register"),
    url(r'dashboard',views.dashboard, name="dashboard"),
    
]