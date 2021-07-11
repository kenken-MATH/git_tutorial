print('anpanman')

# print("アンパンマン'''")
# print('anpanman\' ')
#
# print('"anpanman \'\' "')
# print("fannnnn \"I don't known\" ")
# 改行は「\n」を使う
print('hell. \nHow are you?')

# スラッシュを文字列として扱うため、前に「r」をつける。
print(r'C:\name\name')

# 複数行の出力「""" """」
# 「\」で改行をなくす
print('###################')
print("""\
line1
line2
line3\
""")
print('###################')
#
print('Hi' * 3 + 'Mike.')

# 文字列の連結「＋」。なくてもOK
print('Py' + 'thon')
print('Py' 'thon')

# prefix = 'py'
# 変数だとエラーになる
# print(prefix +  'thon')
# 長い文字列を結合するときに使う。
s = ('aaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbb')
print(s)

############################################

# ■12文字列のインデックスとスライス

word = 'python'

print(word[0])  # 先頭の文字を出力 p
print(word[1])  # ２文字目の文字を出力 y
print(word[-1])  # 最後の文字を出力 n
print(word[0:2])  # 1~2文字目 py
print(word[2:5])  # 3~6文字目 thon
print('------------------------------')
print(word[0:2])  # 1~2文字目 py
print(word[:2])  # 1~2文字目 py
print(word[2:])  # 2文字目から最後まで py
# 文字列を書き換えたい場合
word = 'C' + word[1:]
print(word)
# 文字列の長さを出力関数
n = len(word)
print(n)

############################################
# NO.13 文字列のメソッド
s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')  # Myで始まっているか
print(is_start)

print('---------------------------')

print(s.find('Mike'))  # 左から何文字目か
print(s.rfind('Mike'))  # 最後のMikeが左から何文字目か
print(s.count('Mike'))  # Mikeが何個含まれているか
print(s.capitalize())  # 1文字目を大文字、他を小文字に変換する
print(s.title())  # 全てもワードの先頭を大文字に変換
print(s.upper())  # 全てを大文字にする
print(s.lower())  # 全てを小文字にする
print(s.replace('Mike', 'Nancy'))  # MikeをNancyに置換

# No14.文字列の代入
# ターミナルで実施。

###No17.リスト型##########
# ターミナルで実施。

###No18##########
# ターミナルで実施。

##No19.リストのメソッド###########

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r)
# 添字2
print(r.index(3))
# 添字7(インデックス３以降）
print(r.index(3, 3))

# ２．（「３」の個数）
print(r.count(3))

# if 100 in r:
#      print('exist5')
r.sort()
# 要素を昇順に並べ替える
print(r)
r.sort(reverse=True)
# 要素を降順に並べ替える
print(r)
r.reverse()
# 逆順に並べ替える
print(r)

s = 'My name is Mike.'
# 引数で指定したもので分割し、リストに格納
to_split = s.split(' ')
print(to_split)

# 引数のリストも要素を指定文字列で結合する
x = ' '.join(to_split)
print(x)

print(help(list))

# No.17リストのコピー

# ※注意リストの代入は参照渡し
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('i = ', i)
print('j = ', j)

# 回避策
x = [1, 2, 3, 4, 5]
y = x.copy()
# y = x[:]
y[0] = 100
print('y = ', y)
print('x = ', x)

#####
# 値渡し
X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(X)
print(Y)

# 参照渡し

X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(X)
print(Y)

# No.20リストの使いところ
seat = []
min = 0
max = 5
print(min <= len(seat) < max)
seat.append('a')
print(seat)
print(min <= len(seat) < max)
seat.append('a')
print(seat)
print(min <= len(seat) < max)
seat.append('a')
print(seat)
print(min <= len(seat) < max)
seat.append('a')
print(seat)
print(min <= len(seat) < max)
seat.append('a')
print(seat)
print(min <= len(seat) < max)
seat.pop(0)
print(seat)
print(min <= len(seat) < max)

# NO.21タプル型
# データを書き換えられたくない、読み込み専用などで使う
t = (1, 2, 3, 4, 5, 1)
print(t)
print(type(t))

print(t[0])
print(t[-1])
print(t[2:5])
print(t.index(1))
print(t.index(1, 1))
print(t.count(1))
print(help(list))
print(help(tuple))

t = ([1, 2, 3], [4, 5, 6])
print(t[0])
print(t[0][0])

