import threading
import time
import random

# Tamaño máximo del búfer
BUFFER_SIZE = 5

# Lista que actuará como el búfer compartido
buffer = []
# Semáforos para controlar el acceso al búfer
mutex = threading.Semaphore(1)
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)

# Función del productor
def producer():
    global buffer
    while True:
        # Simula la producción de un producto
        time.sleep(random.uniform(0.5, 1))
        item = random.randint(1, 100)
        empty.acquire()  # Espera a que haya espacio en el búfer
        mutex.acquire()  # Obtiene acceso exclusivo al búfer
        buffer.append(item)  # Agrega el producto al búfer
        print(f'Productor produce {item}. Búfer: {buffer}')
        mutex.release()  # Libera el acceso exclusivo al búfer
        full.release()  # Avisa al consumidor que hay un nuevo producto

# Función del consumidor
def consumer():
    global buffer
    while True:
        full.acquire()  # Espera a que haya productos disponibles
        mutex.acquire()  # Obtiene acceso exclusivo al búfer
        item = buffer.pop(0)  # Extrae el producto del búfer
        print(f'Consumidor consume {item}. Búfer: {buffer}')
        mutex.release()  # Libera el acceso exclusivo al búfer
        empty.release()  # Avisa al productor que hay espacio disponible

# Creamos los threads para el productor y el consumidor
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Iniciamos los threads
producer_thread.start()
consumer_thread.start()

# Esperamos a que los threads terminen
producer_thread.join()
consumer_thread.join()
