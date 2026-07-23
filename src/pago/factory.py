""" 
Archivo    : factory.py 
Descripción: Implementa el patrón Abstract Factory para la creación de 
             pasarelas de pago. PasarelaProduccion crea objetos reales; 
             PasarelaPruebas crea mocks que no realizan cargos. La función 
             obtener_pasarela() selecciona la familia según la variable 
             de entorno ENTORNO. 
Patrón GoF : Abstract Factory (Creacional) 
Curso      : Diseño de Patrones (UCA-IEP026) 
Autores    : Noe Herrera — 13762@uca.edu.mx — 13762 
             Noe Herrera — 13762@uca.edu.mx — 13762 
Fecha      : 23 de Julio del 2026 
""" 
import os 
from abc import ABC, abstractmethod 
from src.pago.pago import Pago, PagoTarjeta, PagoEfectivo 
 
class PagoMock(Pago): 
    """Producto mock — nunca realiza cargos reales""" 
    def __init__(self, etiqueta: str = "mock"): 
        self._etiqueta = etiqueta 
 
    def procesar(self, monto: float) -> bool: 
        print(f"[MOCK-{self._etiqueta.upper()}] Simulando ${monto:.2f} — sin cargo real") 
        return True 
 
    def tipo(self): return f"mock-{self._etiqueta}" 
 
class PasarelaPago(ABC): 
    @abstractmethod 
    def crear_pago_tarjeta(self, numero: str) -> Pago: pass 
 
    @abstractmethod 
    def crear_pago_efectivo(self) -> Pago: pass 
 
class PasarelaProduccion(PasarelaPago): 
    def crear_pago_tarjeta(self, numero: str) -> Pago: 
        return PagoTarjeta(numero) 
        pass 
 
    def crear_pago_efectivo(self) -> Pago: 
        return PagoEfectivo() 
        pass 
 
class PasarelaPruebas(PasarelaPago): 
    def crear_pago_tarjeta(self, numero: str) -> Pago: 
        return PagoMock("tarjeta") 
        pass 
 
    def crear_pago_efectivo(self) -> Pago: 
        return PagoMock("efectivo") 
        pass 
 
def obtener_pasarela() -> PasarelaPago: 
    entorno = os.getenv("ENTORNO", "produccion") 
    return PasarelaPruebas() if entorno == "pruebas" else PasarelaProduccion()