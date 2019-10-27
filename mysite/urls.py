from django.conf.urls import include, url
from django.contrib import admin
from manageUser.views import index
from manageUser.views import about
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'index',index, name="index"),  
    url(r'about',about, name="about"),
    url(r'accounts/',include('accounts.urls'))

]
