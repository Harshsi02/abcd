# d='kk'
# print(d)

# def myfun():
#     print('welcome')
#     print('greetings from HDFC')

#myfun()

# def myfun(name):
#     print('welcome', name)
#     print('greetings from HDFC')
#
# myfun('dhoni')
# myfun(['a', 'b'])

# def myfun(name):
#     if type(name)==str:
#         print('welcome', name)
#     else:
#         print('')
#
# myfun('dhoni')
# myfun(36)
# myfun(['a', 'b'])

# def my_fun(name='dhoni', country='india'):
#     print('welcome', name, 'from', country)
#
# my_fun('kohli', 'pakistan')

# def my_fun(name='dhoni', country=None):
#      print('welcome', name, 'from', country)
#
# my_fun('kohli')

# def my_fun(*players):
#     print(players)
#
# my_fun('kohli')
# my_fun('kohli', 'dhoni')
# my_fun('kohli', 'dhoni', 'dravid')

# def my_fun(*players):
#     print(list(players))

# my_fun(kohli)
# my_fun('kohli', 'dhoni')
# my_fun('kohli', 'dhoni', 'dravid')

# def student_cgpa(mark1, mark2):
#     total = mark1 + mark2
#     return total
#
# output=student_cgpa(20,30)
# print(output)

# def student_cgpa(mark1, mark2, name):
#     total = mark1 + mark2
#     return total, name
#
# output=student_cgpa(20,30, 'dhoni')
# print(output)

# def student_cgpa(mark1, mark2, name):
#     total = mark1 + mark2
#     return total, name
#
# output, name=student_cgpa(20,30, 'dhoni')
# print(output, name)

# function scoping
# def fun():
#     var = 1000
#     print(var)
# fun()

# var=100
# def fun():
#     var = 1000
#     print(var)
# fun()

# var=10 # global variable
# def fun():
#     var = 100 #enclosed Variable
#     def new():
#         var=1000 #local variable
#         print(var)
#     new()
#
# fun()

# var=100
# def fun():
#     var=1000
#     print(var)
#
# print(var)
# fun()
# print(var)

# var = 100
# def fun():
#     global var
#     var = 1000
#     print(var)
#
# print(var)
# fun()
# print(var)

# var = 100
# def fun():
#     global var
#     var = 1000
#     print(var)
#     var=var+1000
#
# print(var)
# fun()
# print(var)

# n=0
# def fun():
#     global n
#     print('hello',n)
#     n=n+1
#     if n<100:
#        fun()
#
#
# fun()



# var=[1,2,3,4,5]
# var2=[i*i for i in var]
# print(var2)
#
# output=list(map(lambda x: x*x, var))
# print(output)


# Class topics
# class is basically to have a  structure for your code
# class generally means the collection of objets (anything that occupies memory)
# class is just a template or wrapper to keep the data inside
# chennai is a class and places in chennai are objects
# furniture is class and chair, tables are objects
# unbounded class (deprecated) and bounded class(constructor)


# # unbounded example
# class my_class:
#
#     def login(ip, pwd):
#         print(ip)
#         print(pwd)
#
#     def hostname(ip):
#         print(ip)
#
# my_obj = my_class #object reference
# my_obj.login('2.2.2.2', 123)
# my_obj.hostname('2.2.2.2')
#
# class my_class:
#
#     def login(ip, pwd):
#         print(ip)
#         print(pwd)
#
#     def hostname(ip):
#         print(ip)
#
# my_class.login('2.2.2.2', 123)
# my_class.hostname('2.2.2.2')
#
# #data that is supposed to get onto the function is not initialized in common place

# # bounded examples
# class my_class:
#
#     def __init__(self, ip, pwd):
#         self.a=ip
#         self.b=pwd
#
#     def login(self):
#         print(self.a)
#         print(self.b)
#
#     def hostname(self):
#         print(self.a)

# my_obj = my_class('2.2.2.2', 123)
# my_class is a constructor
# my_obj is a object reference (object instance-- single memory)
# every constructor that gets created will have one hidden object as first agrgument
# my_obj.login()
# my_obj.hostname()
# __init__ is the constructor
# means, whenever you need constructor, this init will be automatically created
# if we need the data to be initialized then we can use as
# self is nothing but a name given to the object reference which got created during constructor
# data that suppose to get passed onto the function is not initialized in common place

# class my_class:
#
#     def __init__(self, ip, pwd):
#         self.a=ip
#         self.b=pwd
#
#     def login(tata):
#         print(tata.a)
#         print(tata.b)
#
#     def hostname(tata2):
#         print(tata2.a)
#
# my_obj = my_class('2.2.2.2', 123)
# my_obj.login()
# my_obj.hostname()
#
# class myclass:
#
#     def fun(self):
#         print('welcome to my class')
#
# obj=myclass()
# obj.fun()
#
# class myclass:
#     def __init__(self):
#         print('welcome')
#
#     def fun(self):
#         print('welcome to my class')
#
# obj=myclass()
# obj.fun()


# class my_class:
#
#     def __init__(self, ip, pwd):
#         self.a=ip
#         self.b=pwd
#
#     def login(self, certificate):
#         print(self.a, certificate)
#         print(self.b)
#
#     def hostname(self):
#         print(self.a)
#
# my_obj = my_class('2.2.2.2', 123)
# my_obj.login('tt')

