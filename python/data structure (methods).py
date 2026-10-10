#---list---
print("---list---")
nums=[3,1,2]
print(nums)

nums.append(5)
print("append:", nums)

nums.insert(0, 9)
print("insert:", nums)

nums.remove(1)
print("remove:", nums)

nums.sort()
print("sort:", nums)

last=nums.pop()
print("pop:", last,'\n', nums)

nums.reverse()
print("reverse:", nums)

last=nums.count(3)
print("count:",last,'\n', nums)



#---set---
print("---set---")
s={1,2,2,4,4,6}
print(s)

s.add(3)
print("add:", s)

s.remove(1)
print("remove:", s)

s.discard(9)
print("discard:", s)

print("union:", {1,2}.union({2,3}))

print("intersection:", {1,2}.intersection({2,3}))

print("difference:", {1,2}.difference({2,3}))

s.clear()
print("clear:", s)

#---tuple---
print("---tuple---")
t= (1,2,2,3)
print(t)

print("count:", t.count(2))

print("index:", t.index(3))

print("sorted:", sorted(t))

print("len:", t.__len__())
print("len:", len(t))

print("max:", max(t))

print("min:", min(t))

print("sum:", sum(t))
#---dictionary---
print("---dictionary---")
d={"a": 1, "b": 2}
print(d)

print("get:", d.get("a"))     #value a? 1
print("keys:", d.keys())
print("values:", d.values())
print("items:", d.items())

d.update({"c": 3})
print("update:", d)

print("pop:", d.pop("a"))
print("afater pop:", d)

print("setdefault:", d.setdefault('z',0))
print("after setdefault:", d)