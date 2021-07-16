from threading import *
from terminal import *
import listener
cmd = '' 

if __name__ == '__main__':
    #Terminal   
    terminal = Terminal()
    terminal_thread = Thread(target = terminal.cmdloop,)
    terminal_thread.start
    #Web
    print("Starting the C2 Server")
    listener.run()
