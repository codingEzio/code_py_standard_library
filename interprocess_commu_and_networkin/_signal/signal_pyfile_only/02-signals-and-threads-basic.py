import signal
import threading
import os
import time


def signal_handler(num, stack):
    print('Recv signal {} in {}'.format(
        num, threading.currentThread().name
    ))


signal.signal(signal.SIGUSR1, signal_handler)


def wait_for_signal():
    ''' 
    --- Quotes (from stdlib doc) --- 

    about `currentThread`
        "If the caller’s thread of control was not created, 
        a dummy thread obj with limited functionality is returned."

    about `signal.pause`
        "Cause the process to sleep until a signal is received; 
        the appropriate handler will then be called. Returns nothing."
    '''

    print('Waiting for signal in', threading.currentThread().name)
    signal.pause()
    print('Waiting (Already Done)')


# This thread will NOT receive the signal
recvr = threading.Thread(
    target=wait_for_signal,
    name='revr',
)
recvr.start()
time.sleep(0.1)


def send_signal():
    print('Sending signal in', threading.currentThread().name)
    os.kill(os.getpid(), signal.SIGUSR1)


sender = threading.Thread(target=send_signal, name='sender')
sender.start()
sender.join()

# This will NOT either. (In corrspd to the thread above)
print('Waiting for', recvr.name)
signal.alarm(2)
recvr.join()
