'''
��ҽӴ���python����̵�һ�����͵��������£�����ִ������Ҳû���κ����⡣
import multiprocessing

def f(x):
    return x*x

def go():
    pool = multiprocessing.Pool(processes=4)            
    #result = pool.apply_async(self.f, [10])     
    #print result.get(timeout=1)           
    print pool.map(f, range(10))


if __name__== '__main__' :
    go()
���ǣ�һ��������class���������ʾ���󡣳���ͽ�����£�
����
import multiprocessing

class someClass(object):
    def __init__(self):
        pass

    def f(self, x):
        return x*x

    def go(self):
        pool = multiprocessing.Pool(processes=4)            
        #result = pool.apply_async(self.f, [10])     
        #print result.get(timeout=1)           
        print pool.map(self.f, range(10))

�����
PicklingError: Can't pickle <type 'instancemethod'>: attribute lookup __builtin__.instancemethod failed
������ʲô���������
лл


'''

#coding: utf-8
import multiprocessing
import logging

def create_logger(i):
    print i

class CreateLogger(object):
    def __init__(self, func):
        self.func = func

if __name__ == '__main__':
    ilist = range(10)

    cl = CreateLogger(create_logger)
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.map(cl.func, ilist)

    print "hello------------>"