import signal
import time
import threading


def signal_handler(num, stack):
    print(time.ctime(), 'Alarm in', threading.currentThread().name)


signal.signal(signal.SIGALRM, signal_handler)


def use_alarm():
    t_name = threading.currentThread().name

    print(time.ctime(), 'Setting alarm in', t_name)
    signal.alarm(1)

    print(time.ctime(), 'Sleeping in', t_name)
    time.sleep(3)

    print(time.ctime(), 'Done with sleep in', t_name)


# Starting a thread that will never receive the signal
alarm_thread = threading.Thread(
    target=use_alarm,
    name='alarm_thread',
)
alarm_thread.start()
time.sleep(0.1)


# Wait for the thread (nah, it will NOT)
print(time.ctime(), 'Waiting for', alarm_thread.name)
alarm_thread.join()

print(time.ctime(), 'Exiting normally')
