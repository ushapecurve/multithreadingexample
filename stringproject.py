from threading import Thread

my_string = 'This is the string we shall be woking on today'

class StringReader(Thread):
    
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name 
        
    def run(self):
        for i in my_string[::1]:
            print('%s thread is running: %s' % (self.name, i ))

sreader1 = StringReader('Thread #1')
sreader1.start()
sreader1 = StringReader('Thread #1')
sreader1.start()