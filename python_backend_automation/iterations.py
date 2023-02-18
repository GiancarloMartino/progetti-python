# for loop

for i in range(0, 10):
    print(i)

for i in range(3, 5):
    print(i)


# iteration on list
l = [1, "giancarlo", "bobo", "cicciobello"]

print(l)
print(l[0])
print(l[3])

for e in l:
    print(e)


# iteration on dictionary
d = {"a": "Giancarlo", "b": "Melissa"}

print("il dizionario è il seguente:\n", d)
print('')
print("adesso ciclo sugli elementi del dizionario")
for key in d.keys():
    print("key:", key)
for value in d.values():
    print("value:", value)
for key, value in d.items():
    print("key:", key, "with value:", value)
