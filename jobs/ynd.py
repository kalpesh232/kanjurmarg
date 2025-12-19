# ---------- Singleton design pattern in python ---------- #
class Config:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__instance = {"Them" : "Dark", "Version" : 1.0}
        return cls.__instance
    
config1 = Config()
config2 = Config()

print(config1 is config2)
# print(config1.setting)


