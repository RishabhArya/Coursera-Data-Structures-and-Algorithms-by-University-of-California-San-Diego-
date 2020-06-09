# python3

import heapq


class Worker:
    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.size = len(self.jobs)
        assert m == self.size

    def write_response(self):
        for worker_id, start_time in self.result:
            print(worker_id, start_time)

    def assign_jobs(self):
        self.result = []
        self.worker_queue = [Worker(i) for i in range(self.num_workers)]

        for job in self.jobs:
            worker = heapq.heappop(self.worker_queue)

            self.result.append((worker.thread_id, worker.release_time))

            worker.release_time += job
            heapq.heappush(self.worker_queue, worker)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == "__main__":
    job_queue = JobQueue()
    job_queue.solve()
