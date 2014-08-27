from django.conf.urls import patterns, include, url
from article.views import HelloTemplate
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^articles/', include('article.urls')),
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^index/$', 'article.views.index'),
     url(r'^hello/$', 'article.views.hello'),
     url(r'^hello_template/$', 'article.views.hello_template'),
     url(r'^admin/', include(admin.site.urls)),
    # url(r'^hello_template_simple/$', 'article.views.hello_template_simple'),
    # url(r'^hello_mj_class/$', HelloTemplate.as_view()),
)
