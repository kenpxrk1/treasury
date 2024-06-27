# 1.1
# def buy_cats(func):
#     def wrapper(*args, **kwargs):
#         print("Покупайте наших котиков!")
#         print(func(*args, **kwargs))
#     return wrapper
#
#
# @buy_cats
# def print_cats(*args, **kwargs):
#
#     return f"""
#        ("`-''-/").___..--''"`-._
#     `6_ 6  )   `-.  (     ).`-.__.`)
#     (_Y_.)'  ._   )  `._ `. ``-..-'
#   _..`--'_..-_/  /--'_.' ,'
#  (il),-''  (li),'  ((!.-'
#  Это - {" / ".join(args)}   """

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# 1.2
def df_buy_cats(_str: str):
    def buy_cats(func):
        def wrapper(*args, **kwargs):
            print(_str)
            print(func(*args, **kwargs))
        return wrapper
    return buy_cats


@df_buy_cats(_str="Покупайте наших котиков")
def print_cats(*args, **kwargs):

    return f"""
       ("`-''-/").___..--''"`-._
    `6_ 6  )   `-.  (     ).`-.__.`)
    (_Y_.)'  ._   )  `._ `. ``-..-'
  _..`--'_..-_/  /--'_.' ,'
 (il),-''  (li),'  ((!.-'
 Это - {" / ".join(args)}   """


