# An Example of Python Multiprocessing Module

```python
import random
from multiprocessing import Process, Queue
from Queue import Empty
import time

class Worker(Process):

  def __init__(self, work_queue, result_queue):

      # base class initialization
      Process.__init__(self)

      # job management stuff
      self.work_queue = work_queue
      self.result_queue = result_queue
      self.kill_received = False

  def run(self):
      while not self.kill_received:

          # get a task
          try:
              job = self.work_queue.get_nowait()
          except Empty:
              break

          # the actual processing
          print("Starting " + str(job) + " ...")
          delay = random.randrange(1,3)
          time.sleep(delay)

          # store the result
          self.result_queue.put(delay)

if __name__ == "__main__":

  num_jobs = 20
  num_processes=8

  # run
  # load up work queue
  work_queue = Queue()
  for job in range(num_jobs):
      work_queue.put(job)

  # create a queue to pass to workers to store the results
  result_queue = Queue()

  # spawn workers
  processes = [Worker(work_queue, result_queue) for i in range(num_processes)]
  for p in processes:
      p.start()
  # collect the results off the queue
  results = []
  for i in range(num_jobs):
      print(result_queue.get())
  for p in processes:
      p.join()
```