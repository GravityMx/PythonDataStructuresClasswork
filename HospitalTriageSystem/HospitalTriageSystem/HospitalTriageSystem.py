


import heapq
import itertools

class TriageSystem:
    _arrival_counter = itertools.count() 

    def __init__(self):
        self._heap = []  # Holds tuples 

    def add_patient(self, name, severity):
        if not name:
            print("Error: Name cannot be empty.")
            return
        if severity < 1 or severity > 5:
            print("Error: Severity must be between 1 and 5.")
            return

        arrival = next(TriageSystem._arrival_counter)
        heapq.heappush(self._heap, (-severity, arrival, name))

    def process_next(self):
        if not self._heap:
            print("No patients to process.")
            return None
        sev_neg, arrival, name = heapq.heappop(self._heap)
        severity = -sev_neg
        return name, severity

    def peek_next(self):
        if not self._heap:
            print("No patients in queue.")
            return None
        sev_neg, arrival, name = self._heap[0]
        severity = -sev_neg
        return name, severity

    def is_empty(self):
        return len(self._heap) == 0

    def size(self):
        return len(self._heap)

    def clear(self):
        self._heap = []



  
   

# Testing the system
if __name__ == "__main__":
    ts = TriageSystem()

    # Provided test set
    patients = [
        ("Sofia", 5), ("Bob", 2), ("Charlie", 4), ("Diana", 3),
        ("Eli", 1), ("Tom", 4), ("Alice", 5), ("Rachel", 4)
    ]

    for name, sev in patients:
        ts.add_patient(name, sev)

    print("Processing patients:")
    while not ts.is_empty():
        result = ts.process_next()
        if result:
            name, severity = result
            print("Now treating:", name, "(Severity", severity, ")")

    # tie-break example
    patients2 = [
        ("Schumer", 5), ("Grassly", 5), ("McConnell", 5), ("Pelosi", 5)
    ]

    for name, sev in patients2:
        ts.add_patient(name, sev)


    while not ts.is_empty():
        result = ts.process_next()
        if result:
            name, severity = result
            print("Now treating:", name, "(Severity", severity, ")")