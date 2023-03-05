# Создайте класс WordIterable, который в конструкторе принимает строку (текст) и итерируется по словам. Для простоты
# можно считать что текст это набор слов, разделённый только пробелами (никаких знаков препинания). То есть для
# разбиения можно использовать функцию split.

class WordIterable:
    def __init__(self, user_string):
        self.user_string = user_string
        self.counter = 0

    def __iter__(self):
        self.word = self.user_string.split()
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > len(self.word):
            raise StopIteration()

        return self.word[self.counter - 1]


if __name__ == "__main__":
    user_string = 'мама мыла раму'
    for w in WordIterable(user_string):
        print(w)

    assert ['мама', 'мыла', 'раму'] == [w for w in WordIterable('мама мыла раму')]
    assert not ['1', '2', 'm'] == [w for w in WordIterable('мама мыла раму')]
    assert not ['mama', 'мыла', 'раму'] == [w for w in WordIterable('мама мыла раму')]
    assert not ['мама', 'my1a', 'раму'] == [w for w in WordIterable('мама мыла раму')]
