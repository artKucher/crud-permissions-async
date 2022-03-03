import random
from typing import Tuple, List
from uuid import uuid4
from models.second_task import Record


async def generate_records(ids_allocations: Tuple) -> List[Record]:
    result = []
    for ids_allocation in ids_allocations:
        for record_id in range(*ids_allocation):
            result.append(Record(id=record_id, name=str(uuid4())))
    random.shuffle(result)
    return result
