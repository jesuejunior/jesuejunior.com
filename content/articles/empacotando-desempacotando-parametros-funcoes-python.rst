Empacotando e desempacotando parâmetros em funções Python
#########################################################
:date: 2012-07-07 02:34
:author: jesuejunior
:category: Python
:tags: Python
:slug: empacotando-desempacotando-parametros-funcoes-python

Atualmente estou trabalhando com Python e Django, logo
quero/preciso me aprofundar na linguagem e conhecer esse universo está
sendo fantástico e hoje estava lendo e aprendendo sobre como empacotar
e desempacotar parâmetros, coisa que u não sabia que existia, então
gostaria de mostrar o funcionamento. :D
Uma flexibilidade incrivel!

  **#Empacotar parâmetros **
  EX:

.. code-block:: python

    def soma(a,b):
        print a + b

    K = [2,3]

    soma(*K)

Então estamos usando o "\*" para indicar que queremos desempacotar  a
lista ***K*** utilizando seus valores como parametro para a função
***soma***, no exemplo, K[0] será atribuido a ***a*** e K[1] a ***b***.
Esse recurso nos permite armazenar nossos parâmetros em listas e evita
construções estranhas do tipo ***soma(K[0], K[1])***

Vou  descrever um exemplo para mostrar ***lista*** de ***lista*** para
realizar varias chamadas dentro de um ***for***.

.. code-block:: python

    def barra(n=10, c="*"):
        print c*n

    L = [ [3, "-"], [10, "*"], [10], [7, "."] ]

    for a in L:
        barra(*a)

Observe que mesmo usando o empacotamento de parâmetros, recursos
como parâmetros opcionais ainda foram possíveis quando ***a*** contem
apenas um elemento.

**#Desempacotar parâmetros**

Podemos criar funções que recebem um numero indeterminado de parâmetros
utilizando listas de parâmetros.

EX:

.. code-block:: python

	def soma(*args):
		s = 0
		for x in args:
			s += x
		return s

	soma(2,4)
	soma(1,2,3,4,5,6,7,8,9)

Descobri também que podemos usar funções que combinem parâmetros
obrigatorios e uma lista de parâmetros.

.. code-block:: python

    def imprime_maior(msg, *numeros):
        maior = None
        for e in numeros:
             if maior == None or maior < e:
                 maior = e
        print msg, maior

    imprime_maior("Maior: ", 8,6,5,3,1)
    imprime_maior("Max: ", *[1,8,4])

Observe que o primeiro parâmetro é ***msg***, tornando-o obrigatório.
Assim ***imprime\_maior()*** retorna erro, pois o parâmetro ***msg***
não foi passado, mas ***imprime\_maior("Max: ")*** escreve ***None***.
Isso porque numeros é recebida como uma lista, podendo inclusive estar
vazia.

Bom essa foi a tentativa, espero que ajude alguem.

Python é muito muito fantástico!

.. |image0| image:: http://blog.jesuejunior.com/wp-content/uploads/2012/07/python_logo_150px.jpg
   :target: http://blog.jesuejunior.com/wp-content/uploads/2012/07/python_logo_150px.jpg
