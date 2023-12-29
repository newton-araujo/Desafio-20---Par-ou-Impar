<h1>Desafio 20 - Identificação de Números Pares e Ímpares em uma Lista </h1>

<p>
Este código tem como objetivo criar uma lista de números de 1 a 10 e, em seguida, utilizar um loop for para identificar se cada número é par ou ímpar.
</p>

<ol>
<h2><li>Criação da Lista:</li></h2>
<ul>
<li>Inicia a variável numeros com uma lista contendo os números de 1 a 10.</li>
</ul>

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

<h2><li>Loop for:</li></h2>
<ul>
<li>Utiliza um loop for para iterar sobre cada elemento da lista numeros.</li>
</ul>

    for numero in numeros:


<h2><li>Condição de Verificação:</li></h2>
<ul>
<li>Dentro do loop, utiliza uma estrutura condicional (if) para verificar se o número é par ou ímpar.</li>
<li>Verifica se o resto da divisão por 2 (numero % 2) é igual a 0 para determinar se o número é par.
python
</li>
</ul>

    if numero % 2 == 0:

<h2><li>Saída de Dados:</li></h2>
<ul>
<li>Imprime uma mensagem indicando se o número é par ou ímpar.</li>

    print(f"O número {numero} é par")

<li>Em caso de número ímpar, imprime uma mensagem correspondente.</li>

    else:
        print(f"O número {numero} é ímpar")
</ul>
</ol>

<h3>Interatividade:</h3>
<p>
O código proporciona uma experiência interativa ao percorrer a lista de números de 1 a 10, identificando e informando se cada número é par ou ímpar.
</p>

<h3>Conclusão:</h3>
<p>
Ao executar este código, será gerada uma saída que indica se cada número na lista é par ou ímpar, demonstrando o uso de loops e estruturas condicionais em Python.
</p>