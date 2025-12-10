import timeit
t1 = timeit.timeit('a=[\'a\']*100; del a[0]', number=10000)
t2 = timeit.timeit('b=[\'b\']*100; b.pop(0)', number=10000)
t3 = timeit.timeit('c=[\'c\']*100; c.remove(\'c\')', number=10000)
t4 = timeit.timeit('d=[\'d\']*100; d[1:]', number=10000)
print("del : {:5.3f}".format(t1*1000), "msec.")
print("pop() : {:5.3f}".format(t2*1000), "msec.")
print("remove() : {:5.3f}".format(t3*1000), "msec.")
print("d[1:] : {:5.3f}".format(t4*1000), "msec.")