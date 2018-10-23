import sys

# For future ref, the link is right here
#   https://pymotw.com/3/subprocess/index.html#interacting-with-another-command

sys.stderr.write('Mr. Repeat: starting\n')
sys.stderr.flush()

while True:
    next_line = sys.stdin.readline()
    sys.stderr.flush()

    if not next_line:
        break

    sys.stdout.write(next_line)
    sys.stdout.flush()

sys.stderr.write('Mr. Repeat: exiting\n')
sys.stderr.flush()
