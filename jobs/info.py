flat_ls = []
def flatten_list(data):
    for item in data:
        if isinstance(item,list):
            # flat_ls.extend(flatten_list(item))
            flatten_list(item)
        else:
            flat_ls.append(item)

data =  [1, 2, 3, [4, 5, [6, 7, 8, [13, 14]], 9, 10], 11, 12]
flatten_list(data)
print(flat_ls)