from threading import Thread
import time

my_string = 'This is the string we shall be woking on today'

class StringReader1(Thread):
    
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name 
        
    def run(self):
        for i in my_string[0::2]:
            print('%s thread is running: %s \n' % (self.name, i ))
            time.sleep(0.5)
            

class StringReader2(Thread):
    
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name 
        
    def run(self):
        for i in my_string[1::2]:
            print('%s thread is running: %s \n' % (self.name, i ))
            time.sleep(0.5)

sreader1 = StringReader1('Thread #1')
sreader2 = StringReader2('Thread #2')
sreader1.start()
sreader2.start()