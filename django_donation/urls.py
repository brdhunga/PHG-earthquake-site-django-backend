from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',

    #front page
    url(r'^$', 'home_app.views.home', name='home'),
    url(r'^about/', TemplateView.as_view(template_name = "index.html"), name='about'),


    # apis 
    url(r'^api/home/',
        'home_app.views.home_api',
        name='api.home'
        ),
    url(r'^api/faq/',
        'faq_about_app.views.faq_api',
        name='api.faq_and_about'
        ),
    url(r'^api/about/',
        'faq_about_app.views.about_api',
        name='api.about_api'
        ),


    url(r'^admin/', include(admin.site.urls)),
)
