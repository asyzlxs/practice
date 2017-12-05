# coding=utf-8
# import unittest

from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split


class Test():
    def __init__(self):
        pass

    def test_pd(self):
        df_train = pd.read_csv('../data/Breast-Cancer/breast-cancer-train.csv')
        df_test = pd.read_csv('../data/Breast-Cancer/breast-cancer-test.csv')
        df_test_negative = df_test.loc[df_test['Type'] == 0][['Clump Thickness', 'Cell Size']]
        df_test_positive = df_test.loc[df_test['Type'] == 1][['Clump Thickness', 'Cell Size']]
        # print len(df_test_negative), len(df_test_positive)
        plt.scatter(df_test_negative['Clump Thickness'], df_test_negative['Cell Size'], marker='o', s=200, c='red')
        plt.scatter(df_test_positive['Clump Thickness'], df_test_positive['Cell Size'], marker='x', s=150, c='black')
        plt.xlabel('Clump Thickness')
        plt.ylabel('Cell Size')
        plt.show()

    def test_load_digits(self):
        digits = load_digits()
        # print digits.data.shape
        x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)
        print y_train.shape


    def test01(self):
        iris = datasets.load_iris()
        digits = datasets.load_digits()
        for i in enumerate(iris):
            print i
        print len(iris), len(digits)

    def test02(self):
        print "hello word!"


if __name__ == '__main__':
    a = Test()
    a.test_load_digits()
    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(Test("test_pd"))
    # suite.addTest(Test("test02"))
    # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
