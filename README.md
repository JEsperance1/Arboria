Arboria

Arboria is a work-in-progress top-down adventure game inspired by classics like The Legend of Zelda: The Minish Cap. Built with Python and Pygame, Arboria features sprite-based movement, tile maps, and a retro-style overworld with interactive objects and NPCs.

Project Highlights

Top-down gameplay reminiscent of GBA-era Zelda titles.

Sprite-based rendering with an asset pipeline for characters, environment tiles, and UI.

Modular code structure with src/ for game logic, assets/ for sprites and maps, and tests/ for automated validation.

Fully cross-platform codebase (Windows, macOS, Linux).

Build & Deployment Pipeline

This project uses a CI/CD pipeline to automatically test, package, and deliver the game:

Pytest Integration – Runs automated tests on every push to ensure stability.

PyInstaller Packaging – Bundles the game into a standalone .exe so no Python installation is needed for end-users.

AWS CodeBuild – Handles build and packaging steps in a controlled environment.

Artifact Delivery via S3 – The built executable is uploaded to an Amazon S3 bucket for easy download and distribution.

Platform Agnostic Builds – Pipeline can be switched between Linux and Windows build containers for different output formats.

With every commit, Arboria’s pipeline ensures the game is tested, packaged, and ready to share — making iteration and distribution fast and reliable.
