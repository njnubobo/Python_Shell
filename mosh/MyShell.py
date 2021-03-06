import sys
import shlex
import os

SHELL_STATUS_RUN = 1
SHELL_STATUS_STOP = 0

def shell_loop():
    status = SHELL_STATUS_RUN
    while status == SHELL_STATUS_RUN:
        # Display a command prompt
        sys.stdout.write('> ')
        sys.stdout.flush()
        # Read command input
        cmd = sys.stdin.readline()
        # Tokenize the command input
        cmd_tokens = tokenize(cmd)
        # Execute the command and retrieve new status
        status = execute(cmd_tokens)

def tokenize(string):
    return shlex.split(string)

def execute(cmd_tokens):
    # Fork a child shell process
    # If the current process is a child process, it's 'pid' is set to '0'
    # else the current process is a parent process and the value of 'pid'
    # is the process id of its child process
    pid = os.fork()
    if pid == 0:
        # Child process
        # Replace the child process with the program called with exec
        os.execvp(cmd_tokens[0], cmd_tokens)
    elif pid > 0:
        # Parent process
        while True:
            # Wait response status from its child process (identified with pid)
            wpid, status = os.waitpid(pid, 0)
            # Finish waiting if its child process exits normally
            # or is terminated by a signal
            if os.WIFEXITED(status) or os.WIFSIGNALED(status):
                break
    return SHELL_STATUS_RUN


def main():
    shell_loop()

if __name__ == "__main__":
    if __name__ == '__main__':
        main()