t[0][0] = 100
# 宣言
t = 1, 2, 3
print(t)
# int型
t = 1
# タプル型
t = 1,
# 要素なしタプル型
t = ()
print(type(t))

new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple)
new_tuple = (1,) + (4, 5, 6)
print(new_tuple)

# NO.22タプルのアッパキング

num_tuple = (10, 20)

x, y = num_tuple
print(x, y)

x, y = (10, 20)
print(x, y)

x, y = 10, 20
print(x, y)

# 長くなると見にくい
a, b, c, d, e, f = 'mike', 'a', 'b', 'c', 'd', 'e'

# 値の入れ換え
i = 10
j = 20
tmp = i
i = j
j = tmp
print('i,j = ', i, j)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

# NO.23タプルの使いところ
# ３つの中から２つ選ぶゲーム、
# 選んだ答えが選択肢に追加されないようにする

chose_from_two = ('a', 'b', 'c')

answer = []
answer.append('a')
answer.append('c')
print(chose_from_two)
print(answer)

# chose_from_two.append('a')
# chose_from_two.append('c')


# NO.24辞書型

d = {'x': 10, 'y': 20}
print(d)
print(type(d))

print(d['x'])
print(d['y'])

d['x'] = 100
print(d)

d['x'] = 'X'
print(d)

d['z'] = 200
print(d)

d[1] = 1000
print(d)

dict1 = dict(a=10, b=20)
print(dict1)

dict2 = dict([('c', 30), ('d', 40)])
print(dict2)

# NO.24辞書型のメソッド
d = {'x': 10, 'y': 20}
print(d)
# キー
a = d.keys()
print(a)
# 値
b = d.values()
print(b)

d2 = {'x': 1000, 'j': 500}
print(d2)

d.update(d2)
print(d)

# バリューの取得
c = d['x']
print(c)

e = d.get('x')
print(d)

f = d.get('z')
# 戻り値None
print(e)

# 要素の削除
d.pop('x')
print(d)

# del使うときは気をつける
del d['y']
print(d)

d = dict(a=100, b=200)
print(d)

d.clear()
print(d)

d = dict(a=100, b=200)

# キーが辞書にあるか
h = 'a' in d
print(h)

# キーが辞書にあるか
i = 'o' in d
print(i)

# No.26辞書のコピー
print('No.26辞書のコピー')
x = {'a': 1}
y = x
y['a'] = 1000
print('xは', x)
print('yは', y)

# 参照渡しを避けるため
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print('xは', x)
print('yは', y)

# まとめ：辞書のコピーも参照渡しになるので、気をつける。

# 27.辞書の使いところ
print('27.辞書の使いところ')

L = [
    ['apple', 100],
    ['banana', 200],
    ['orange', 300]
]
# リストだと検索するのが面倒（キーがわかっていても値をすぐに取り出せない）


fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300
}

print(fruits['apple'])

# 28.集合型
a = {1, 2, 3, 4, 5, 5, 6, 6}
print(a)

print(type(a))

b = {2, 3, 3, 5, 5, 7}

print(b)
# 差集合
print(a - b)
# 差集合
print(b - a)
# 共通部分
print(a & b)
# 和集合
print(a | b)
# 共通部分の補集合 not &
print(a ^ b)

# 29.集合のメソッド

s = {1, 2, 3, 4, 5}
s.add(6)
print(s)
s.remove(6)
print(s)
s.clear()
# 空集合はの表記は辞書と区別するため、set()と表示される
print(s)

a = {}
print(type(a))

# 30.集合の使いところ
my_friends = {'A', 'B', 'C'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
# 型変換
kind = set(f)
print(kind)  # 一意的なものを使いたい場合など

print('XXXX')
"""
コメントです
コメントです
コメントです
コメントです

"""
print('XXXX')

# Apple price
some_value = 100

# 一行が長くなるとき

S = 'aaaaaaa' \
    + 'bbbbbbbb'
print(S)

x = (1 + 1 + 1 + 1 + 1 + 1
     + 1 + 1 + 1 + 1 + 1 + 1)
print(x)
"""
改行するときは、行末にバックスラッシュ\を入れるか
まるカッコ（）こ囲むか
"""

# 33.if文

x = 0

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

a, b = 5, 10

if a > 0:
    print('positive')
    if b > 0:
        print('b is positive')
# インデントを揃えることに注意

# 34.デバッガーを使って確認

# 35.比較演算子と論理演算子

a = 1
b = 1

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a > 0 and b > 0)
print(a > 0 or b > 0)

