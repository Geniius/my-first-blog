from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
<<<<<<< HEAD
    url(r'^test$', views.post_edit, name='test'),
    url(r'^base$', views.base, name='base'),
    url(r'^freelance$', views.freelance, name='freelance'),


=======
>>>>>>> b4d9de804ba72fd6be89302ce17e50fe533797ec
]