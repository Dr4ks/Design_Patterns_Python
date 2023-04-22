class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.handle_request(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass')


class ConcreteHandlerA(Handler):
    def _handle(self, request):
        if 0 < request <= 10:
            print(f'Request {request} handled by ConcreteHandlerA')
            return True


class ConcreteHandlerB(Handler):
    def _handle(self, request):
        if 10 < request <= 20:
            print(f'Request {request} handled by ConcreteHandlerB')
            return True


class ConcreteHandlerC(Handler):
    def _handle(self, request):
        if 20 < request <= 30:
            print(f'Request {request} handled by ConcreteHandlerC')
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        print(f'End of chain, no handler for {request}')
        return True

if __name__ == '__main__':
    handler_chain = ConcreteHandlerA(ConcreteHandlerB(ConcreteHandlerC(DefaultHandler())))
    requests = [2, 5, 14, 22, 18, 3, 35]

    for request in requests:
        handler_chain.handle_request(request)
