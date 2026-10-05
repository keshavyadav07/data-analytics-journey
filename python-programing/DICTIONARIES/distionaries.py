info = { "name":"keshav","city":"indore","age" :"20","income":"50000"}

print(info)
print(info["city"])
print(info.get("nameee"))
info["cast"] = "obc"
print(info)
info.pop("cast")
print(info)
info["section"] = "B1"
print(info)
info.popitem()
print(info)
print(info.keys())
print(info.values())
print(info.items())
info.update({"name":"keshav yadav","city":"indore","age" :"21","income":"500000"})
print(info)
del info["income"]
print(info)