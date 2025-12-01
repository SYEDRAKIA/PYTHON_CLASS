words = input("Enter words: ").split()
groups = {}

for w in words:
    key = "".join(sorted(w))
    if key not in groups:
        groups[key] = []
    groups[key].append(w)

for g in groups.values():
    print(g)