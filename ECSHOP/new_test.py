# def odd():
#     funcs = []
#     for c in "abcdefg":
#         funcs.append((lambda :c))
#     return funcs
# for func in odd():
#     print(odd())
#     print(func())
a =  "abcdefg"
for i in a:
    print(lambda :i)