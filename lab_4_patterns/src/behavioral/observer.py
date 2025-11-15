# Наблюдатель - поведенческий
from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, order_id: str, status: str):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, order_id: str, status: str):
        for observer in self._observers:
            observer.update(order_id, status)

class OrderNotifier(Subject):
    def __init__(self):
        super().__init__()

    def order_status_changed(self, order_id: str, new_status: str):
        print(f"Order {order_id} status changed to {new_status}")
        self.notify(order_id, new_status)
