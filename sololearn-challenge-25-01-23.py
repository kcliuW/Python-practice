# Question 1
print("python"=='python')

# Question 2
words = ["Python", "40"]
index = 2
words.insert(index, "forty")
words.append("fty")
print(len(words[2]))

# Question 3
i = [1, 2, 3]
s = '{2}{1}{0}'.format(i[0],i[2],i[1])
print(s)

# Question 4
class A:
    _var = 5
    def pr(self):
        print(self._var)

class B(A):
    _var = 4

B().pr()

# Question 5
s = "troe!"
print(s[3]+s[1]*2+s[2]+s[1]+s[4])