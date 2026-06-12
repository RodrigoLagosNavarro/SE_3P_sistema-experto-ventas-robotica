# Preguntas utilizadas por el sistema:
#
# nivel:
# - principiante
# - intermedio
# - avanzado
#
# presupuesto:
# - bajo
# - medio
# - alto
#
# proyecto:
# - educacion
# - iot
# - automatizacion
# - robotica_movil
# - vision_artificial
#
# categoria:
# - controlador
# - sensor
# - actuador
# - kit


productos = [

    # ========================================================
    # CONTROLADORES
    # ========================================================

    {
        "nombre": "Arduino Uno",
        "categoria": "controlador",
        "nivel": "principiante",
        "presupuesto": "bajo",
        "proyecto": "educacion",
        "justificacion": "Ideal para aprender programación y electrónica."
    },

    {
        "nombre": "Arduino Mega",
        "categoria": "controlador",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "automatizacion",
        "justificacion": "Mayor cantidad de entradas y salidas para proyectos complejos."
    },

    {
        "nombre": "ESP32",
        "categoria": "controlador",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "iot",
        "justificacion": "Incluye WiFi y Bluetooth integrados."
    },

    {
        "nombre": "ESP8266",
        "categoria": "controlador",
        "nivel": "intermedio",
        "presupuesto": "bajo",
        "proyecto": "iot",
        "justificacion": "Excelente opción económica para IoT."
    },

    {
        "nombre": "Raspberry Pi 5",
        "categoria": "controlador",
        "nivel": "avanzado",
        "presupuesto": "alto",
        "proyecto": "vision_artificial",
        "justificacion": "Gran capacidad de procesamiento para visión artificial."
    },

    # ========================================================
    # SENSORES
    # ========================================================

    {
        "nombre": "HC-SR04",
        "categoria": "sensor",
        "nivel": "principiante",
        "presupuesto": "bajo",
        "proyecto": "robotica_movil",
        "justificacion": "Sensor ultrasónico para medir distancias."
    },

    {
        "nombre": "DHT11",
        "categoria": "sensor",
        "nivel": "principiante",
        "presupuesto": "bajo",
        "proyecto": "iot",
        "justificacion": "Sensor básico de temperatura y humedad."
    },

    {
        "nombre": "DHT22",
        "categoria": "sensor",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "iot",
        "justificacion": "Mayor precisión que el DHT11."
    },

    {
        "nombre": "MQ-2",
        "categoria": "sensor",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "automatizacion",
        "justificacion": "Detecta humo y gases inflamables."
    },

    {
        "nombre": "PIR HC-SR501",
        "categoria": "sensor",
        "nivel": "principiante",
        "presupuesto": "bajo",
        "proyecto": "automatizacion",
        "justificacion": "Sensor de movimiento infrarrojo."
    },

    {
        "nombre": "Camara Raspberry Pi",
        "categoria": "sensor",
        "nivel": "avanzado",
        "presupuesto": "alto",
        "proyecto": "vision_artificial",
        "justificacion": "Captura imágenes para procesamiento visual."
    },

    # ========================================================
    # ACTUADORES
    # ========================================================

    {
        "nombre": "Servo SG90",
        "categoria": "actuador",
        "nivel": "principiante",
        "presupuesto": "bajo",
        "proyecto": "robotica_movil",
        "justificacion": "Servo económico para proyectos básicos."
    },

    {
        "nombre": "Servo MG996R",
        "categoria": "actuador",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "robotica_movil",
        "justificacion": "Mayor torque para aplicaciones exigentes."
    },

    {
        "nombre": "Motor DC TT",
        "categoria": "actuador",
        "nivel": "principiante",
        "presupuesto": "bajo",
        "proyecto": "robotica_movil",
        "justificacion": "Motor común para robots educativos."
    },

    {
        "nombre": "Motor Paso a Paso 28BYJ-48",
        "categoria": "actuador",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "automatizacion",
        "justificacion": "Permite movimientos precisos."
    },

    {
        "nombre": "Driver L298N",
        "categoria": "actuador",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "robotica_movil",
        "justificacion": "Controlador para motores DC."
    },

    # ========================================================
    # KITS
    # ========================================================

    {
        "nombre": "Kit Arduino Starter",
        "categoria": "kit",
        "nivel": "principiante",
        "presupuesto": "medio",
        "proyecto": "educacion",
        "justificacion": "Incluye componentes básicos para comenzar."
    },

    {
        "nombre": "Kit Elegoo UNO",
        "categoria": "kit",
        "nivel": "principiante",
        "presupuesto": "medio",
        "proyecto": "educacion",
        "justificacion": "Kit completo para prácticas educativas."
    },

    {
        "nombre": "Kit ESP32 IoT",
        "categoria": "kit",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "iot",
        "justificacion": "Incluye hardware para proyectos conectados."
    },

    {
        "nombre": "Kit Raspberry Pi",
        "categoria": "kit",
        "nivel": "avanzado",
        "presupuesto": "alto",
        "proyecto": "vision_artificial",
        "justificacion": "Ideal para sistemas inteligentes."
    }
]


# ============================================================
# REGLAS DE INFERENCIA
# ============================================================

