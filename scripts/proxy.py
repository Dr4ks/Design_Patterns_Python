class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")

        
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()
