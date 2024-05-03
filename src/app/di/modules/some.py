import aioinject

from app.core.some.repository import SomeRepository
from lib.types import Providers

PROVIDERS: Providers = [
    aioinject.Scoped(SomeRepository),
]
