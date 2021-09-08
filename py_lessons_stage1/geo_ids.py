ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
geo_ids_set = set()
for geo_id, geo_nums in ids.items():
    geo_ids_set = geo_ids_set | set(geo_nums)
# print(geo_ids_set)