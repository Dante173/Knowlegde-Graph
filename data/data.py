import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
import string


file = open("origin.txt",encoding='UTF-8')
entity_set = set()
relation_set = set()
date_set = set()
all_list = []
for line in file.readlines():
    four_tuple = line.split()

    if(len(four_tuple)!=4):
        print(four_tuple)
        if("Xinjiang" in four_tuple[0] or "Ningxia" in four_tuple[0]):
            entity_set.add(four_tuple[0]+" "+four_tuple[1])
            entity_set.add(four_tuple[2])
        else:
            entity_set.add(four_tuple[0])
            entity_set.add(four_tuple[1]+" "+four_tuple[2])
        relation_set.add(four_tuple[-2])
        date_set.add(four_tuple[-1])
    else:          
        entity_set.add(four_tuple[0])
        entity_set.add(four_tuple[1])
        relation_set.add(four_tuple[2])
        date_set.add(four_tuple[3])
        all_list.append(line)
X_train, X_test, Y_train, Y_test = train_test_split(
    all_list, all_list, test_size=0.30, random_state=42)

file.close()

train_file = open("train.txt","w",encoding='UTF-8')
for i in range(len(X_train)):
    train_file.write(X_train[i])
train_file.close()

test_file = open("test.txt","w",encoding='UTF-8')
for i in range(len(X_test)):
    test_file.write(X_test[i])
test_file.close()

entity_file = open("entity2id.txt","w",encoding='UTF-8')
for i in range(len(entity_set)):
    st = entity_set.pop()
    entity_file.write(st+"\t"+str(i)+"\n")
entity_file.close()

relation_file = open("relation2id.txt","w",encoding='UTF-8')
for i in range(len(relation_set)):
    st = relation_set.pop()
    relation_file.write(st+"\t"+str(i)+"\n")
relation_file.close()

date_file = open("date2id.txt","w",encoding='UTF-8')
for i in range(len(date_set)):
    st = date_set.pop()
    date_file.write(st+"\t"+str(i)+"\n")
date_file.close()

