import time
import subprocess
import sys
import random
import os

env = os.environ.copy()
env['PYTHONUNBUFFERED'] = '1'

def exec_cmd(cmd):
    while True:
        print(f'starting process "{cmd}"')
        p = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            env=env,
        )
        while p.poll() is None:
            line = p.stdout.readline().decode('utf-8')
            sys.stdout.write(line)
            sys.stdout.flush()
        p.wait()
        rand_time = random.randint(1, 10)
        print(f'process ended. restarting in {rand_time} seconds...')
        time.sleep(rand_time)

if __name__ == '__main__':
    exec_cmd(' '.join(sys.argv[1:]))
