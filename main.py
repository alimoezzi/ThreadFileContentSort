import os
import threading


def sortIntFile(filename: str):
    lines = []
    with open(filename, 'rt') as file:
        lines = list(file.readlines())
    lines.sort(key=lambda x: int(x.split('\n')[0]))
    with  open(filename, 'wt') as file:
        file.write(''.join(lines))
        file.flush()


if __name__ == '__main__':
    for i in os.scandir('intFiles/'):
        try:
            t = threading.Thread(target=sortIntFile, args=(i.path,), name=f'sort {i.path}')
            t.start()
        except Exception as e:
            print(e)
            os.system('pause')