reglas = [

    {
        "id": "R1",
        "nivel": "principiante",
        "presupuesto": "bajo",
        "proyecto": "educacion",
        "categoria": "controlador",
        "producto": "Arduino Uno",
        "explicacion": "Se recomienda Arduino Uno porque es económico y adecuado para usuarios que están iniciando."
    },

    {
        "id": "R2",
        "nivel": "principiante",
        "presupuesto": "medio",
        "proyecto": "educacion",
        "categoria": "kit",
        "producto": "Kit Arduino Starter",
        "explicacion": "El kit incluye componentes y ejemplos prácticos ideales para aprendizaje."
    },

    {
        "id": "R3",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "iot",
        "categoria": "controlador",
        "producto": "ESP32",
        "explicacion": "ESP32 incorpora conectividad WiFi y Bluetooth para proyectos IoT."
    },

    {
        "id": "R4",
        "nivel": "intermedio",
        "presupuesto": "bajo",
        "proyecto": "iot",
        "categoria": "controlador",
        "producto": "ESP8266",
        "explicacion": "ESP8266 es una alternativa económica para sistemas conectados."
    },

    {
        "id": "R5",
        "nivel": "avanzado",
        "presupuesto": "alto",
        "proyecto": "vision_artificial",
        "categoria": "controlador",
        "producto": "Raspberry Pi 5",
        "explicacion": "Raspberry Pi 5 ofrece potencia suficiente para procesamiento de imágenes."
    },

    {
        "id": "R6",
        "nivel": "principiante",
        "presupuesto": "bajo",
        "proyecto": "robotica_movil",
        "categoria": "sensor",
        "producto": "HC-SR04",
        "explicacion": "Permite detectar obstáculos y medir distancias en robots móviles."
    },

    {
        "id": "R7",
        "nivel": "principiante",
        "presupuesto": "bajo",
        "proyecto": "robotica_movil",
        "categoria": "actuador",
        "producto": "Servo SG90",
        "explicacion": "Es un actuador económico y sencillo para proyectos educativos."
    },

    {
        "id": "R8",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "robotica_movil",
        "categoria": "actuador",
        "producto": "Servo MG996R",
        "explicacion": "Ofrece mayor torque para aplicaciones más exigentes."
    },

    {
        "id": "R9",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "automatizacion",
        "categoria": "sensor",
        "producto": "MQ-2",
        "explicacion": "Permite detectar gases y humo en sistemas automatizados."
    },

    {
        "id": "R10",
        "nivel": "avanzado",
        "presupuesto": "alto",
        "proyecto": "vision_artificial",
        "categoria": "kit",
        "producto": "Kit Raspberry Pi",
        "explicacion": "Incluye componentes necesarios para sistemas inteligentes avanzados."
    },

    {
        "id": "R11",
        "nivel": "avanzado",
        "presupuesto": "alto",
        "proyecto": "vision_artificial",
        "categoria": "sensor",
        "producto": "Camara Raspberry Pi",
        "explicacion": "Permite capturar imágenes para aplicaciones de visión artificial."
    },

    {
        "id": "R12",
        "nivel": "principiante",
        "presupuesto": "bajo",
        "proyecto": "iot",
        "categoria": "sensor",
        "producto": "DHT11",
        "explicacion": "Sensor sencillo y económico para monitoreo ambiental."
    },

    {
        "id": "R13",
        "nivel": "principiante",
        "presupuesto": "bajo",
        "proyecto": "automatizacion",
        "categoria": "sensor",
        "producto": "PIR HC-SR501",
        "explicacion": "Ideal para detectar movimiento en sistemas automáticos."
    }

,
    {
        "id": "R14",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "iot",
        "categoria": "sensor",
        "producto": "DHT22",
        "explicacion": "Ofrece mayor precisión para monitoreo ambiental en proyectos IoT."
    },

    {
        "id": "R15",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "automatizacion",
        "categoria": "controlador",
        "producto": "Arduino Mega",
        "explicacion": "Cuenta con múltiples entradas y salidas para automatización."
    },

    {
        "id": "R16",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "automatizacion",
        "categoria": "actuador",
        "producto": "Motor Paso a Paso 28BYJ-48",
        "explicacion": "Permite movimientos precisos en sistemas automatizados."
    },

    {
        "id": "R17",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "robotica_movil",
        "categoria": "controlador",
        "producto": "Arduino Mega",
        "explicacion": "Permite controlar múltiples sensores y actuadores en robots."
    },

    {
        "id": "R18",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "robotica_movil",
        "categoria": "sensor",
        "producto": "HC-SR04",
        "explicacion": "Facilita la detección de obstáculos en robots móviles."
    },

    {
        "id": "R19",
        "nivel": "intermedio",
        "presupuesto": "medio",
        "proyecto": "robotica_movil",
        "categoria": "actuador",
        "producto": "Driver L298N",
        "explicacion": "Permite controlar motores DC en plataformas móviles."
    },

    {
        "id": "R20",
        "nivel": "avanzado",
        "presupuesto": "alto",
        "proyecto": "vision_artificial",
        "categoria": "controlador",
        "producto": "Raspberry Pi 5",
        "explicacion": "Ideal para procesamiento avanzado de imágenes."
    }
]

