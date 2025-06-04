class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating the instance")
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            print("Instance already created")
        return cls._instance
        
    def __init__(self, value):
        if not hasattr(self,'initialized'):
            self.value = value
            self.initialized = True
            
s1 = Singleton("First")
print(s1)
print(s1.value)
s2 = Singleton("Second")
print(s2)
print(s2.value)
print(s1 == s2)

