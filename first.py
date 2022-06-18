# a=[int(x) for x in input('enter list of numbers').split( )]
# m=list(filter(lambda x:(x%2==0),a))
# m=list(map(lambda x:(x%2==0),a))
# n=list(filter(lambda x:(x%2!=0),a))
# n=list(map(lambda x:(x%2!=0),a))
# print('even',m)
# print('odd',n)

# a=[int(x) for x in input('enter the list of values').split()]
# a=['2','9','7']
# m=list(map(int,a))
# print(m)
# l=list(map(lambda x:(x**2),a))
# print(l)

'''lambda reduce'''
# from functools import*
# list=[float(x) for x in input('enter values').split( )]
# list=[1,2,3,6,5,4,7,89,9,5,5,56]
# w=reduce(lambda x,y:x+y,list)
# w=reduce(lambda x,y:x-y,list)
# w=reduce(lambda x,y:y-x,list)
# print(w)

'''global and local variable'''
# a=100
# def pre():
#   
    # a=10
    # b=52
    # print('local',a)
    # print('local',b)
# print('global', a)
# pre()
# print('global',a)

'''===================='''

# a=500
# def pre():
#     global a,b
    # a=10
    # b=52
    # print('local',a)
    # print('local',b)
# print('global',a)
# print('global',a)
# print('global',a)
# print('global',a)
# pre()
# print('global',a)
# print('global',a)
# print('global',a)
# print(b)  


# c=200
# def fn():
    # global c
    # c=20
    # print(c)
# print(c)
# fn()
# print(c)
a=3.5
print(int(a))