# # here 'certificate' is the argument which is only meant for the function 'login'

# class my_class:
#
#     def __init__(self, book, laptop):
#         self.book=book
#         self.laptop=laptop
#
#     def abjijeet(self, certificate):
#         print(self.book, certificate)
#         print(self.laptop)
#
#     def mohammed(self):
#         print(self.book)
#
# my_obj = my_class('2.2.2.2', 123)
# my_obj.abjijeet('tt')
# my_obj.mohammed()

# # access specifier -- public, private and protected

# class my_class:
#
#     def __init__(self, book, laptop):
#         self.book=book
#         self.laptop=laptop
#
#     def __abjijeet(self, certificate): # '__' makes the function private and cannot be accessed outside the class
#         print(self.book, certificate)
#         print(self.laptop)
#
#     def mohammed(self):
#         print(self.book)
#
# my_obj = my_class('2.2.2.2', 123)
# my_obj.abjijeet('tt')
# my_obj.mohammed()
#
# # the above code gives error as the function 'abjijeet' is private

# # single inheritance
# class my_class:
#
#     def __init__(self, book, laptop):
#         self.book=book
#         self.laptop=laptop
#
#     def abjijeet(self, certificate):
#         print(self.book, certificate)
#         print(self.laptop)
#
# class second_class(my_class):
#
#     def mohammed(self):
#         print(self.book)
#
# my_obj = second_class('2.2.2.2', 123)
# my_obj.abjijeet('tt')
# my_obj.mohammed()

# class parent:
#     # parent class method
#     def m1(self):
#         print('parent class method called...')
#
# class child(parent):
#
#     def __init__(self):
#         #child class constructor
#         print('child class object created')
#
#     def m2(self):
#         print('child class method called')
#
# # creating object of child class
# my_obj = child()
# my_obj.m1()
# my_obj.m2()

# we can also have init function in the child class also and can access the child class in the parent class as well
# class parent:
#
#     def m1(self):
#         print(self.age)
#
# class child(parent):
#
#     def __init__(self, age):
#         self.age = age
#
#     def m2(self):
#         print(self.age)
#
#
# my_obj = child(33)
# my_obj.m1()
# my_obj.m2()

# class rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# class square:
#     def __init__(self, length):
#         self.length = length
#
#     def area(self):
#         return self.length * self.length
#
#     def perimeter(self):
#         return 4 * self.length
#
# Square = square(4)
# a=Square.area()
# print(a)
# Rectangle = rectangle(2, 4)
# b=Rectangle.area()
# print(b)

# class A:
#     def __init__(self, age):
#        self.age=age
#     def fun(self):
#         print('hello')
#         print(self.age)
#     def new(self):
#         print(self.age)
# class B(A):
#     def __init__(self, rank):
#         self.rank=rank
#         super().__init__(self.rank)
# # 33 is passed to the parent class as well in the age variable
#     def fun(self):
#         print('hi')
#         print(self.rank)
#         print(self.age)
#
# b=B(33)
# b.fun()
# b.new()

# class A:
#     def fun(self):
#         print('A')
#
# class B(A):
#     def fun(self):
#         print('B')
#
# class C(A):
#     def fun(self):
#         print('C')
#
# class D(B,C):
#     def fun(self):
#         print('D')
#
# d=D()
# d.fun()

# class A:
#     def fun(self):
#         print('A')
#
# class B(A):
#     def fun(self):
#         print('B')
#
# class C(A):
#     def fun(self):
#         print('C')
#
# class D(B,C):
#     pass
#
# d=D()
# d.fun()

# class A:
#     def fun(self):
#         print('A')
#
# class B(A):
#     def fun(self):
#         print('B')
#
# class C(A):
#     def fun(self):
#         print('C')
#
# class D(C, B): # MRO -- Method Resolution Order
#     pass
#
# d=D()
# d.fun()

## Exception Handling
# try:
#     Var=10/0
#     print(Var)
# except:
#     print('sorry')

# try:
#     var = 'a'/0
#     print(var)
# except ZeroDivisionError as ex:
#     print(ex)
# except:
#     print('opps')

# try:
#     var = a/0
#     print(var)
# except ZeroDivisionError as ex:
#     print(ex)
# except TypeError as ex:
#     print(ex)
# except:
#     print('opps')

# try:
#     var = 10/'a'
#     print(var)
# except (ZeroDivisionError, TypeError) as ex:
#     print(ex)
# except:
#     print('oops')

# try:
#     var = 'a'/0
#     print(var)
#
# except Exception as ex:
#     print(ex)

# try:
#     var = 67/3
#     print(var)
# except Exception as ex:
#     print(ex)
# else:
#     print('else')
# finally:
#     print('finally')

# # finally will always get printed
# # and else will be printed when we will not get an exception

# try:
#     var = 10/0
#     print(var)
# except Exception as ex:
#     print(ex)
# else:
#     print('else')
# finally:
#     print('finally')

# user defined exception

# class MyError(Exception):
#     pass
#
# try:
#     var=10
#     if var>5:
#         raise MyError
#
# except MyError:
#     print('sorry')

# class MyError(Exception):
#     meaning='sorry'
#
# try:
#     var=10
#     if var>5:
#         raise MyError
#
# except MyError:
#     print(MyError.meaning)