# 36.InとNotの使いところ

x = [1, 2, 3]

y = 1

if y in x:
    print('in')

if 100 not in x:
    print('not in')

# a = 1
# b = 2
#
# if not a == b:
#     print('NOt equal')
#
# if a != b:
#     print('NOt equal')

is_ok = True

if not is_ok:
    print('hello')

# 37.値が入っていない判定をするテクニック

# False: 0, 0.0, '', [], (), {}, set()
is_ok = [1, 3]
if is_ok:
    print('OK')
else:
    print('NO')

# 38.Noneを判定する場合

is_empty = None

if is_empty is not None:
    print('Noneです')

print(1 == True)
# print(1 is True)
print(None is None)

# 39.while文とcontinue文とbreak文

count = 0
# while count < 5:
#     print(count)
#     count += 1

while True:
    print('XXX')
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1

# 40.while else文

count = 0

while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')

# 41.input関数

# while True:
# 	word = input('Eenter:')
# 	num = int(word)
# 	if num == 100:
# 		break
# 	print('next')
# 42.for文とbreak文とcontinue文

some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

print('###')
# for i in some_list:
# 	print(i)

for s in 'abcde':
    print(s)

for word in ['my', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
    print(word)

# 43.for else文

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'bananaa':
        print('stop eating')
        break

    print(fruit)
else:
    print('I ate all')

# 44.range関数

# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in num_list:
# 	print(i)

# for i in range(2, 10, 3):
# 	print(i)

for i in range(10):
    print(i, 'hello')

for _ in range(10):
    print('hello')

# 45.enumerate関数
# i = 0
#
# for fruit in ['apple', 'banana', 'orange']:
# 	print(i, fruit)
# 	i += 1

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

# 46.zip関数

days = ['Mon', 'Tur', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# for i in range(len(days)):
# 	print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# 辞書をfor文で処理する

d = {'x': 100, 'y': 200}

print(d.items())
for k, v in d.items():
    print(k, ':', v)


# 48.関数定義

def say_something():
    s = 'hi'
    return s


result = say_something()
print(result)


def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


result = what_is_this('green')
result = what_is_this('red')
result = what_is_this('yellow')

print(result)


# 49.関数の引数と返り値の宣言

def add_num(a: int, b: int) -> int:
    return a + b


r = add_num('a', 'b')
print(r)


# 型が違ってもエラーを返さない

# 50.位置引数とキーワード引数とデフォルト引数

def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)


menu()
menu('chicken', drink='beer')


# 51.デフォルト引数で気をつけること

def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)
# 
# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)

r = test_func(100)
print(r)


r = test_func(100)
print(r)

# pythonはデフォルト引数で参照渡しのオブジェクトを設定しないほうがいい。

# 52.位置引数のタプル化


def say_something(word, *args):
	print('word=', word)
	for arg in args:
		print(arg)

say_something('hi', 'mike', 'nance')

# あまり使わない(タプル作ってアンパッキング)
# t = ('mike', 'nancy')
# say_something('hi', *t)

# 53.キーワード引数の辞書化

def menu(**kwargs):
	# print(kwargs)
	for k, v in kwargs.items():
		print(k, v)
# menu(entree='beef', drink='coffee')

d = {
	'entree': 'beef',
	'drink': 'ice coffe',
	'dessert': 'ice'
}

menu(**d)

print('########')

# 順序が守る必要がある
def menu(food, *args, **kwargs):
	print(food)
	print(args)
	print(kwargs)
menu('banana', 'apple', 'orange', entree='beef', drink = 'coffe')

# 54.Docstringsとは

def example_func(param1, param2):
	"""Example function with types documented in the docstring
	Args:
		parama1 (int): The first parameter.
		param2 (str): The second parameter.
	Returns:
		bool: The return value. Trune to success, False otherwise.
	"""
	print(param1)
	print(param2)
	return True
print(example_func.__doc__)
help(example_func)
# help(example_func.__doc__)


# 55.関数内関数

def outer(a, b):
	def plus(c, d):
		return c + d

	r1 = plus(a, b)
	r2 = plus(b, a)
	print(r1 + r2)


outer(1, 2)


# 56.クロージャー

