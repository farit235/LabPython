import pandas as pd
from collections import Counter

INDEX_COL = 0
SURVIVED_COL = "Survived"
PCLASS_COL = "Pclass"
NAME_COL = "Name"
SEX_COL = "Sex"
AGE_COL = "Age"
SIBSP_COL = "SibSp"
PARCH_COL = "Parch"
TICKET_COL = "Ticket"
FARE_COL = "Fare"
CABIN_COL = "Cabin"
EMBARKED_COL = "Embarked"

# new
AGE_GROUP_COL = "AgeGroup"
SIBSP_GROUP_COL = "SibSpGroup"
PARCH_GROUP_COL = "ParchGroup"
FARE_GROUP_COL = "FareGroup"

data = pd.read_csv('train.csv')
print(data)

# 1
group_survived = data.groupby([PCLASS_COL, SEX_COL, SURVIVED_COL])
print(group_survived.size())
print()

# 2
group_allnums = data.groupby([SEX_COL, PCLASS_COL, AGE_COL, TICKET_COL, FARE_COL])
print(group_allnums.size())
print()

# 3
group_port = data.groupby([EMBARKED_COL, SURVIVED_COL])
print(group_port.size().unstack())
print("Люди, севшие в порту С - Cherbourg, выжили в большей степени")
print()

# 4
res_names = []
names = data[NAME_COL].tolist()
for i in names:
    res = i.find(',')
    i = i[0:res]
    res_names.append(i)
total = Counter(res_names).most_common(10)
print(total)


# 5
print("Медиана возраста")
med_age = data[AGE_COL].median()
print(med_age)
print("Медиана сетры брата")
med_sibsp = data[SIBSP_COL].median()  # медиана сестры и брата нелогичны, но сделать можно
print(med_sibsp)
print("Медиана родителей")
med_parch = data[PARCH_COL].median()  # медиана присутствия родителей на борту тоже странно
print(med_parch)
print("Медиана тарифа")
med_fare = data[FARE_COL].median()
print(med_fare)
print()

data[AGE_GROUP_COL] = data[AGE_COL]
data[AGE_GROUP_COL].fillna(med_age, inplace=True)

data[SIBSP_GROUP_COL] = data[SIBSP_COL]
data[SIBSP_GROUP_COL].fillna(med_sibsp, inplace=True)

data[PARCH_GROUP_COL] = data[PARCH_COL]
data[PARCH_GROUP_COL].fillna(med_parch, inplace=True)

data[FARE_GROUP_COL] = data[FARE_COL]
data[FARE_GROUP_COL].fillna(med_fare, inplace=True)

print("Медианные значения добавлены в таблицу!")
print()

# 6
print("Выживаемость в train.csv")
print(data[SURVIVED_COL].value_counts())
print()
everyone = data[NAME_COL]
everyone = everyone.count()
live = int(input("Введите количество выживших в файле train.csv (введите число, напротив 1): "))
print("Выживаемость в файле train.csv")
pers = live/everyone
print("{:.1%}".format(pers))
print()

NAME_COL1 = "Name"
data1 = pd.read_csv('test.csv')
everyone1 = data1[NAME_COL1]
everyone1 = everyone1.count()
live1 = pers * everyone1
print("Кол-во человек, которые выживут в файле test.csv, относительно статистики в trains.csv: ")
print(round(live1))





