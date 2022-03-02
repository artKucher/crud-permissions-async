from typing import List
from models.second_task import Record


async def merge_ordered_lists(first_list: List[Record], second_list: List[Record]) -> List[Record]:
    if not first_list or not second_list:
        return first_list or second_list
    result = []
    i, j = 0, 0
    while i < len(first_list) and j < len(second_list):
        if first_list[i] < second_list[j]:
            result.append(first_list[i])
            i += 1
        else:
            result.append(second_list[j])
            j += 1

    return result + first_list[i:] + second_list[j:]
