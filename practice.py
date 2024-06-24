def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


def make_negative2(number):
    return number * -1 if number > 0 else number


def make_negative(number):
    return abs(number) * -1


def positive_sum(arr):
    sum = 0
    for num in arr:
        sum += num if num > 0 else 0
    return sum


txt = "Hello World"[::-1]


def get_count(sentence):
    count = 0
    vowels = ('a', 'e', 'i', 'o', 'u')
    for s in sentence:
        if s in vowels:
            count += 1
    return count


def disemvowel(string_):
    string_ = string_.translate(str.maketrans('', '', 'aeiou'))
    return string_


def remove_char(s):
    return s[1:-1]


def square_sum(numbers):
    return sum(num ** 2 for num in numbers)


def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum


def spin_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    return " ".join(words)


def spin_words2(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    if len(names) == 1:
        return f'{names[0]} likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    if len(names) >= 4:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


def likes2(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names) - 2)


print(likes2(['Peter']))


def slice(a, b):
    start = ord(a)
    end = ord(b)
    if start == end:
        return a
    else:
        return ''.join(chr(start + i) for i in range(end - start + 1))


def slice2(a, b): start, end = ord(a), ord(b); return chr(start) + (chr(start + 1) if start != ord(b) else '')

print(slice("A", "X"))
