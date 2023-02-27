# Запишите в файл file_01.txt строку
# "Hello world"

def my_func():
    print('hello word')


with open('file_01.txt', 'w') as f:
    f.write('Hello word\n')
