""" 
Archivo    : calculadora.py 
Descripción: Contexto del patrón Strategy. CalculadoraDescuento mantiene 
             una referencia a la estrategia activa y delega el cálculo a 
             ella. Cambiar la estrategia en tiempo de ejecución no requiere 
             modificar esta clase. 
Patrón GoF : Strategy — Context (Comportamiento) 
Curso      : Diseño de Patrones (UCA-IEP026) 
Autores    : Noe Herrera — 13762@uca.edu.mx — 13762 
             Noe Herrera — 13762@uca.edu.mx — 13762 
Fecha      : 23 de Julio del 2026 
"""
from src.descuento.estrategias import EstrategiaDescuento, SinDescuento 
 
class CalculadoraDescuento: 
    def __init__(self): 
        self._estrategia: EstrategiaDescuento = SinDescuento() 
 
    def set_estrategia(self, estrategia: EstrategiaDescuento): 
        self._estrategia = estrategia 
 
    def aplicar(self, subtotal: float) -> dict: 
        descuento = self._estrategia.calcular(subtotal) 
        return { 
             "subtotal":    subtotal, 
             "descuento":   descuento, 
             "total":       subtotal - descuento, 
             "descripcion": self._estrategia.descripcion(), 
         } 
        pass 