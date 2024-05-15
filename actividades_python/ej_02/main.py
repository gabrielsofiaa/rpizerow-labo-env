from gpiozero import LED
from time import sleep

# Importamos la clase LED para controlar los LEDs, y sleep de time para pausar la ejecución.

led_rojo = LED(19)
led_azul = LED(26)
led_verde = LED(13)

# Creamos objetos para los LEDs rojo, azul y verde, asignándoles los pines GPIO correspondientes.

while True:
	led_rojo.on()
	sleep(1)
	led_rojo.off()
	led_azul.on()
	sleep(0.5)
	led_azul.off()
	led_verde.on()
	sleep(0.25)
	led_verde.off()

# Encendemos el LED rojo, esperamos 1 segundo, lo apagamos,
# luego encendemos el LED azul, esperamos 0.5 segundos, y así sucesivamente en un ciclo continuo.
