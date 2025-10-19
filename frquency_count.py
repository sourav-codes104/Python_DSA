sugar = "1234356789"
seen = {}
for s in sugar:
    if s in seen:
        seen[s] += 1
    else:
        seen[s] = 1
for k,v in seen.items():
    if v > 1:
        print(k,"->",v,"Repeated value")
    elif v == 0:
        print(k, "->", v, "not present")
    else:
        print(k,"->",v,"present only once")
