# 2.1
# def retry_10_times_if_exc(func):
#     tries = 0
#
#     def wrapper(*args):
#         nonlocal tries
#         while tries <= 10:
#             try:
#                 print(f"Попытка вызвать функцию номер {tries+1}")
#                 return func(*args)
#
#             except Exception as e:
#                 tries += 1
#                 if tries == 10:
#                     raise e
#
#     return wrapper


# @retry_10_times_if_exc
# def number_division(*args):
#     return int(args[0]) / int(args[1])

# -----------------------------------------------------------------------------------------------------

# 2.2
def retry(retry_count: int):
    def retry_n_times(func):
        tries = 0

        def wrapper(*args):
            nonlocal tries
            while tries <= retry_count:
                try:
                    print(f"Попытка вызвать функцию номер {tries+1}")
                    return func(*args)

                except Exception as e:
                    tries += 1
                    if tries == retry_count:
                        raise e

        return wrapper
    return retry_n_times


@retry(retry_count=20)
def number_division(*args):
    return int(args[0]) / int(args[1])


number_division(10, 0)

