"""hotelmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from hoteltacos import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index,name='index'),
    path("chefregister", views.chefregister,name='chefregister'),
    path("pagerenderchefregister", views.pagerenderchefregister,name='pagerenderchefregister'),
    path("loginpagerender", views.loginpagerender,name='loginpagerender'),
    path("adminviewallchef", views.adminviewallchef,name='adminviewallchef'),
    path("staffregister", views.staffregister,name='staffregister'),
    path("pagerenderstaffregister", views.pagerenderstaffregister,name='pagerenderstaffregister'),
    path("chefdashboard", views.chefdashboard,name='chefdashboard'),
    path("foradmintoapprovechef/<int:reg_id>",views.foradmintoapprovechef,name='foradmintoapprovechef'),
    path("adminapprovedchef", views.adminapprovedchef,name='adminapprovedchef'),
    path("chef_profile", views.chef_profile,name='chef_profile'),
    path("rejectchef/<int:id>",views.rejectchef,name='rejectchef'),
    path("adminviewallstaff", views.adminviewallstaff,name='adminviewallstaff'),
    path("staff_profile", views.staff_profile,name='staff_profile'),
    path("updatestaffprofile/<int:id>",views.updatestaffprofile,name='updatestaffprofile'),
    path("foradmintoapprovestaff/<int:reg_id>",views.foradmintoapprovestaff,name='foradmintoapprovestaff'),
    path("adminapprovedstaff", views.adminapprovedstaff,name='adminapprovedstaff'),
    path("rejectstaff/<int:id>",views.rejectstaff,name='rejectstaff'),
    path("loginactivate", views.loginactivate,name='loginactivate'),
    path("mainfood", views.mainfood,name='mainfood'),
    path("updatechefprofile/<int:id>",views.updatechefprofile,name='updatechefprofile'),
    path("editchefprofile/<int:id>",views.editchefprofile,name='editchefprofile'),
    path("editstaffprofile/<int:id>",views.editstaffprofile,name='editstaffprofile'),
    path("career", views.career,name='career'),
    path("contactus", views.contactus,name='contactus'),
    path("reservation", views.reservation,name='reservation'),
    path("bookreservation", views.bookreservation,name='bookreservation'),
    path("outsideuserregister", views.outsideuserregister,name='outsideuserregister'),
    path("pagerenderoutsiderregister", views.pagerenderoutsiderregister,name='pagerenderoutsiderregister'),
    path("adminviewalloutsideuser", views.adminviewalloutsideuser,name='adminviewalloutsideuser'),
    path("toapproveoutsideuser/<int:reg_id>",views.toapproveoutsideuser,name='toapproveoutsideuser'),
    path("rejectoutsideuser/<int:id>",views.rejectoutsideuser,name='rejectoutsideuser'),
    path("adminapprovedoutsideuser", views.adminapprovedoutsideuser,name='adminapprovedoutsideuser'),
    path("thankyoupage", views.thankyoupage,name='thankyoupage'),
    path("viewallreser", views.viewallreser,name='viewallreser'),
    path("reserapprove/<int:reg_id>",views.reserapprove,name='reserapprove'),
    path("approvedreser", views.approvedreser,name='approvedreser'),
  
]
