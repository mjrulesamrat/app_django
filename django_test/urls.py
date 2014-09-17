from django.conf.urls import patterns, include, url
from article.views import HelloTemplate
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^articles/', include('article.urls')),
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^hello/$', 'article.views.hello'),
     url(r'^hello_template/$', 'article.views.hello_template'),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^accounts/login', 'django_test.views.login'),
     url(r'^accounts/logout', 'django_test.views.logout'), 
     url(r'^accounts/auth', 'django_test.views.auth_view'),
     url(r'^accounts/loggedin', 'django_test.views.loggedin'),
     url(r'^accounts/invalid', 'django_test.views.invalid_login'),
     #this is latest added send url...17-9-14
     url(r'^send/$', 'demo1.views.post'),
    # url(r'^hello_template_simple/$', 'article.views.hello_template_simple'),
    # url(r'^hello_mj_class/$', HelloTemplate.as_view()),
)
