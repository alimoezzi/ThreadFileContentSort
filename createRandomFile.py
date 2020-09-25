import random


def createRandomIntFile():
    for i in range(10):
        with open(f'intFiles/{i}', 'wt') as file:
            a = [str(random.randint(0,10000)) for i in range(100)]
            file.write('\n'.join(a))
            file.flush()

if __name__ == '__main__':
    createRandomIntFile()
