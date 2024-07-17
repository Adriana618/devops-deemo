"""
Module for registering models with the Django admin site.

This module registers the User model with the Django admin site, allowing it to be managed
through the admin interface.
"""

from django.contrib import admin
from .models import User

admin.site.register(User)
