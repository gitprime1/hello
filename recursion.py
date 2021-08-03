def permutaion(list1, s:list):
   if list1 == 1:
      return s
   else:
      return [
         x + y
         for y in permute(1,s)
         for x in permute(list1 - 1,s)
      ]
print(len(permutation(1, ["a","b","c"])))
print(len(permutation(3, ["a","b","c"])))
