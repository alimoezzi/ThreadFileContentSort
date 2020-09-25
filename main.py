import os


def sortIntFile(filename: str):
    lines = []
    with open(filename, 'rt') as file:
        lines = list(file.readlines())
    lines = lines.sort(key=lambda x: int(x))
    with  open(filename, 'wt') as file:
        file.write('\n'.join(lines))
        file.flush()



if __name__ == '__main__':
    for i in os.scandir('intFiles/'):
        try:
            sortIntFile(i.path)
        except Exception as e:
            print(e)
            os.system('pause')
