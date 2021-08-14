import os
import pickle
data = {
   'a': [1, 2.0, 3, 4+6j],
   'b': ("character string", b"byte string"),
    'c': {None, True, False}
    }


with open('data.pickle', 'wb') as f:
   pickle.dump(data, f)


with open('data.pickle', 'rb') as f:
   data_new = pickle.load(f)
print(data_new)



pp = (os.path.join('..', 'C:/Users/benep/PycharmProjects/pythonProject/SF_mod_27', 'my_cookies.txt'))
# # здесь символ / уже повернут для Опер Сист MAC
cookies = open(pp)

print (cookies.read()) # вывод текста из файла
print (pp) # показан путь до файла

with open(r'my_cookies.txt', encoding='utf8') as cookiesfile:
    cookies = cookiesfile.read()

print(cookies)

with open('my_cookies.txt', 'rb') as cookiesfile:
    cookies = pickle.load(cookiesfile)
print(cookies)

# {'c': {False, True, None}, 'a': [1, 2.0, 3, (4+6j)], 'b': ('character string', b'byte string')}
