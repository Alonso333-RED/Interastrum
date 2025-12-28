from abc import ABC, abstractmethod

class Astro(ABC):

    def interact(self, tipo: str, other):
        if tipo not in self.interactions:
            raise ValueError(f"Interacción '{tipo}' no soportada")
        self.interactions[tipo](other)

    @property
    @abstractmethod
    def interactions(self) -> dict:
        """Retorna un dict {nombre: función}"""
        pass