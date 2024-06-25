class Handler:  # BaseHandler
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):   # setNext method
        self.next_handler = handler
        return handler

    def handle(self, request):  
        if self.next_handler:
            return self.next_handler.handle(request)
        return None

class LowLevelSupport(Handler):
    def handle(self, request):
        if request == "low":
            return "LowLevelSupport: Handling low-level support request."
        else:
            return super().handle(request)

class MidLevelSupport(Handler):
    def handle(self, request):
        if request == "mid":
            return "MidLevelSupport: Handling mid-level support request."
        else:
            return super().handle(request)

class HighLevelSupport(Handler):
    def handle(self, request):
        if request == "high":
            return "HighLevelSupport: Handling high-level support request."
        else:
            return super().handle(request)

# Client code
def client_code(handler, request):
    result = handler.handle(request)
    if result:
        print(result)
    else:
        print("No handler could handle the request.")

# Usage
low_support = LowLevelSupport()
mid_support = MidLevelSupport()
high_support = HighLevelSupport()

low_support.set_next(mid_support).set_next(high_support)

print("Client: Sending a low-level request.")
client_code(low_support, "low")

print("\nClient: Sending a mid-level request.")
client_code(low_support, "mid")

print("\nClient: Sending a high-level request.")
client_code(low_support, "high")

print("\nClient: Sending an unknown request.")
client_code(low_support, "unknown")

## Output
# Client: Sending a low-level request.
# LowLevelSupport: Handling low-level support request.

# Client: Sending a mid-level request.
# MidLevelSupport: Handling mid-level support request.

# Client: Sending a high-level request.
# HighLevelSupport: Handling high-level support request.

# Client: Sending an unknown request.
# No handler could handle the request.