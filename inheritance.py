from abc import ABC, abstractmethod

class Base(ABC):
    def concrete_method(self) -> None:
        return self.abstract_method()
    
    @abstractmethod
    def abstract_method(self) -> None:
        raise NotImplementedError

class Sub(Base):
    def abstract_method(self) -> None:
        """Providing a concrete implementation for the 'abstract_method' from the Base class"""
        print("I'm a concrete implementation of the 'abstract_method' of Base")

sub = Sub()
sub.concrete_method()
# base = Base()
# base.abstract_method()