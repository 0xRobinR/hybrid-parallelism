from contractor.config import MIN_WORKERS, MAX_WORKERS


class Contractor:
    def __init__(self, min_workers=MIN_WORKERS, max_workers=MAX_WORKERS):
        self.workers = []
        self.min_workers = min_workers
        self.max_workers = max_workers

    def handle_worker_connection(self, worker_socket):
        """
        handles worker connection and update the list of workers
        """
        self.workers.append(worker_socket)

    def start_work(self):
        """
        starts the work of the AI contractor
        """
        pass

    def stop_work(self):
        """
        stops the work of the AI contractor
        """
        pass

    def host_process(self):
        """
        broadcast the work to the workers, and collect the results
        """
        pass

    def get_model(self):
        """
        returns the model
        """
        pass
