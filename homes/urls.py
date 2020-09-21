from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('login', views.login, name="login"),
    path('handtool', views.handtool, name="handtool"),
    path('machtool', views.machtool, name="machtool"),
    path('autotool', views.autotool, name="autotool"),
    path('powertool', views.powertool, name="powertool"),
    path('measuringtool', views.measuringtool, name="measuringtool"),
    path('handtool1', views.handtool1, name="handtool1"),
    path('hammer', views.hammer, name="hammer"),
    path('blockplane', views.blockplane, name="blockplane"),
    path('pliers', views.pliers, name="pliers"),
    path('screw', views.screw, name="screw"),
    path('wrench', views.wrench, name="wrench"),
    path('chisel', views.chisel, name="chisel"),
    path('saw', views.saw, name="saw"),
    path('punch', views.punch, name="punch"),
    path('file', views.file, name="file"),
    path('bench', views.bench, name="bench"),
    path('hatchet', views.hatchet, name="hatchet"),
    path('clamp', views.clamp, name="clamp"),
    path('register', views.register, name="register"),
    path('logins', views.logins, name="logins"),
    path('search', views.search, name="search")

    
]