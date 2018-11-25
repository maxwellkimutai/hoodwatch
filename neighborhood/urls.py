from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name = 'index'),
    url('^edit_profile/(?P<username>\w{0,50})',views.edit_profile,name = 'edit_profile'),
    url('^businesses$',views.businesses,name = 'businesses'),
    url('^post/(?P<id>\d+)',views.post,name='post'),
    url(r'^search/$',views.search,name='search'),
    url('^api/businesses/$',views.BusinessList.as_view())

]
