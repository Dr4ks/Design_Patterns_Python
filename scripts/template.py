from abc import ABC, abstractmethod

# Abstract Class
class DataProcessor(ABC):
    def process_data(self):   # templateMethod()
        self.read_data()
        self.parse_data()
        self.analyze_data()
        self.display_results()

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def parse_data(self):
        pass

    @abstractmethod
    def analyze_data(self):
        pass

    def display_results(self):
        print("Displaying results...")

# Concrete Class1
class XMLDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from XML file...")

    def parse_data(self):
        print("Parsing XML data...")

    def analyze_data(self):
        print("Analyzing XML data...")

# Concrete Class2
class CSVDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from CSV file...")

    def parse_data(self):
        print("Parsing CSV data...")

    def analyze_data(self):
        print("Analyzing CSV data...")

# Client code
def client_code():
    xml_processor = XMLDataProcessor()
    csv_processor = CSVDataProcessor()

    print("Processing XML data:")
    xml_processor.process_data()

    print("\nProcessing CSV data:")
    csv_processor.process_data()

# Usage
client_code()


## Output
# Processing XML data:
# Reading data from XML file...
# Parsing XML data...
# Analyzing XML data...
# Displaying results...

# Processing CSV data:
# Reading data from CSV file...
# Parsing CSV data...
# Analyzing CSV data...
# Displaying results...