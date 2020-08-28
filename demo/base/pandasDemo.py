import numpy as np, pandas as pd


def demo1():
    arr1 = np.arange(10)
    print(arr1)
    print(type(arr1))
    s1 = pd.Series(arr1)
    print(s1)
    print(type(s1))


def demo2():
    dict = {'a': 10, 'b': 20, "c": 30, 'd': 40, 'e': 50}
    s2 = pd.Series(dict)
    print(s2)
    print(type(s2))


def demo3():
    arr2 = np.array(np.arange(12)).reshape(4, 3)
    print(arr2)
    print(type(arr2))
    df1 = pd.DataFrame(arr2)
    print(df1)
    print(type(df1))


def demo4():
    dic2 = {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8],
            'c': [9, 10, 11, 12], 'd': [13, 14, 15, 16]}
    print(dic2)
    df2 = pd.DataFrame(dic2)
    print(df2)
    print(type(df2))


def demo5():
    dic3 = {'one': {'a': 1, 'b': 2, 'c': 3, 'd': 4},
            'two': {'a': 5, 'b': 6, 'c': 7, 'd': 8},
            'three': {'a': 9, 'b': 10, 'c': 11, 'd': 12}}
    df3 = pd.DataFrame(dic3)
    print(df3)
    print(type(df3))
    print()


def demo6():
    s4 = pd.Series(np.array([1, 1, 2, 3, 5, 8]))
    print(s4.index)
    s4.index = ['a', 'b', 'c', 'd', 'e', 'f']
    print(s4)


def demo7():
    s5 = pd.Series(np.array([10, 15, 20, 30, 55, 80]))
    s5.index = ['a', 'b', 'c', 'd', 'e', 'f']
    s6 = pd.Series(np.array([12, 11, 13, 15, 14, 16]))
    s6.index = ['a', 'b', 'c', 'd', 'e', 'f']
    print(s5 + s6)
    print(s5 / s6)


def readCsv():
    student = pd.io.parsers.read_csv('G:/test/test.csv')


def demo8():
    np.random.seed(1234)
    d1 = pd.Series(2 * np.random.normal(size=100) + 3)
    d2 = np.random.f(2, 4, size=100)
    d3 = np.random.randint(1, 100, size=100)
    print(d1.min())
    print(d1.max())
    print(d1.idxmax())
    print(d1.idxmin())
    print(d1.quantile())

    print(d1.sum)




if __name__ == '__main__':
    demo8()

