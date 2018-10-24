import signal
import os
import time


def do_exit(sig, stack):
    raise SystemExit('Exiting')


# This one ignores SIGINT (i.e. the 'Ctrl+C')
# In plain words,
#   yo, 'ctrl+c'! ur ignored!
signal.signal(signal.SIGINT, signal.SIG_IGN)

# Actually, u can term this by any means (except the 'Ctrl+C')
# For this line,
#   it corresponds to 'kill -USR1 THE_PID'
signal.signal(signal.SIGUSR1, do_exit)

print('My PID :', os.getpid())

signal.pause()
