"""Pydantic model for Adobe Audition Sesx project files.

This project is designed to allow full reading and writing of .sesx files without
 breaking the project files or losing any data.
This is fully powered by pydantic and pydantic-xml,
 providing high performance and reliability.
"""

__version__ = "0.1.0"

from .model import Sesx

__all__ = [
    "Sesx",
]
