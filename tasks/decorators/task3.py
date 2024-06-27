import redis


r = redis.Redis(host="localhost", port=6379, decode_responses=True)

# 3.1
# def cache_result(func):
#     def wrapper(*args, **kwargs):
#         key = [str(arg) for arg in args]
#         key = "-".join(key)
#         cache_value = r.get(key)
#         if cache_value:
#             print("Достаем данные из кэша...")
#             return cache_value
#         res = func(*args, **kwargs)
#         r.set(key, res)
#         return res
#     return wrapper
#
#
# @cache_result
# def multiply_numbers(x: float, y: float) -> float:
#     print("Calculating result....")
#     return x * y

# 2.2
# def cache_result(func):
#     def wrapper(*args, **kwargs):
#         key = [str(arg) for arg in args]
#         key = "-".join(key)
#         cache_value = r.get(key)
#         if cache_value:
#             print("Достаем данные из кэша...")
#             return cache_value
#         res = func(*args, **kwargs)
#         r.set(key, res, ex=10)
#         return res
#     return wrapper
#
#
# @cache_result
# def multiply_numbers(x: float, y: float) -> float:
#     print("Calculating result....")
#     return x * y

# 3.3
def cache_f_result(cached_time: int):
    """
    If args still cached it will be returned from cache
    else running the function and caching result

    :param cached_time: integer - count of seconds that result of the function is still actually
    :return: result of the function.
    """
    def cache_result(func):
        def wrapper(*args, **kwargs):
            key = [str(arg) for arg in args]
            key = "-".join(key)
            cache_value = r.get(key)
            if cache_value:
                print("Достаем данные из кэша...")
                return cache_value
            res = func(*args, **kwargs)
            r.set(key, res, ex=cached_time)
            return res
        return wrapper
    return cache_result


@cache_f_result(cached_time=2)
def multiply_numbers(x: float, y: float) -> float:
    print("Calculating result....")
    return x * y


print(multiply_numbers(2, 2))