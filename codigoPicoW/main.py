import network
import urequests
import time
from machine import ADC


# Wi-Fi
SSID = "NOME REDE"
PASSWORD = "SENHA REDE"
    
# Conecta no Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    time.sleep(1)

print("Conectado:", wifi.ifconfig())

# Sensor interno
sensor = ADC(4)
factor = 3.3 / 65535

URL = "http://SEU_IP:8000/api/temperatura/"


# ===== WIFI =====
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Conectando ao Wi-Fi...")
while not wlan.isconnected():
    time.sleep(1)

print("Conectado:", wlan.ifconfig())

# ===== SENSOR DE TEMPERATURA =====
sensor = ADC(4)
conversion_factor = 3.3 / 65535

def ler_temperatura():
    leitura = sensor.read_u16()
    tensao = leitura * conversion_factor
    temperatura = 27 - (tensao - 0.706) / 0.001721
    return round(temperatura, 2)

# ===== LOOP =====
while True:
    try:
        temp = ler_temperatura()
        print("Temperatura:", temp)

        resposta = urequests.post(
            URL,
            json={"valor": temp},
            headers={"Content-Type": "application/json"}
        )

        print("Enviado:", resposta.status_code)
        resposta.close()

    except Exception as e:
        print("Erro:", e)

    time.sleep(5)  # envia a cada 5 segundos

