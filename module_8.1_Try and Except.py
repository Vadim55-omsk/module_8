def add_everything_up(a, b):
    try:
        return f'{a+b:.3f}'
    except:
        return f'{a}{b}'

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))






# print(f'{123.456 + 7:.3f}')

# pi = 3.141592
# print(f'{pi:.3f}')
# 3.142