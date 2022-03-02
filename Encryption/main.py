import numpy as np
import numpy as geek
import docx
import os
#1

def first_task():
    file_name = "/Users/farit_sib/PycharmProjects/Encryption/Vici.docx"
    file_stats = os.stat(file_name)

    print("File size:")
    print(f'File Size in Bytes is {file_stats.st_size}')
    print(f'File Size in KyloBytes is {file_stats.st_size / 1000}')
    print()

    # print("Text size:")
    # doc = docx.Document("/Users/farit_sib/Desktop/Vici.docx")
    # str1 = doc.paragraphs[0].text
    # print("Text in file: " + str1)
    # print("The length of the string  is :", len(str1))



#2
def second_task():
    with open("encoded.txt", "rb") as f:
        for line in f.readlines():
            print(line)
    txt = line

    all_dict = dict()  # crate dictionary

    for i in txt:
        if i in all_dict:
            all_dict[i] += 1
        else:
            all_dict[i] = 1

    print(f"Словарь частотности: {str(all_dict)}")



# Task №3

def third_task():
    import numpy as np
    import numpy as geek

    main_key = [3, 1, 4, 5, 2]
    code_key = [1, 2, 3, 4, 5]

    filename = "encoded.txt"
    with open(filename, encoding="utf8") as file:
        text = file.read()
        print("Main text: " + text)
        print()

    spl = list(text.replace(' ', ''))  # parse our txt

    if len(spl) % 5 != 0:
        spl += 'z' * (5 - (len(spl) % 5))
    print("Correctly added table with 'z' : " + f"{spl}")  # correctly added table with 'z'
    print()

    # зашифровка

    arr = np.array(spl).reshape(-1, 5).transpose()
    d = dict(enumerate(arr, 1))  # numerate dict
    new_d = sorted(d.items(), key=lambda pair: main_key.index(pair[0]))  # sort our dict by key
    all = []
    for i in new_d:
        for j in i:
            all.append(j)
    nechet = []
    for i in range(len(all)):
        if i % 2 != 0:
            nechet.append(all[i])
    my_array = np.array(nechet)
    my_array1 = geek.array_str(my_array)  # transform to str
    my_array2 = "".join(c for c in my_array1 if c.isalpha())
    print("Зашифрованное сообщение: " + my_array2)

    print()
    # расшифровка
    coded_array = np.array(list(my_array2)).reshape(5, -1)
    coded_d = dict(enumerate(coded_array, 1))
    coded_d = list(coded_d.items())
    all = []
    for i in coded_d:
        for j in i:
            all.append(j)
    repl = [3, 1, 4, 5, 2]
    ind = [0, 2, 4, 6, 8]
    for i in range(len(ind)):
        all[ind[i]] = repl[i]
    it = iter(all)
    res_dct = dict(zip(it, it))
    new_d = sorted(res_dct.items(), key=lambda pair: code_key.index(pair[0]))
    all = []
    for i in new_d:
        for j in i:
            all.append(j)
    nechet = []
    for i in range(len(all)):
        if i % 2 != 0:
            nechet.append(all[i])
    my_array = np.array(nechet).transpose()
    my_array1 = geek.array_str(my_array)  # transform to str
    my_array2 = "".join(c for c in my_array1 if c.isalpha())
    print("Расшифрованное сообщение: " + my_array2)

print(first_task())
print(second_task())
print(third_task())
