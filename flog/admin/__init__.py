"""
MIT License
Copyright(c) 2021 Andy Zhou
"""
from flask import Blueprint

admin_bp = Blueprint("admin", __name__)

from . import views
