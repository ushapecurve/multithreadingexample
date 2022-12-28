import threading
import time

my_string = 'This is the string we shall be woking on today'

def read_string(input_string, starting_position, in_step):
    for letter in input_string[starting_position::in_step]:
        print('%s thread is running: %s \n' % (threading.currentThread().getName(),  letter ))
        time.sleep(0.5)
        

        

# read_string(my_string, 0, 2)
# print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
# read_string(my_string, 1, 2)

t1 = threading.Thread(target = read_string , name = 'Thread-1-', args=(my_string, 0, 2))
t2 = threading.Thread(target = read_string, name = 'Thread-2-', args=(my_string, 1, 2))
# only "MainThread thread is running:" not    'Thread-1-'   and        'Thread-2-'


t1.start()
t2.start() 
    