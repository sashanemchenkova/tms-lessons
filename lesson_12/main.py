try:
    a, b = int(input()), int(input())
    print(a/b)
    print('OK')
except ZeroDivisionError as e:
    print('Error:', e)
except ValueError as e:
    print('Incorrect value:', e)
print('The end. Goodbye')
