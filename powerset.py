def power_set(a,lst):
    if len(a) == 0:
        print(lst)
    else:
        power_set(a[1:],lst)
        power_set(a[1:],lst+[a[0]])

a=[1,2]
power_set(a,[])
