from django.conf.urls import url
from django.contrib import admin
from donkidik import views, api

urlpatterns = [

    # VIEWS
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),

    # API

    # HOME VIEW
    url(r'^api/feed$', api.get_feed),
    url(r'^api/sessions$', api.get_sessions),

    # POST api
    url(r'^api/post/create$', api.post_create),
    url(r'^api/post/update$', api.post_update),
    url(r'^api/post/delete$', api.post_delete),
    url(r'^api/post/upvote$', api.post_upvote),
    url(r'^api/post/downvote$', api.post_downvote),

    # COMMENT api
    url(r'^api/comments$', api.get_comments),
    url(r'^api/comment/add$', api.add_comment),
    url(r'^api/comment/remove$', api.remove_comment),

    # USER api

]
