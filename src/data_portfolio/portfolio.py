from dataclasses import dataclass

from .datasets import N2V_BSD68


class Denoising():
    """
    """

    def __init__(self):	
        self._N2V_BSD64 = N2V_BSD68()
        self._N2V_SEM = None
        self._N2N_SEM = None
        self._RGB = None
        self._flywing = None
        self._DSB2018 = None

    @property
    def N2V_BSD64(self):
        return self._N2V_BSD64

    @property
    def N2V_SEM(self):
        return self._N2V_SEM
    
    @property
    def RGB(self):
        return self._RGB
    
    @property
    def flywing(self):
        return self._flywing
    

    @classmethod
    def list_datasets(cls) -> list[str]:
        return ["N2V_BSD", "SEM", "RGB", "flywing", 'DSB2018']  


@dataclass
class Portfolio():
    denoising: Denoising = Denoising()

    def __str__(self) -> str:
        return f"Portfolio: {self.denoising.list_datasets()}"
