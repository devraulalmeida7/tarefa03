print("Digite o dia da semana abaixo.")
print("dom = 1, seg = 2, ter = 3, qua = 4, qui = 5, sex = 6 ,sab = 7")

valor = int(input("Digite o dia da semana: "))

dom = 1
seg = 2
ter = 3
qua = 4
qui = 5
sex = 6
sab = 7

hrs = int(input("Digite as horas: "))
mins = int(input("Digite os minutos: "))

if  2 <= valor <= 6 and  8<= hrs <= 11 and 0 < mins < 60 :
    print("Trabalhando")
elif valor == 7 and 8<= hrs <= 11 and 0 < mins < 60:
    print("Trabalhando")
else:
    print("Não está trabalhando")