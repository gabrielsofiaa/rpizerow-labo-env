from gpiozero import LED, Buzzer
from time import sleep

# Declaración de componentes: LEDs y Zumbador

led_verde = LED(13)
led_rojo = LED(19)
led_azul = LED(26)
bzz = Buzzer(22)

while True:
    # Solicitamos al usuario que ingrese un comando
    res = input("Ingrese un comando (Sintaxis: comando.opcion): ")

    # Opciones de comando, con manejo de errores
    if res == "buzz.on":
        bzz.on()
    elif res == "buzz.off":
        bzz.off()
    elif res == "rgb.red":
        led_rojo.on()
    elif res == "rgb.blue":
        led_azul.on()
    elif res == "rgb.green":
        led_verde.on()
        led_azul.off()
        led_rojo.off()
    else:
        # Manejo de errores para comandos incorrectos
        print("Error: Comando no reconocido")
