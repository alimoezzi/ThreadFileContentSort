import os
import threading
import numpy as np
from createRandomFile import createRandomIntFile


def sortIntFile(filenames: list):
    for filename in filenames:
        lines = []
        with open(filename, 'rt') as file:
            lines = list(file.readlines())
        lines.sort(key=lambda x: int(x.split('\n')[0]))
        with  open(filename, 'wt') as file:
            file.write(''.join(lines))
            file.flush()

        print(f'\nThread {threading.currentThread().getName()} exiting')


if __name__ == '__main__':
    createRandomIntFile()
    print('Random integer files created.')
    os.system('pause')
    n = input("Enter number of workers: ")
    l = [i.path for i in os.scandir('intFiles/') if '.keep' not in i.path]
    for i in np.array_split(l, int(n)):
        try:
            t = threading.Thread(target=sortIntFile, args=(i,), name=f'sort {i}')
            print(f'Thread {t.getName()} about to start')
            t.start()
        except Exception as e:
            print(e)
            os.system('pause')
