from abc import ABC, abstractmethod

# Context
class PaymentProcessor:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def process_payment(self, amount):
        self._strategy.process_payment(amount)

# Strategy
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Concrete Strategie1
class CreditCardStrategy(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Payment of ${amount} processed using Credit Card.")

# Concrete Strategie2
class PayPalStrategy(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Payment of ${amount} processed using PayPal.")

# Client code
def client_code():
    payment_processor = PaymentProcessor(CreditCardStrategy())
    payment_processor.process_payment(100)

    payment_processor.set_strategy(PayPalStrategy())
    payment_processor.process_payment(200)

# Usage
client_code()

## Output
# Payment of $100 processed using Credit Card.
# Payment of $200 processed using PayPal.
   
