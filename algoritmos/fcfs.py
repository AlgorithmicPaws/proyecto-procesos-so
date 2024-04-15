class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def first_come_first_serve(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Ordenar los procesos por tiempo de llegada
    current_time = 0
    completed_processes = []

    for process in processes:
        start_time = max(current_time, process.arrival_time)
        current_time = start_time + process.burst_time
        completed_processes.append((process.pid, start_time, current_time))

    return completed_processes

def simulate_processes(process_data):
    processes = []
    for pid, arrival_time, burst_time in process_data:
        process = Process(pid, arrival_time, burst_time)
        processes.append(process)
    
    completed_processes = first_come_first_serve(processes)
    for pid, start_time, end_time in completed_processes:
        print(f"Proceso {pid}: Tiempo de inicio: {start_time}, Tiempo de finalización: {end_time}")

if __name__ == "__main__":
    process_data = [
        (1, 0, 8),  # (pid, arrival_time, burst_time)
        (2, 1, 4),
        (3, 2, 9),
        (4, 3, 5),
        (5, 4, 2)
    ]

    simulate_processes(process_data)
