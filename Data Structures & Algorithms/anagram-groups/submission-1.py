# def manual_counter(s):
#     d=dict()
#     for k in s:
#         d[k]=d.get(k,0)+1
#     return d

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groups=[]
#         for word in strs:
#             found=False
#             for group in groups:
#                 if manual_counter(word)==manual_counter(group[0]):
#                     group.append(word)
#                     found=True
#                     break
#             if not found:
#                 groups.append([word])
#         return groups


from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in d:
                d[key] = []

            d[key].append(word)

        return list(d.values())
        


                
        