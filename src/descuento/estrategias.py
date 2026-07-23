""" 
Archivo    : estrategias.py 
Descripción: Define la interfaz EstrategiaDescuento y sus implementaciones 
             concretas (SinDescuento, DescuentoPorVolumen, DescuentoCupon, 
             DescuentoVIP). Cada estrategia encapsula un algoritmo de cálculo 
             de descuento independiente y reemplazable en tiempo de ejecución. 
Patrón GoF : Strategy (Comportamiento) 
Curso      : Diseño de Patrones (UCA-IEP026) 
Autores    : Noe Herrera — 13762@uca.edu.mx — 13762 
             Noe Herrera — 13762@uca.edu.mx — 13762 
Fecha      : 23 de Julio del 2026 
"""
from abc import ABC, abstractmethod 
 
class EstrategiaDescuento(ABC): 
    @abstractmethod 
    def calcular(self, subtotal: float) -> float: pass 
 
    @abstractmethod 
    def descripcion(self) -> str: pass 
 
class SinDescuento(EstrategiaDescuento): 
    def calcular(self, subtotal: float) -> float: 
        return 0.0 
        pass 
    def descripcion(self): return "Sin descuento" 
 
class DescuentoPorVolumen(EstrategiaDescuento): 
    """10% si el subtotal supera $100""" 
    UMBRAL     = 100.0 
    PORCENTAJE = 0.10 
 
    def calcular(self, subtotal: float) -> float: 
        return subtotal * self.PORCENTAJE if subtotal > self.UMBRAL else 0.0 
        pass 
 
    def descripcion(self): 
        return f"{self.PORCENTAJE*100:.0f}% por volumen (> ${self.UMBRAL:.0f})" 
 
class DescuentoCupon(EstrategiaDescuento): 
    CUPONES_VALIDOS = {"PROMO10": 0.10, "VER20": 0.20, "DESC15": 0.15} 
 
    def __init__(self, codigo: str): 
        if codigo not in self.CUPONES_VALIDOS: 
             raise ValueError(f"Cupón inválido: '{codigo}'") 
        self._codigo = codigo 
        self._pct    = self.CUPONES_VALIDOS.get(codigo, 0.0) 
 
    def calcular(self, subtotal: float) -> float: 
        return subtotal * self._pct 
        pass 
 
    def descripcion(self): 
        return f"Cupón {self._codigo} ({self._pct*100:.0f}%)" 
 
class DescuentoVIP(EstrategiaDescuento): 
    """15% fijo para clientes VIP""" 
    def calcular(self, subtotal: float) -> float: 
        return subtotal * 0.15 
        pass 
 
    def descripcion(self): return "15% cliente VIP" 