class Subject:
    def __init__(self):
        self._observers = [] # List to store observers
        
    def register(self, observer):
        self._observers.append(observer)
        
    def notify_all(self, message:str):
        for observer in self._observers:
            observer.notify(message)
            
class Observer:
    def notify(self, message:str):
        print(f"Observer received: {message}")
        

subject = Subject()
observer1 = Observer()
observer2 = Observer()


subject.register(observer1)
subject.register(observer2)

subject.notify_all("Hello, Observers!")