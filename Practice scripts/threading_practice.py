import threading
import time

num_threads = 5
def thread_msg(msg):
    global num_threads
    num_threads -= 1
    print(f'Message from thread {msg}')
    
while num_threads > 0:
    print(f'This is thread number {num_threads}')
    threading.Thread(target=thread_msg(f'This is thread number {num_threads}')).start()
    time.sleep(5)
    
    
    




'''
Threads are streams that can be scheduled by the operating system and can be executed
across a single core concurrently, or in parallel across multiple cores. Threads are a similar
concept to processes: they are also code in execution. The main difference between the
two is that threads are executed within a process, and processes share resources among
themselves, such as memory.

'''