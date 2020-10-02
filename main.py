import os
import threading
import numpy as np
from createRandomFile import createRandomIntFile
import multiprocessing as mul


def sortIntFile(filenames: list):
    for filename in filenames:
        lines = []
        with open(filename, 'rt') as file:
            lines = list(file.readlines())
        lines.sort(key=lambda x: int(x.split('\n')[0]))
        with  open(filename, 'wt') as file:
            file.write(''.join(lines))
            file.flush()

        print(f'\nWorker {threading.currentThread().getName()}@{mul.process.current_process()} exiting')


if __name__ == '__main__':
    createRandomIntFile()
    print('Random integer files created.')
    os.system('pause')
    n = input("Enter number of workers: ")
    o = input("Thread or process (1/0): ")
    l = [i.path for i in os.scandir('intFiles/') if '.keep' not in i.path]
    for i in np.array_split(l, int(n)):
        try:
            if o == '1':
                t = threading.Thread(target=sortIntFile, args=(i,), name=f'sort {i}')
                print(f'Worker {t.getName()} about to start')
                t.start()
            else:
                pool = mul.Pool(mul.cpu_count())
                results = pool.starmap(sortIntFile, [(i,)])
                pool.close()
        except Exception as e:
            print(e)
            os.system('pause')
