resources = {"shards": 0, "fragments": 0, "motes": 0}
legendary_is_collected = False

while True:
    data = input().split()
    for idx in range(0, len(data), 2):
        resource = data[idx + 1].lower()
        quantity = int(data[idx])
        if resource not in resources:
            resources[resource] = 0
        resources[resource] += quantity
        if resources.get("shards") >= 250 or resources.get("fragments") >= 250 or resources.get("motes") >= 250:
            legendary_is_collected = True
            break
    if legendary_is_collected:
        break

key_material = [key for key, value in resources.items() if value >= 250]
resources[key_material[0]] -= 250
legendary_item_obtained = ''
if key_material[0] == "shards":
    legendary_item_obtained = "Shadowmourne"
elif key_material[0] == "fragments":
    legendary_item_obtained = "Valanyr"
elif key_material[0] == "motes":
    legendary_item_obtained = "Dragonwrath"

key_materials_ls = ["shards", "fragments", "motes"]
key_materials_dc = {item: value for item, value in resources.items() if item in key_materials_ls}
junk_materials = {item: value for item, value in resources.items() if item not in key_materials_ls}

key_mat_sorted = sorted(key_materials_dc, key = lambda k: (-key_materials_dc[k], k))
junk_mat_sorted = sorted(junk_materials)

print(f"{legendary_item_obtained} obtained!")
for material in key_mat_sorted:
    print(f"{material}: {resources[material]}")
for material in junk_mat_sorted:
    print(f"{material}: {resources[material]}")
