"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('app',views.appoint),
    path('adm',views.adminlog),
    path('adm2',views.admin2),
    path('admlog',views.adminlog2),
    path('login1',views.login),
    path('sign',views.signup),
    path('signup2',views.signup2),
    path('homepage',views.homepage),
    path('logout',views.logout),
    path('doc',views.doctors1),
    path('docform',views.doctorform),
    path('regdoc',views.reg_docs),
    path('del_doc/<id>',views.del_doc),
    path('book',views.book_appoint),
    path('home2',views.home2),
    path('adm_app',views.admin_app),
    path('del_app/<id>',views.del_app),
    path('accept_app/<id>',views.accept_app),
    path('bk_details',views.booking_details),
]
