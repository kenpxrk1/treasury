import datetime as dt
from typing import Callable
import logging

# 4.1 - 4.2
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
# console_handler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
#
# logger.addHandler(console_handler)
#
#
# def get_runtime(func: Callable):
#     def wrapper(*args, **kwargs):
#         start_time = dt.datetime.now()
#         res = func(*args, **kwargs)
#         end_time = dt.datetime.now()
#         logger.info(f"Function {func.__name__} runtime equals: {end_time-start_time}")
#         return res
#     return wrapper
#
#
# @get_runtime
# def bruteforce_search(dataset: list, target_num: int) -> int | None:
#     lst = dataset
#     for i in range(len(lst)):
#         if lst[i] == target_num:
#             return i
#     return None
#
#
# @get_runtime
# def binary_search(dataset: list, target_num: int) -> int | None:
#     left = 0
#     right = len(dataset)
#     mid = len(dataset) // 2
#
#     while dataset[mid] != target_num and left < right:
#         if target_num > dataset[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1
#         mid = (left + right) // 2
#
#     if left > right:
#         return None
#     else:
#         return mid
#
#
# dataset = range(1000)
# bruteforce_search(dataset, 950)
# binary_search(dataset, 950)


# 4.3
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))

logger.addHandler(console_handler)


def logging_runtime(file_path: str):
    logging.basicConfig(level=logging.INFO, filename=file_path, filemode="a")

    def get_runtime(func: Callable):
        def wrapper(*args, **kwargs):
            start_time = dt.datetime.now()
            res = func(*args, **kwargs)
            end_time = dt.datetime.now()
            logging.info(f"Function {func.__name__} runtime equals: {end_time-start_time}")
            return res
        return wrapper
    return get_runtime


@logging_runtime("logs/runtime.log")
def bruteforce_search(dataset: list, target_num: int) -> int | None:
    lst = dataset
    for i in range(len(lst)):
        if lst[i] == target_num:
            return i
    return None


@logging_runtime("decorators/runtime.log")
def binary_search(dataset: list, target_num: int) -> int | None:
    left = 0
    right = len(dataset)
    mid = len(dataset) // 2

    while dataset[mid] != target_num and left < right:
        if target_num > dataset[mid]:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    if left > right:
        return None
    else:
        return mid


dataset = range(10000)
bruteforce_search(dataset, 950)
binary_search(dataset, 950)



