#algoritmo começa solicitando a entrada dos dados/valores, total da conta{bill}, porcentagem
#que a pessoa quer dar de gorjeta{tip} e quantidade de pessoas{people} que irá dividir a conta
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#A primeira variável quer saber o valor total da conta{bill} com a porcentagem da gorjeta{tip} e dividir para a
#quantidade de pessoas{people} que dividirão a conta. Exemplo: a CONTA deu R$100.00, a PORCENTAGEM
#selecionada foi 10, e a CONTA foi dividida para 2 PESSOAS. O resultado seria R$55.00,
#sendo que 10% de 100 = R$10.00, e a conta total vai ser dividida entre as duas pessoas.
splitBill = (bill / people) * (tip / 100 + 1)
#A segunda variável quer receber o valor do quanto cada pessoa pagará de gorjeta, sendo assim multiplica o total
#da {bill} pela porcentagem escolhida{tip} e divide pela quantidade de PESSOAS{people}. Exemplo: Se a {bill} deu
#R$100.00 e a {tip} é 10%, e serão 2 {people} para dividir, o resultado será R$5.00 cada pessoa
tipPerPeople = ((bill * tip / 100) / people)
#depois ela só apresenta o resumo dos dados, total da conta, quanto ficou para cada um com a porcentagem aplicada
#e quanto deu de total com a gorjeta inclusa
print(f"Give a total bill of ${bill}")
print(f"Each person should pay: ${splitBill:.2f}")
print(f"Each person should give a tip of ${tipPerPeople:.2f} dollars")
print(f"The total bill with tip is ${bill + (bill * tip /100)}. Thank you for your help!")