while True:
    try:
        size=int(input("Uchta ro'yxatning ummumiy hajmini kiriting: "))
    except ValueError:    
        print("Xato. Hajmi butun son bo'lishi zarur. Boshqatdan kiriting.\n")
    else:
        break
    
list1=[]
list2=[]
list3=[]
gen_list=[]
print()
print("Birinchi ro'yxat: ")
for steps in range(size):
    while True:
        try:
            value=input("Ichiga qiymat kiriting: ")
            if value=="":
                raise OSError("DIQQAT! Hali qiymat kiritmadingiz. Boshqatdan kiriting.\n")
        except OSError as exc:
            print(exc)
        else:
            list1.append(value)
            break

print()        
print("Ikkinchi ro'yxat: ")
for steps in range(size):
    while True:
        try:
            value=input("Ichiga qiymat kiriting: ")
            if value=="":
                raise OSError("DIQQAT! Hali qiymat kiritmadingiz. Boshqatdan kiriting.\n")
        except OSError as exc:
            print(exc)
        else:
            list2.append(value)
            break

print()        
print("Uchinchi ro'yxat: ")
for steps in range(size):
    while True:
        try:
            value=input("Ichiga qiymat kiriting: ")
            if value=="":
                raise OSError("DIQQAT! Hali qiymat kiritmadingiz. Boshqatdan kiriting.\n")
        except OSError as exc:
            print(exc)
        else:
            list3.append(value)
            break        

print()

for index in range(size):
    diction1=dict()
    diction2=dict()
    diction1[list2[index]]=list3[index]
    diction2[list1[index]]=diction1
    gen_list.append(diction2)

print(f"Chiqish: {gen_list}")