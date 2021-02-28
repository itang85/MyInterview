# import re
#
# s = input()
# answer = re.findall(r'[\u4e00-\u9fa5]', s)
# print(answer)


# print(*[(1,2),(3,4)])
# #
# #
# # def test(*args):
# #     print(args)
# #
# # test(1,2,3,4,5,6,(1,2))


# # 带参数的装饰器
# def outer(out_args):
#     def middle(func):
#         def wrapper(*args, **kwargs):
#             print(out_args)
#             wrapper_result = func(*args, **kwargs)
#             print(wrapper_result)
#             return wrapper_result
#         return wrapper
#     return middle
#
#
# @outer("hello")
# def foo(a, b):
#     return a + b
#
#
# foo(2, 3)


# dic = {
#     '张三': 2,
#     '李四': 1,
#     '王麻子': 10,
# }
# dic_item = dic.items()
# dic_item = sorted(dic_item, key=lambda x:x[1], reverse=True)
# print(dict(dic_item))



print('abcdcd'.find('cd'))
