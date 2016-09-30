#-*- coding:utf-8 -*-
import tensorflow as tf
import numpy as np
from tensorflow.python.platform import gfile
import csv
import collections
import random

Dataset = collections.namedtuple('Dataset', ['data', 'target'])
def load_csvfile(filename,target_dtype,target_column=-1):
    with gfile.Open(filename) as csv_file:
        data_file = csv.reader(csv_file)
        data, target = [], []
        for row in data_file:
            target.append(row.pop(target_column))
            data.append(np.asarray(row, dtype=target_dtype))
    target = np.array(target, dtype=target_dtype)
    data = np.array(data)
    return Dataset(data=data, target=target)

def gen_random_7():
    ret = set()
    while len(ret) < 7:
        ret.add(random.randint(1,45))
    return ret

def gen_new_lotto():
    year = 2016
    mon = 9
    day = 30
    a = list(gen_random_7())
    a.sort()
    cnt = [133,116,112,122,115,109,116,120,87,111,115,108,122,117,111,107,121,109,110,130,104,90,101,111,113,117,131,99,98,101,115,99,121,123,110,104,122,108,114,127,95,103,127,114,109]
    return [year,mon,day]+a+cnt

if __name__ == '__main__':
    train_filename = 'data/datas_72K.csv'
    training_set = load_csvfile(train_filename,target_dtype=np.int)
    print training_set.data
    x_train, y_train = training_set.data, training_set.target

    classifier = tf.contrib.learn.DNNClassifier(hidden_units=[55,30,10], n_classes=2)
    classifier.fit(x=x_train, y=y_train, steps=200)

    for i in xrange(100000):
        print i
        new_lotto = np.array([gen_new_lotto()],dtype=int)
        y = classifier.predict(new_lotto)
        if y[0] == 1:
            print new_lotto[3:10]
        
