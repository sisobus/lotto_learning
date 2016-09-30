#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import csv
import random

def get_winner_info(last_time=721):
    d = [ {} for i in xrange(1024) ]
    input_filename = 'Datagod_645_Win.txt'
    with open(input_filename,'r') as fp:
        lines = fp.read().strip().split('\n')[1:]
    for line in lines:
        cols = line.split(',')
        lucky_time = int(cols[0].strip())
        lucky_date = cols[1].strip()
        year = int(lucky_date.split('-')[0])
        mon = int(lucky_date.split('-')[1])
        day = int(lucky_date.split('-')[2])
        a1 = int(cols[12])
        a2 = int(cols[13])
        a3 = int(cols[14])
        a4 = int(cols[15])
        a5 = int(cols[16])
        a6 = int(cols[17])
        a7 = int(cols[18])
        d[lucky_time]['id'] = int(lucky_time)
        d[lucky_time]['year'] = year
        d[lucky_time]['mon'] = mon
        d[lucky_time]['day'] = day
        d[lucky_time]['a1'] = a1
        d[lucky_time]['a2'] = a2
        d[lucky_time]['a3'] = a3
        d[lucky_time]['a4'] = a4
        d[lucky_time]['a5'] = a5
        d[lucky_time]['a6'] = a6
        d[lucky_time]['a7'] = a7
        d[lucky_time]['label'] = 1
    cnt = [0 for i in xrange(55)]
    for i in xrange(1,last_time+1):
        cnt[d[i]['a1']] += 1
        cnt[d[i]['a2']] += 1
        cnt[d[i]['a3']] += 1
        cnt[d[i]['a4']] += 1
        cnt[d[i]['a5']] += 1
        cnt[d[i]['a6']] += 1
        cnt[d[i]['a7']] += 1
        for j in xrange(1,46):
            d[i]['cnt_'+str(j)] = cnt[j]
    return d

def write_info_to_file(datas,filename='datas.csv'):
    with open(filename,'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['year','mon','day','a1','a2','a3','a4','a5','a6','a7']+['cnt_%d'%i for i in xrange(1,46)]+['label'])
        for data in datas:
            cur_cnt = []
            for i in xrange(1,46):
                cur_cnt.append(str(data['cnt_%d'%i]))
            writer.writerow([str(data['year']),str(data['mon']),str(data['day']),str(data['a1']),str(data['a2']),str(data['a3']),str(data['a4']),str(data['a5']),str(data['a6']),str(data['a7'])]+cur_cnt+[str(data['label'])])
   
def gen_random_7():
    ret = set()
    while len(ret) < 7:
        ret.add(random.randint(1,45))
    return ret

def gen_new_data_with_data(data):
    new_data = {}
    new_data['id'] = data['id']
    new_data['year'] = data['year']
    new_data['mon'] = data['mon']
    new_data['day'] = data['day']
    new_data['label'] = 0
    for i in xrange(1,46):
        new_data['cnt_%d'%i] = data['cnt_%d'%i]
    r = list(gen_random_7())
    r.sort()
    while r[0] == data['a1'] and r[1] == data['a2'] and r[2] == data['a3'] and r[3] == data['a4'] and r[4] == data['a5'] and r[5] == data['a6'] and r[6] == data['a7']:
        r = list(gen_random_7()).sort()
    new_data['a1'] = r[0]
    new_data['a2'] = r[1]
    new_data['a3'] = r[2]
    new_data['a4'] = r[3]
    new_data['a5'] = r[4]
    new_data['a6'] = r[5]
    new_data['a7'] = r[6]
    return new_data

if __name__ == '__main__':
    last_time = 721
    gen_cnt = 100

    d = get_winner_info(last_time)
    datas = []
    for i in xrange(1,last_time+1):
        print i
        datas.append(d[i])
        for j in xrange(gen_cnt):
            datas.append(gen_new_data_with_data(d[i]))
    write_info_to_file(datas)
#    datas = []
#    for i in xrange(1,10):
#        datas.append(d[i])
