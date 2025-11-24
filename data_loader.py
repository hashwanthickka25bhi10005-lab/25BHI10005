class User:
    def _init_(self, name, age):
        self.name = name
        self.age = age
        self.history = []

    def add_record(self, record):
        self.history.append(record)

    def get_history(self):
        return self.history
