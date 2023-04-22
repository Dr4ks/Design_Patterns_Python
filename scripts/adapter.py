class Adaptee:  
    def specific_request(self):
        return "Specific request."

class Target:
    def request(self):
        return "Generic request."

class Adapter(Target): 
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    print(adapter.request())
