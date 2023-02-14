print("Pascal Triangle")

def val(l,c):
    if l==c or c==0:
        return 1
    
    else:
        return val(l-1, c-1) + val(l-1, c)
        
ln=int(input("Numbers of lines= ")); tri_pas =[""*(ln-lin)+"".join([f"{val(lin,col):4}" for col in range (lin+1)])for lin in range(ln + 1)]

print(*tri_pas, sep="\n")