# def outer(a, b):
#
# 	def inner():
# 		return a + b
#
# 	return inner
#
# f = outer(1, 2)
#
# print('####')
#
# # 後から実行したいときとかに使う
# r = f()
# print(r)

def circel_area_func(pi):
	def circle_area(radius):
		return pi * radius ** 2

	return circle_area


cal1 = circel_area_func(3.14)
cal2 = circel_area_func(3.141592)

# 後々用途によって使い分けたい場合に使う
# 難しい。。
print(cal1(10))
print(cal2(10))

# 57.デコレーター

def print_more(func):
	def wrapper(*args, **kwargs):
		print('func:', func.__name__)
		print('args',args)
		print('kwargs',kwargs)
		result = func(*args, **kwargs)
		print('result:', result)
		return result
	return wrapper

def print_info(func):
	def wrapper(*args, **kwargs):
		print('start')
		result = func(*args, **kwargs)
		print('end')
		return result
	return wrapper
@print_info
@print_more
def add_num(a, b):
	return a + b

r = add_num(10, 20)
print(r)

# 関数を引数として渡してる？？


# @print_info
# def sub_num(a, b):
# 	return a - b


# 関数の前後で何かをしたい場合にデコレーターを使う


# f = print_info(add_num)
# r = f(10, 20)
# print(r)

# print('start')
# r = add_num(10, 20)
# print('end')
#
# print(r)

# 58.ラムダ
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
	for word in words:
		print(func(word))

def sample_func(word):
	return word.capitalize()

def sample_func2(word):
	return word.lower()
# sample_func = lambda word: word.capitalize()

change_words(l, lambda  word: word.capitalize())

change_words(l, lambda  word: word.lower())


# 繰り返しオブジェクトに対して、その要素に関数を適応する
# 関数を引数とするものは、lambdaを使えばコード量が減る
# 書き方： lambda 引数 : 処理

# 59.ジェネレーター

# l = ['good morning', 'good afternoon', 'good night']
#
# for i in l:
# 	print(i)
#
# print('#########')
def counter(num=10):
	for _ in range(num):
		yield 'run'


def greeting():
	yield 'good morning'
	yield 'good afternoon'
	yield 'good night'

for g in greeting():
	print(g)

# 反復処理だが、ジェネレーターの場合、
print('#########')
g = greeting()
c = counter()

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

# 関数の中が全部実行するわけではなくて、一回一回実行ところが都合いい

# リスト内包表記

t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)
r = []

for i in t:
	if i % 2 == 0:
		r.append(i)

print(r)

r = [i for i in t if i % 2 == 0]
print(r)


"""
メリットは、メモリの消費。短く書ける.
"""
r = []
for i in t :
	for j in t2:
		r.append(i * j)

print(r)

r = [i*j for i in t for j in t2]
print(r)

"""
二重ループなどは内包表記で書くと逆に読みにくい
"""

# 61.辞書内包表記

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}

for x, y in zip(w, f):
	d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)


# 62.集合内包表記

s = set()

for i in range(10):
	if i % 2 == 0:
		s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)


# 63.ジェネレーター内包表記

def g():
	for i in range(10):
		yield i

g = g()

g = tuple(i for i in range(10) if i % 2 == 0)
print(type(g))
print(g)

"""
()だけだとジェネレーターになるので、
タプルにする場合はtuple()にする。
"""
for x in g:
	print(x)


# 64.名前空間とスコープ

"""
test test ######################33
"""
animal = 'cat'

def f():
	"""test func doc"""
	print(f.__name__)
	print(f.__doc__)

f()
print('global:', globals())

#flobals()でグローバル変数一覧を表示

# 65.例外処理

l = [1, 2, 3]
i = 5
try:
	l[0]
except IndexError as exc:
	print("don't worry:{}".format(exc))
except NameError as ex :
	print(ex)
except Exception as ex:
	print('other:{}'.format(ex))
else:
	print('done')
finally:
	print('clean up')

# else:例外なく処理されたら実行される
# finally:必ず実行される処理

# 66.独自例外の発生

# raise IndexError('test error')

class UppercaseError(Exception):
	pass

def check():
	words = {'APPLE', 'orange', 'banana'}
	for word in words:
		if word.isupper():
			raise ValueError(word)

try:
	check()
except ValueError as exc:
	print('This is my fault. go next.')


import  lesson_package.utils as u

r = u.say_twice('hello')
print(r)

# gitチュートリアル









































































