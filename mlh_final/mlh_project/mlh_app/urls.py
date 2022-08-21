from django.urls import path
from . import views
from django.urls import include, re_path
from django.conf import settings

# Added all of the URLs which are used in this application
urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('', views.loginPage, name="login"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    # path('main_page/', views.main_page, name="main_page"),
    # re_path(r'^insert$', views.insert, name='insert')

    # path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('addInForum/', views.addInForum, name='addInForum'),
    path('addInDiscussion/', views.addInDiscussion, name='addInDiscussion'),
    path('addInDiscussion/', views.addInDiscussion, name='addInDiscussion'),
    path('asia/', views.asia, name='asia'),
    path('africa/', views.africa, name='africa'),
    path('northAmerica/', views.northAmerica, name='northAmerica'),
    path('southAmerica/', views.southAmerica, name='southAmerica'),
    path('antarctica/', views.antarctica, name='antarctica'),
    path('europe/', views.europe, name='europe'),
    path('oceania/', views.oceania, name='oceania'),
    path('upload_display_video/', views.upload_display_video, name='upload_display_video'),
    path('handle_uploaded_file/', views.handle_uploaded_file, name='handle_uploaded_file'),
    path('points/', views.points, name='points'),

]
