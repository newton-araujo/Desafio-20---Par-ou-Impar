'''
Para este desafio vamos criar um lista de 1 a 10. Usando o "for loop",
para iterar sobre a lista. Se o número atuall da iteração for par, 
imprima 
- "O número [número] é par"

Se for impar.
- "O número [número] é impar"

'''
#Criar lista de 1 a 10
numeros = [1,2,3,4,5,6,7,8,9,10]

#Criar for loop
for numero in numeros:
    #Condição para verificar se o número é par
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    #Caso o número for impar 
    else:
        print(f"O número {numero} é impar")