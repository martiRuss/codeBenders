from django.contrib import admin
from django.urls import path, include
from analyze import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.regoPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('dash/', include('analyze.urls')),
    path('logout/', views.LogOutpage, name='logout'),
    
]
