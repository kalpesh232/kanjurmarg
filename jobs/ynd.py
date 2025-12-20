# ---------- Singleton design pattern in python ---------- #
# class Config:
#     __instance = None

#     def __new__(cls):
#         if not cls.__instance:
#             cls.__instance = super().__new__(cls)
#             cls.__instance = {"Them" : "Dark", "Version" : 1.0}
#         return cls.__instance
    
# config1 = Config()
# config2 = Config()

# print(config1 is config2)
# # print(config1.setting)

# From a string, extract all unique substrings starting from length 3 and return them in length-wise order.
a = "xyzyxzxzyyzx"

result = []
seen = set()

n = len(a)

for length in range(3, n + 1):          # length 3 → n
    for i in range(n - length + 1):
        sub = a[i:i + length]
        if sub not in seen:
            seen.add(sub)
            result.append(sub)

print(tuple(result))
# ('xyz', 'yzx', 'xyzx')