# led.py - Versión 2: Parpadeo (Blink)
from machine import Pin
import time
led = Pin(2, Pin.OUT)
print("Iniciando secuencia de parpadeo...")
while True:
led.value(1)
time.sleep(0.5) # Espera medio segundo
led.value(0)
time.sleep(0.5)