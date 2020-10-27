from multiprocessing import Process


def f(name):
    print(f"Hello {name}")


if __name__ == '__main__':
    p = Process(target=f, args=('roy',))
    p.start()
    p.join()
