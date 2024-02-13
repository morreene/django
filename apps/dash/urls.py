# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path, include
from apps.dash import views
# import views

urlpatterns = [

    # # The home page
    # path('', views.index, name='home'),

    # # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

    path('django_plotly_dash/', include('django_plotly_dash.urls')), #DY
    path('my-dash-app/', views.my_dash_app_view, name='my-dash-app'), #DY

]
