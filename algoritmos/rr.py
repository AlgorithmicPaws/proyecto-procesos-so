from collections import deque

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def round_robin(processes, time_quantum):
    ready_queue = deque(processes)
    current_time = 0
    completed_processes = []

    while ready_queue:
        process = ready_queue.popleft()
        start_time = max(current_time, process.arrival_time)
        execution_time = min(time_quantum, process.remaining_time)
        current_time = start_time + execution_time
        process.remaining_time -= execution_time

        if process.remaining_time > 0:
            ready_queue.append(process)
        else:
            completed_processes.append((process.pid, start_time, current_time))

    return completed_processes

def simulate_processes(process_data, time_quantum):
    processes = []
    for pid, arrival_time, burst_time in process_data:
        process = Process(pid, arrival_time, burst_time)
        processes.append(process)
    
    completed_processes = round_robin(processes, time_quantum)
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
    time_quantum = 3

    simulate_processes(process_data, time_quantum)
