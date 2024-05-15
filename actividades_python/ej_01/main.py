from gpiozero import LED, Button
from signal import pause

# Importamos las clases LED y Button de la biblioteca gpiozero.
# También importamos la función pause de signal para pausar la ejecución.

led = LED(26)
button = Button(18)

# Creamos objetos LED y Button asignándoles los pines GPIO correspondientes.

button.when_pressed = led.on
button.when_released = led.off

# Configuramos el comportamiento del LED cuando se presiona y se suelta el botón.

pause()
