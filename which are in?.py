def in_array(array1, array2):
    ans = []

    for i in array1:
        for j in array2:
            if i in j  and i not in ans:
                ans.append(i)
                ans.sort()

    return ans

a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]



print(in_array(a1,a2))
