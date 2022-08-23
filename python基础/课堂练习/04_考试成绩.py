'''
info={"student":"tom","score":{"english":60,"math":90}}
将python的成绩80更新到score中,并打印"xxx的总成绩为xxx"
'''
info={"student":"tom","score":{"english":60,"math":90}}
info['score']['python'] = 80
print(info)
d = info["score"]["english"] + info["score"]["math"] + info["score"]["python"]
print(f'{info["student"]}的总成绩为{d}')
