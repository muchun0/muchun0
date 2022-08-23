import yaml
with open(r'../data/consName_data.yaml', 'r', encoding='utf8') as fp:
    a = yaml.full_load(fp)
print(a)