Formatação de string Python
###########################
:date: 2012-01-26 16:31
:author: jesuejunior
:category: Python
:tags: Python
:slug: formatacao-de-string-python


Estou aprendendo Python e estou gostando, aqui vai um método que um
sábio me ensinou e eu pesquisei mais algumas informações.

A partir da versão 2.6 o Python traz um recurso diferente para formatar
strings.

Diz o manual que a partir da versão 3.0 a formatação usando o método %
será descontinuado, por isso resolvi criar esse post tanto para ajudar
quem não sabe quanto para eu lembrar posteriormente.

Se você é iniciante em Python assim como eu, tente começar a mudar logo
para o método do str.format(). (Muito pratico)

#A mudança é simples. Portanto, vamos aos exemplos:

.. code-block:: python

    >>> nome = 'Jesué'
    >>> sobrenome = 'Junior'
    >>> idade = 23

# Campo simples.

.. code-block:: python

    >>> print "meu nome é %s" % (nome) # 's' de string
    >>> print "meu nome é {nome}".format(nome=nome)

# 2 campos mudando o nome da substituicao (“n” e “s”). Descobri esse recentemente.

.. code-block:: python

    >>> print "meu nome completo é %s %s" % (nome, sobrenome)
    >>> print "meu nome completo é {n} {s}".format(n=nome, s=sobrenome)

# Numero com 2 algarismos e zero à esquerda.

.. code-block:: python

    >>> print "minha idade é %02d anos" % (idade)
    >>> print "minha idade é {0:02d} anos".format(idade)

# Argumento posicional.

.. code-block:: python

    >>> print "eu sou {0} e eu tenho {1} anos".format(nome, idade)

Eu, comecei agora e já adotei o format, porque eu posso nomear os campos
livremente.

Lembrete: Ele só pode ser usado a partir do python 2.6.

Qualquer duvida leia maiores informações no manual.

