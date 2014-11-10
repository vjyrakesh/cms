from django.conf.urls import patterns, include, url
from search.views import search, hello
from django.contrib import admin
#import coltrane
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^tinymce/(?P<path>.*)$','django.views.static.serve',{'document-root':'C:/RAKESH/djangowork/cms/cms/templates/admin/flatpages/flatpage/tinymce'}),
    url(r'^hello/$',hello),
    url(r'^search/$',search),
    url(r'^weblog/$','coltrane.views.entries_index'),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','coltrane.views.entry_detail'),
    url(r'^addsource/$','myfeeder.views.addsource'),
    url(r'^myfeeder/home/$','myfeeder.views.feedhome'),
    url(r'^source/(\w+)/$','myfeeder.views.feed_entries'),
    #url(r'',include('django.contrib.flatpages.urls')),
    

)
