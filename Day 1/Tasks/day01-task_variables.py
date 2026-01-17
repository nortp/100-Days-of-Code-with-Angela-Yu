"""*Desafio da aula de VARIÁVEIS:*

DESAFIO 1. Escrever um código em apenas uma linha, que leia a entrada do _user_ e imprima
o comprimento/quantidade de caracteres digitada por este.

Como nas aulas a professora ainda não havia falado sobre a função para esta finalidade, era necessário
realizar uma pesquisa no Google, que no caso, ela mesmo orientou realizar pesquisas durante o aprendizado.
Eu não fiz a pesquisa, pois até o ponto do vídeo em que ela mostrava onde pesquisar (usando W3Schools como exemplo
e documentação) eu notei como era a estrutura da função, no caso "len()" e tentei aplicar a partir dali mesmo no
desafio proposto.

Solução proposta abaixo"""
#print(len(input("Qual seu nome?")))

#DESAFIO 2. Escrever o mesmo código anterior, mas dividido em partes, agora utilizando variáveis.

name = input("Qual o seu nome?")
lenght = len(name)
print(lenght)

