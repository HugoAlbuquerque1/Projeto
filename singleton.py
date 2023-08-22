
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.iniciar()
        return cls._instance
    
    def iniciar(self):
        self.connection = None
        