print("Bem-vindo a montanha russa safadinha")
altura = int(input("Qual o sua altura (em cm), meu pimpolho? "))

if altura >= 120:
    print("Muito bem, você é bem altinho e pode dar uma voltinha nessa montanha russa")
    idade = int(input("Qual a sua idade? "))
    if idade <= 12:
        print("Você é bem jovemzinho, vou te dar um descontinho, pague 5 reais")
    elif idade <= 18:
        print("Você já não é tão jovemzinho, mas vou te dar um descontinho, pague 7 reais")
    else:
        print("Véio coroca paga mais caro, porque tem imposto, pague 12 reais")
else:
    print("Opa, opa, opaaaaa, meu amigo, pode parando aí, você parece um anão cadeirante, você não pode subir na montanha")
