# led.py - Versión 1: Encender LED
from machine import Pin
import time
# El LED integrado suele estar en el GPIO 2
led = Pin(2, Pin.OUT)
print("Encendiendo el LED...")
led.value(1) # 1 es encendido, 0 es apagado