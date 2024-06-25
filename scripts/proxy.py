from abc import ABC, abstractmethod

# Service interface
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

# ConcreteService
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")

# ProxyService
class Proxy(Subject):
    def __init__(self):
        self._real_subject = RealSubject() # ConcreteService

    def request(self):
        # Access control or additional logic can be added here
        print("Proxy: Checking access before handling request.")
        self._real_subject.request()

# Client code
def client_code(subject: Subject):
    subject.request()

# Usage
def main():
    real_subject = RealSubject()
    proxy = Proxy()

    print("Client: Directly interacting with the RealSubject:")
    client_code(real_subject)

    print("\nClient: Indirectly interacting with the Proxy:")
    client_code(proxy)

if __name__ == "__main__":
    main()

## Output
# Client: Directly interacting with the RealSubject:
# RealSubject: Handling request.

# Client: Indirectly interacting with the Proxy:
# Proxy: Checking access before handling request.
# RealSubject: Handling request.
