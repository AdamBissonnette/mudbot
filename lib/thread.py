import louie
import threading
import time

class Thread(threading.Thread):
    stopping = False
    kill_signal = "mudbot.killall"
    stop_signal = "mudbot.stop"
    timeout = 0.2

    def __init__(self):
        super().__init__()
        louie.connect(self.stop, signal=self.kill_signal)
        louie.connect(self.stop, signal=self.stop_signal)

    def stop(self):
        self.stopping = True
        print ("stopped {}".format(self))

    def run(self):
        while not self.stopping:
            self.do_action()
            time.sleep(self.timeout)
    
    def do_action(self):
        pass