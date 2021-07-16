from cmd import Cmd
import main 

class Terminal (Cmd):
    prompt = 'HackGodybj > '

    def default(self, args):
        main.cmd = args
        