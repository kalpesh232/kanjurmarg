class Logger:
    _instant = None

    def __new__(cls):
        if cls._instant is None :
            cls._instant = super().__new__(cls)
            cls._instant.log_file = 'log.txt'

            return cls._instant
    
    def log_text(self, message):
        with open("log.txt", "a") as file:
            file.write(message + "\n")