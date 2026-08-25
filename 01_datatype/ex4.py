a = "python"
print(a, type(a))


print("I'll be back")
print('I\'ll be back')


a = """
Hello
World
"""

print(a)

def func():
    """
    func() 함수에 대한 설명
    """


print(func.__doc__)



print("Hello" + "World")

print("Hello "*5)


print("Hello "+str(10))

print("10" + "2")
print(int("10") + int("2"))

name = "pororo"
age = 26



print(f"이름: {name}")
print(f"내년 나이: {age+1}")
print(f"{name.upper()}")


pi = 3.141592
print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789
print(f"{num:,}")
print(f"{num:15,d}")
print(f"{num:<15,d}")
print(f"{num:015,d}")