"""
archive-manager - Create and manage archives

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import ArchiveManager, manage, process, main

__all__ = ["ArchiveManager", "manage", "process", "main"]
