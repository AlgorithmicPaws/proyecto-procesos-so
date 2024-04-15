import threading
import time
import random

NUM_PHILOSOPHERS = 5

# Semáforos para cada tenedor
forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

# Función que simula el comportamiento de un filósofo
def philosopher(id):
    left_fork = forks[id]
    right_fork = forks[(id + 1) % NUM_PHILOSOPHERS]

    while True:
        # El filósofo piensa
        print(f'Filósofo {id} está pensando.')
        time.sleep(random.uniform(1, 3))

        # El filósofo quiere comer
        print(f'Filósofo {id} quiere comer.')

        # Toma el tenedor izquierdo
        left_fork.acquire()
        print(f'Filósofo {id} toma el tenedor izquierdo.')

        # Toma el tenedor derecho
        right_fork.acquire()
        print(f'Filósofo {id} toma el tenedor derecho.')

        # El filósofo come
        print(f'Filósofo {id} está comiendo.')
        time.sleep(random.uniform(2, 4))

        # Suelta los tenedores
        left_fork.release()
        right_fork.release()
        print(f'Filósofo {id} suelta los tenedores.')

# Creamos e iniciamos los threads para cada filósofo
philosopher_threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(NUM_PHILOSOPHERS)]
for thread in philosopher_threads:
    thread.start()

# Esperamos a que todos los threads terminen
for thread in philosopher_threads:
    thread.join()
