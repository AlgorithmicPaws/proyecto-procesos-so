import heapq
import multiprocessing
import time

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    def __lt__(self, other):
        return self.burst_time < other.burst_time

def shortest_job_first(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Ordenar los procesos por tiempo de llegada
    ready_queue = []
    current_time = 0
    completed_processes = []

    while processes or ready_queue:
        while processes and processes[0].arrival_time <= current_time:
            process = processes.pop(0)
            heapq.heappush(ready_queue, process)

        if ready_queue:
            process = heapq.heappop(ready_queue)
            start_time = max(current_time, process.arrival_time)
            current_time = start_time + process.burst_time
            completed_processes.append((process.pid, start_time, current_time))
        else:
            current_time += 1

    return completed_processes

def simulate_processes(process_data):
    processes = []
    for pid, arrival_time, burst_time in process_data:
        process = Process(pid, arrival_time, burst_time)
        processes.append(process)
    
    completed_processes = shortest_job_first(processes)
    for pid, start_time, end_time in completed_processes:
        print(f"Proceso {pid}: Tiempo de inicio: {start_time}, Tiempo de finalización: {end_time}")

if __name__ == "__main__":
    process_data = [
        (1, 0, 5),  # (pid, arrival_time, burst_time)
        (2, 2, 3),
        (3, 4, 1),
        (4, 6, 4),
        (5, 8, 2)
    ]

    simulate_processes(process_data)
