import threading
import be
import time


def change__avatar(file_name_number):
    thres = []
    number = file_name_number[0]
    file_name = file_name_number[1]
    for i in range(int(number)):
        thres.append(threading.Thread(target=be.change_avatar,args={file_name,}))
    for thresd in thres:
        thresd.start()
        time.sleep(5)
    for thresd in thres:
        thresd.join()
