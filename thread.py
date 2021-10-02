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
def change__name(file_name_number_name):
    thres = []
    number = file_name_number_name[0]
    file_name = file_name_number_name[1]+';'+file_name_number_name[2]
    for i in range(int(number)):
        thres.append(threading.Thread(target=be.change_name,args={file_name,}))
    for thresd in thres:
        thresd.start()
        time.sleep(5)
    for thresd in thres:
        thresd.join()

def join_gr(file_name):
    thres = []
    number = file_name[0]
    link_gr = file_name[1]
    for i in range(int(number)):
        thres.append(threading.Thread(target=be.join__,args={link_gr,}))
    for thresd in thres:
        thresd.start()
        time.sleep(5)
    for thresd in thres:
        thresd.join()

def chat_ok(file_name):
    thres = []
    number = file_name[0]
    data = file_name[1]+'@h#1'+file_name[2]+'@h#1'+file_name[3]
    for i in range(int(number)):
        thres.append(threading.Thread(target=be.chat,args={data,}))
    for thresd in thres:
        thresd.start()
        time.sleep(5)
    for thresd in thres:
        thresd.join()