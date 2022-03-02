import asyncio
import aiohttp
from typing import List
from fastapi import APIRouter
from config import settings
from models.second_task import Record
from utils.data_generator import generate_records
from utils.lists_utils import merge_ordered_lists
from utils.sources_client import SourcesClient

router = APIRouter(prefix='/second-task')

IDS_ALLOCATIONS = {
    'first_source': ((1, 11), (31, 41)),
    'second_source': ((11, 21), (41, 51)),
    'third_source': ((21, 31), (51, 61))
}


@router.get(
    '/records',
    summary='Get sorted list of records',
    response_model=List[Record]
)
async def get_ordered_records():
    async with aiohttp.ClientSession() as session:
        client = SourcesClient(session=session)
        coroutines = [client.get_sorted_records(url) for url in settings.SOURCES_URLS]
        ordered_list = []
        for coroutine in asyncio.as_completed(coroutines):
            ordered_list = await merge_ordered_lists(await coroutine, ordered_list)

        return ordered_list


@router.get(
    '/first-source',
    summary='First resource with records',
    response_model=List[Record]
)
async def get_ordered_data():
    return await generate_records(IDS_ALLOCATIONS['first_source'])


@router.get(
    '/second-source',
    summary='Second resource with records',
    response_model=List[Record]
)
async def get_ordered_data():
    return await generate_records(IDS_ALLOCATIONS['second_source'])


@router.get(
    '/third-source',
    summary='Third resource with records',
    response_model=List[Record]
)
async def get_ordered_data():
    return await generate_records(IDS_ALLOCATIONS['third_source'])

