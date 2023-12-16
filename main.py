from farm import Farm

bobs_farm = Farm("Bob", 0, "Maryland")

while bobs_farm.time < 40:
    bobs_farm.get_user_input()
    bobs_farm.update_Farm()