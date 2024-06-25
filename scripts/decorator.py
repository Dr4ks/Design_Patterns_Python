from abc import ABC, abstractmethod

# Component
class Text(ABC):
    @abstractmethod
    def render(self):
        pass

# ConcreteComponent
class SimpleText(Text):
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text

# BaseDecorator
class TextDecorator(Text):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    @abstractmethod
    def render(self):
        pass

# ConcreteDecorator 1
class BoldText(TextDecorator):
    def render(self):
        return f"<b>{self._wrapped.render()}</b>"

# ConcreteDecorator 2
class ItalicText(TextDecorator):
    def render(self):
        return f"<i>{self._wrapped.render()}</i>"

# Client code
def client_code(text):
    print(text.render())

# Usage
simple_text = SimpleText("Hello, World!")
bold_text = BoldText(simple_text)
italic_text = ItalicText(simple_text)
bold_italic_text = BoldText(ItalicText(simple_text))

print("Client: Rendering simple text:")
client_code(simple_text)

print("\nClient: Rendering bold text:")
client_code(bold_text)

print("\nClient: Rendering italic text:")
client_code(italic_text)

print("\nClient: Rendering bold and italic text:")
client_code(bold_italic_text)

## Output
# Client: Rendering simple text:
# Hello, World!

# Client: Rendering bold text:
# <b>Hello, World!</b>

# Client: Rendering italic text:
# <i>Hello, World!</i>

# Client: Rendering bold and italic text:
# <b><i>Hello, World!</i></b>
