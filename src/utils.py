import sys
import os
import pygame

def resource_path(relative_path):
    """Get absolute path to resource, works in dev and PyInstaller"""
    try:
        # PyInstaller stores temp path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Dev mode: relative to project root
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(base_path, relative_path)