class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def some_method(self):
        print("Some method")
    
s1 = Singleton()
s2 = Singleton()

print(s1 == s2) 

s1.some_method()  
s2.some_method()  

