import sys
import importlib
import pytest

REQUIRED_PACKAGES = ["pygame"]

def test_python_version():
    major, minor = sys.version_info[:2]
    assert major == 3 and minor >= 8, "Python 3.8+ is required"

@pytest.mark.parametrize("pkg", REQUIRED_PACKAGES)
def test_required_packages_installed(pkg):
    assert importlib.util.find_spec(pkg) is not None, f"{pkg} is not installed"

import pygame

def test_game_launch_and_quit():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Test Launch")
    pygame.quit()

import os
import pygame
import pytest

ASSET_DIRS = ["assets/images", "assets/sounds"]

@pytest.mark.parametrize("directory", ASSET_DIRS)
def test_assets_loadable(directory):
    pygame.init()
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            try:
                if file.lower().endswith((".png", ".jpg")):
                    pygame.image.load(path)
                elif file.lower().endswith((".wav", ".mp3", ".ogg")):
                    pygame.mixer.Sound(path)
            except Exception as e:
                pytest.fail(f"Failed to load {path}: {e}")
    pygame.quit()

import pygame
import time

def test_frame_time_under_threshold():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    for _ in range(10):
        start = time.time()
        clock.tick(60)  # Target 60 FPS
        elapsed = time.time() - start
        assert elapsed < 0.05, f"Frame took too long: {elapsed:.3f}s"

    pygame.quit()
