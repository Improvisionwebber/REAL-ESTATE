from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('manage', views.manage,name='manage'),
    path('user', views.user,name='user'),
    path('register', views.register,name='register'),
    path('contact', views.contact,name='contact'),
    path('delete<int:id>/', views.contact_delete, name="contactsubmission_delete"),
    path('tables', views.tables,name='tables'),
    path('services', views.services,name='services'),
    path('add_post', views.add_post,name='add_post'),
    path('single/<int:pk>', views.single,name='single')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)