import os

def gen():
    print("")



def menuju(txt):
    f = open(f"db/{txt}",'r')
    f1= f.readlines()
    f.close()
    baris = 0
#txt = input("enter: ")
    for i in f1:
        if i.find(txt) != -1:
            break
        else:
            baris += 1
    #print(baris)
    return baris


def tautan(file):
    try:
        f = open(f"db/{file}", "r")
        isi = f.readlines()
        f.close()
        #l = line
        judul = isi[0]
        return judul.split('-')[1]
    except FileNotFoundError:
        print("Wrong file or file path")
        #import os
    #os.system("clear")

    #else:
    #    break
