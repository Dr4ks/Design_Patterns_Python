# Singleton
class Logger:
    _instance = None  # instance

    def __new__(cls):  # getInstance()
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialize the instance here
            cls._instance.log_file = "logfile.txt"
        return cls._instance

    def log(self, message):
        pass

# Client code
def client_code():
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("Message logged by logger1")
    logger2.log("Message logged by logger2")

    print(f"Logger 1 file: {logger1.log_file}")
    print(f"Logger 2 file: {logger2.log_file}")

    print(f"Are logger1 and logger2 the same instance? {logger1 is logger2}")

# Usage
client_code()

## Output
# Logger 1 file: logfile.txt
# Logger 2 file: logfile.txt
# Are logger1 and logger2 the same instance? True