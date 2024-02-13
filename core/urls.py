# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),                # Django admin route

    path("", include("apps.users.urls")),  # New with Google OAuth
    path('accounts/', include('allauth.urls')),
    path('social-account/', include('allauth.socialaccount.urls')),


    # path("", include("apps.authentication.urls")),  # Original Auth routes - login / register
    path("", include('apps.subscriptions.urls')),   # Stripe subscription
    path("", include("apps.dash.urls")),            # Dash app
    path("", include("apps.home.urls")),            # UI Kits Html files    

]
