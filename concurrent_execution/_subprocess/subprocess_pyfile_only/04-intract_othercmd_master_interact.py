import io
import subprocess

# For future ref, the link is right here
#   https://pymotw.com/3/subprocess/index.html#interacting-with-another-command

print('One line at a time:')

proc = subprocess.Popen(
    'python3 *slave*',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)

stdin = io.TextIOWrapper(
    proc.stdin,
    encoding='utf-8',
    line_buffering=True,
)

stdout = io.TextIOWrapper(
    proc.stdout,
    encoding='utf-8',
)

for i in range(5):
    line = '{}\n'.format(i)
    stdin.write(line)
    output = stdout.readline()
    print(output.rstrip())

remainder = proc.communicate()[0].decode('utf-8')
print(remainder)

print('\n------------\n')

print('All output at once:')

proc = subprocess.Popen(
    'python3 *slave*',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)

stdin = io.TextIOWrapper(
    proc.stdin,
    encoding='utf-8',
)

for i in range(5):
    line = '{}\n'.format(i)
    stdin.write(line)

stdin.flush()

output = proc.communicate()[0].decode('utf-8')
print(output)
