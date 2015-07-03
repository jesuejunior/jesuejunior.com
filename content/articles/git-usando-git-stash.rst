GIT: Usando git stash (Começando a trabalhar em equipe)
#######################################################
:date: 2012-10-12 15:42
:author: jesuejunior
:category: Git, Linux
:tags: Git, Linux
:slug: git-usando-git-stash

O motivo desse post é mostrar a utilidade do\ ** git stash**.

Breve relato: Estou desenvolvendo uma ferramenta chamada
`m2tool <https://github.com/jesuejunior/m2tool>`__ junto com o `Dalton Matos <http://www.daltonmatos.com>`__,
então em um fim de semana, estávamos  conversando e desenvolvendo, como o projeto está bem no começo, o que eu estava
fazendo ele já precisava e vice-e-versa. Ele fez \ * push* de um novo recurso para a ***branch develop*** que
eu precisava para continuar desenvolvendo uma funcionalidade, porem eu não tinha feito *commit* das minhas
alterações até o momento e não poderia fazer , pois estava incompleto e dependia do que eu iria aplicar
para rodar os testes..

 
O que foi preciso fazer?

Usar o git stash para salvar minhas alterações até o momento (tipo
temp), peguei as alterações que estavam disponiveis na branch develop
fiz rebase na minha branch e depois voltei de onde havia parado sem
perder nada e já podendo usar as coisas novas. Isso foi o máximo.
hahahaha

*The Stash*, quando você precisa guardar mudanças que ainda não foi
feito *commit*, mas você precisa voltar para ultima revisão da sua
branch o chamado "HEAD".

E quando você restaura o seu *stash*, você consegue continuar
trabalhando em seu código de onde parou anteriormente.

***Fazendo o Stash* de suas modificações atuais e que ainda não  foram
comitadas.**

.. code-block:: shell

    $ git stash save
    Saved "WIP on master: ed1a10e..."

**Listando *stashes* atuais.**

Sim, você pode salvar mais do que um. *Stash* funciona como uma pilha e
a qualquer momento você pode salvar o novo stash e será colocado como
ultimo na pilha. (Espero que conheça o conceito de pilha)

.. code-block:: shell

    $ git stash list
    stash@{0}: WIP on master: 151f1ab..."
    stash@{1}: WIP on master: ed1a10e..."

Perceba a parte **stash@{0}.** Este é seu ID *stash*, é o que você
precisa saber para restaura-lo posteriormente. Note que temos 2 stashes
e que o stash@{1} contem as suas modificações mais recentes.

**Aplicando um *"stash"***

| Existe duas formas que eu conheço de aplicar um *stash*.
|  1º. Simples e facil de entender para quem saca de pilhas.

.. code-block:: shell

    $ git stash pop stash@{0}

ou simplesmente assim já que se trata de pilha ele pega o ultimo da
pilha e aplica.

.. code-block:: shell

    $ git stash pop

2º. Facil, porem pode ficar o *stash* na listagem mesmo depois de
aplicado.

.. code-block:: shell

    $ git stash apply stash@{0}

Como disse antes, usando o *apply* o *stash* pode continuar salvo, então
o que podemos fazer para limpar *stashes* que já usamos ou não
precisaremos mais é:

.. code-block:: shell

    $ git stash drop stash@{0}

E para limpar todos os *stashes* basta executar:

.. code-block:: shell

    $ git stash clear

Se você quer apenas fazer de forma rápida um *stash* e que logo apos um
*rebase* ou *merge* já o restaurará, pode usar simplesmente:

.. code-block:: shell

    $ git stash
    $ git rebase develop
    $ git stash pop

O que fizemos foi guardar nossas alterações, *rebase* em nossa *branch*
com base na *develop* e em seguida aplicamos nosso stash para continuar
desenvolvendo.

OBS: Existem inúmeras maneiras de usar o *git stash*, tentei mostrar a
maneira que me ajudou.

A melhor coisa à ser feita é testar bastante e entender o funcionamento
para só depois colocar em pratica em um trabalho de verdade.

Espero que ajude. Obrigado.

.. |image0| image:: http://blog.jesuejunior.com/wp-content/uploads/2012/10/github-logo.png
   :target: http://blog.jesuejunior.com/wp-content/uploads/2012/10/github-logo.png
