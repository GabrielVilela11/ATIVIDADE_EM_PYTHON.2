#APROVANDO FINANCIAMENTO

from math import trunc
from math import ceil


print("Você pode financiar uma casa conosco em até 30 anos sem que os valores das parcelas mensais ultrapassem a 50% do valor atual do seu salário \n")

casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o seu salário mensal? R$"))
tempo = int(input("Sabendo que para financiar uma casa, é cobrado 6% de "
                  "juros ao ano. Em quantos meses deseja pagar a casa: "))

aa = tempo / 12
ano = ceil(aa * 10)/10

if 0 < tempo <= 360:
    j = tempo * 0.5
    total = casa + (casa * j / 100)
    print(f"\nO valor da casa com {j}% de juros ficou em R${total:.2f}\n")

    mes = total / tempo
    meio = salario - (salario * 50 / 100)

    if mes > meio:
        print("Você não foi aprovado para financiar a casa, devido as parcelas mensais ultrapassarem  50% do seu salário atual\n")

    else:
        a = trunc(ano)
        meses = str(ano).split('.')[1]

        if tempo == 1:
            print(f"A casa foi financiada por {tempo} mês ")

        elif tempo < 12:
            print(f"A casa foi financiada por {tempo} meses ")

        elif tempo == 12:
            print(f"A casa foi fianciada por {ano} ano")


        elif ano == 1 and (meses == '0' or meses == '1'):
            print(f"A casa foi financiada por {a} ano")

        elif ano > 1 and (meses == '0' or meses == '1'):
            print(f"A casa foi financiada por {a} anos")

        else:
            print(f"A casa foi financiada por {a} anos e {meses} meses")

    print(f"O valor das parcelas mensais ficaram em R${mes:.2f}")
else:
    print("Você só pode financiar a casa em até 30 anos")
