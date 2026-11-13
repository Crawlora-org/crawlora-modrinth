"""Typed Modrinth client for the Crawlora hosted API."""

from .platform import ModrinthClient, AsyncModrinthClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = ModrinthClient
AsyncClient = AsyncModrinthClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Modrinth'
PLATFORM = 'modrinth'
CONTRACT_REVISION = 'sha256:5341542aa3348dd1331db6d30348f76aed08640ae369839ddf821af91bd7c21f'

__all__ = [
    "ModrinthClient", "AsyncModrinthClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
