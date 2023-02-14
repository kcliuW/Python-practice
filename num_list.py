def num_list():
    num =""
    for n in "3445":
        num += n
        yield num
print(list(num_list()))