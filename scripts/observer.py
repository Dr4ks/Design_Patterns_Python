class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(*args, **kwargs)


class Observer:
    def update(self, *args, **kwargs):
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self.notify(self._state)


class ConcreteObserverA(Observer):
    def update(self, state):
        print(f"Observer A received the state {state}")


class ConcreteObserverB(Observer):
    def update(self, state):
        print(f"Observer B received the state {state}")


subject = ConcreteSubject()
observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.attach(observer_a)
subject.attach(observer_b)

subject.state = "state 1"
subject.state = "state 2"

subject.detach(observer_b)

subject.state = "state 3"
