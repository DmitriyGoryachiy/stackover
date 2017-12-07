from django.conf.urls import url
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import logout
from core.views import signup

urlpatterns = [
    # url(r'^login/', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'core/logout.html'}, name='logout'),
    url(r'^login/$', LoginView.as_view(template_name='core/login.html'), name='login'),
    url(r'^signup/$', signup, name='signup'),
    # url('^register/', CreateView.as_view(template_name='core/register.html',form_class=UserCreationForm,success_url='/')),
    # url(r'^register/$', LoginView.as_view(template_name='core/register.html'),name='register'),


]
