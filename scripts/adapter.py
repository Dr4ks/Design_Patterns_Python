# Adaptee
class OldPrinter:
    def print_message(self, message):  # This is specificRequest()
        print(f"Old Printer: {message}")

# Target Interface
class NewPrinterInterface:
    def print(self, text):
        pass

# Adapter
class PrinterAdapter(NewPrinterInterface,OldPrinter):
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self, text):
        self.old_printer.print_message(text)  # Adaptee.specificRequest()

# Client 
def client_code(printer):
    printer.print("Hello, World!")

# Usage
old_printer = OldPrinter()
adapter = PrinterAdapter(old_printer)
client_code(adapter)


## Output
# Old Printer: Hello, World!
