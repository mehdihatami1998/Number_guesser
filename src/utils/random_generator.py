import random

def random_generator(start, end):
    return random.randint(start, end)


if __name__ == '__main__':
    print(random_generator(1, 100))