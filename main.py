
# zad1
# moje_ulubiene_filmy=["Sharknado","Jack frost: zemsta zmutowanego balwana","Dracula w Pakistanie","Nazistowscy Surferzy Muszą Zginąć","Embrion wybiera sie na lowy"]
# moje_ulubiene_filmy.reverse()
# moje_ulubiene_filmy.insert(5,"Zakaźne zanikowe zapalenie nosa u świń")
# moje_ulubiene_filmy.insert(6,"Dokładnie naładujcie babcie!")
# moje_ulubiene_filmy.insert(7,"Maniakalne pielęgniarki w poszukiwaniu ekstazy")
# moje_ulubiene_filmy.insert(8,"Zmotoryzowane laski w krainie zombich")
# moje_ulubiene_filmy.insert(9,"Twardy jak brylant")
# print(moje_ulubiene_filmy)


# zad2
# slownik=[1:'Embrion wybiera sie na lowy', 2:'Nazistowscy Surferzy Muszą Zginąć', 3:'Dracula w Pakistanie', 4:'Jack frost: zemsta zmutowanego balwana', 5:'Sharknado', 6:'Zakaźne zanikowe zapalenie nosa u świń', 7:'Dokładnie naładujcie babcie!', 8:'Maniakalne pielęgniarki w poszukiwaniu ekstazy', 9:'Zmotoryzowane laski w krainie zombich', 10:'Twardy jak brylant']


#zad3
# przedmioty={"md":"matematyka dyskretna", "wd":"wizualizacja danych", "ps":"programowanie strukturalne", "CAD":"komputerowe wspomaganie projektowania", "rr":"rachunek różniczkowy i całki"}
# print(len(przedmioty))


# #zad4
# print("wprowadz liczbe, a ja podniose ja do tej samej potegi")
# a=int(input())
# print(pow(a,a))


#zad.5
# a=open(siema.txt,"+")
# a.readline()
# a.write("napis zawiera ",a.count('c')," liter c")


#zad.6
# a=int(input("wpisz 3 liczby calkowite, a ja sprawdze, czy a jest parzyste i b>c: "))
# b=int(input())
# c=int(input())
# if a%2==0 and b>c:
#     print("a jest parzyste, a b jest wieksze od c")
# else:
#     print("warunek nie jest spelniony")


#zad.7
# liczby=[2,3,4,1.1,5,2.7,1]
# for x in liczby:
#     print(x+(x+1))



# #zad.8
# lista=[]
# licznik=0
# while licznik<10:
#     i=float(input())
#     if type(int(i))==int:
#         lista.append(int(i))
#     licznik+=1
# print(lista)



#zad9 nie umiem :D
# lista=[1,2,3,4,5,6]
# zera="000000"
# szlaczek="0    0"
# rzad=1
# if rzad==1 or rzad==6:
#     for x in lista:
#         print(zera)
# elif rzad ==2 or rzad==3 or rzad==4 or rzad==5:
#     for x in lista:
#         print(szlaczek)
# rzad+=1

#zad.10 tutaj tez problemy
# a=input("podaj cyfre: ")
# if type(int(a))==int or type(float(a))==float:
#     print("dobrze")
# else:
#     print("zle")