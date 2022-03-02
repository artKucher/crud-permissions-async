import asyncio
import aiohttp
from typing import List
from pydantic import AnyHttpUrl, parse_obj_as

from config import settings
from models.second_task import Record


class SourcesClient:
    REQUEST_TIMEOUT = aiohttp.ClientTimeout(settings.SOURCES_REQUEST_TIMEOUT_SECONDS)

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    async def get_sorted_records(self, source_url: AnyHttpUrl) -> List[Record]:
        try:
            async with self.session.get(source_url, timeout=self.REQUEST_TIMEOUT, raise_for_status=True) as response:
                data = await response.json()
                records = parse_obj_as(List[Record], data)
                return sorted(records)
        except (asyncio.TimeoutError, aiohttp.ClientResponseError):
            return []
