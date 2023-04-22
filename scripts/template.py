from abc import ABC, abstractmethod

class AlgorithmTemplate(ABC):

    def run(self):
        self.step_one()
        self.step_two()
        self.step_three()

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    @abstractmethod
    def step_three(self):
        pass

class Algorithm1(AlgorithmTemplate):

    def step_one(self):
        print("Running step 1 for Algorithm 1")

    def step_two(self):
        print("Running step 2 for Algorithm 1")

    def step_three(self):
        print("Running step 3 for Algorithm 1")

class Algorithm2(AlgorithmTemplate):

    def step_one(self):
        print("Running step 1 for Algorithm 2")

    def step_two(self):
        print("Running step 2 for Algorithm 2")

    def step_three(self):
        print("Running step 3 for Algorithm 2")

algorithm1 = Algorithm1()
algorithm1.run()

algorithm2 = Algorithm2()
algorithm2.run()
