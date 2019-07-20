Aprendendo a usar o GitHub (Primeiros passos)
#############################################
:date: 2012-06-06 20:18
:author: jesuejunior
:category: Linux
:tags: Git
:slug: aprendendo-github-primeiros-passos
:status: published

`GitHub <https://github.com/>`__ é uma rede social para códigos, muito interessante, você consegue
guardar seus códigos, conhecer outros devs, recebe ajuda em seus projetos, divulga os seus, entre outras coisas.
Me interessei sobre o assunto e uso hoje em dia, então resolvi escrever esse post, primeiro para não
esquecer e depois para ajudar quem estiver começando e precisar ter uma ajuda para aprender sobre versionamento de código e guarda-los.
É possível guardar código de qualquer linguagem, com opções de repositórios publico(free) ou privados(pago),
no meu caso como é para aprendizagem e projetos pessoais não vejo problemas usar publicamente.

**1º Passo** é criar uma conta no `GitHub <https://github.com/>`__

**2º Passo** é instalar o GIT em sua maquina Linux, que depende muito da sua distribuição.

Para baseados em Debian/Ubuntu.

.. code-block:: shell

    $ sudo apt-get install git

Para Archlinux.

.. code-block:: shell

    $ sudo pacman -S git

Para baseados em Red Hat

.. code-block:: shell

    $ sudo yum install git

Configurar o cliente GIT, para vincular os commits para o autor correto

.. code-block:: shell

    git config --global user.name "SEU NOME AQUI"
    git config --global user.email email@gmail.com

Para inicializar o repositório GIT vazio existe duas formas [1] [2]

***[1]*** - Executando o comando abaixo, que o git vai criar a pasta, caso ela não existir e inicializará como repositório GIT. Ex:

.. code-block:: shell

    ~$ git init python

[2] Criar a pasta e depois entrar na pasta e depois inicializar o repositório, ficaria assim:

.. code-block:: shell

    ~$ mkdir python
    ~$ cd python
    ~$ git init

Entre em seu repositório e crie o arquivo README

.. code-block:: shell

    cd python/
    vim README

Escreva um texto inicial, como por exemplo “First commit” e salve o arquivo (:wq)

.. code-block:: shell

    ~$ git status

Aparecerá a os dados conforme imagem abaixo, mas o que isso quer dizer?
Bom, a parte importante dessa tela é *Untracked files* que mostra os arquivos que o GIT ainda não está gerenciando, ou seja, o GIT não sabe o
que fazer com ele e não registra nenhuma modificação no arquivo.

|image1|

Então temos que adicionar o(os) arquivo(os) que queremos que o GIT gerencie para nos.

.. code-block:: shell

    ~$ git add README

Veremos agora o que mudou depois de mandar o GIT gerenciar nosso arquivo *README.*

.. code-block:: shell

    ~$ git status

Agora percebemos que o status do nosso arquivo mudou de **Untracked files** como na imagem anterior para **Changes to be committed**,
isso quer dizer que a partir de agora o GIT vai gerenciar o nosso arquivo, ele mostra que voce não fez o *commit* para essa modificações entrarem em vigor.

|image2|

Fazendo o *commit* existem duas maneiras para fazer isso. [3] [4]

[3] Podemos apenas digitar o comando e o nosso editor de textos padrão abrirá para voce poder escrever a mensagem que identificará o *commit*.

.. code-block:: shell

    ~$ git commit

[4] Podemos fazer tudo isso em apenas uma etapa da seguinte forma. O ***-m*** informa para esperar a mensagem de *commit* entre aspas por ser uma string.

.. code-block:: shell

    ~$ git commit -m 'Adicionando arquivo README'

No fim se tudo ocorrer certo, será mostrada uma mensagem conforme imagem.

|image3|

Temos como ver o histórico de *commit,*existem inúmeras formas de customizar a visualização do histórico, duas sugestões rápidas
***-n* *[5]** e o  ***--committer=<nomedocara>***

**[6]**, para saber todas as possibilidades pode utilizar o comando de ajuda *git log --help*

.. code-block:: shell

    ~$ git log

**[5]** - Limita o numero de linhas a ser mostrado

**[6]** - Mostra apenas os *commits* da pessoa que você precisa ver, muito útil para quando se tem mais de um dev fazendo *commit* no mesmo projeto.

Agora vamos direcionar nosso repositório local GIT para nosso repositório remoto no GItHub, assim poder desfrutar dos recursos
que o github.com oferece, alem de ter nosso código guardado e exposto para receber ajuda e etc.

Onde  **jesuejunior** deve ser o nome de usuario que voce criou no site do github e  **python** é o repositório de
seu projeto criado, assim você estando dentro de seu repositório local ele vai direcionar seus arquivos devidamente 
commitados através do comando  *push* que veremos em instantes.

.. code-block:: shell

    ~$ git remote add origin git@github.com:jesuejunior/python

Para ver seu repositório remoto, utilize o comando:

.. code-block:: shell

    ~$ git remote

Se tem para adicionar tem que ter como remover, certo? Então para
remover um repositório remoto, voce precisa saber qual repositório voce
quer remover, após executar o comando *git remote* temos o resultado
*origin*, então para remover é simples, utilize o comando:

.. code-block:: shell

    ~$ git remote rm origin

Pronto foi removido seu repositório remoto (redirecionamento para o
github).

Ao tentar verificar seu repositório, com o seguinte comando, voce
receberá uma menssagem de erro, pois não tem sua chave SSH/RSA
configurada.

.. code-block:: shell

    ~$ git remote show origin

| Então vamos configura-la.
|  Primeiro entre  na pasta onde fica gravado suas chaves SSH (rsa)

.. code-block:: shell

    ~$ cd ~/.ssh/

Agora vamos gerar sua chave SSH.

.. code-block:: shell

    ssh-keygen -t rsa -b 2048 -f github

|image4|

Vai pedir uma senha para sua chave por duas vezes, sugiro **não**
colocar a mesma senha do site. Pronto sua chave foi gerada com sucesso.

Precisamos agora editar nosso arquivo *config*  que deve conter o
seguinte conteúdo.

.. code-block:: shell

    vim ~/.ssh/config

.. code-block:: shell

    Host github.com
    Port 443
    HostName ssh.github.com
    IdentityFile ~/.ssh/github
    User git

Agora copie o conteúdo do github.pub

Para exibir o conteúdo da chave em seu terminal execute o comando
abaixo, nada impede de abrir no seu editor de texto preferido.

.. code-block:: shell

    cat ~/.ssh/github.pub

Esse é o conteúdo que deve ser copiado para  sua pagina do Github >
Account Settings > SSH Public Keys > Add SSH Key\ |image5|

Vamos verificar se conseguimos acessar nosso repositório no GitHub.com e
ver se está redirecionado corretamente.

.. code-block:: shell

    ~$ git remote show origin

|image6|\ Agora vamos fazer nosso primeiro envio de arquivos para o
GitHub através do comando:

.. code-block:: shell

    ~$ git push origin master

A partir de agora sempre que fizer modificações nos arquivos, você segue
a sequencia de comandos *status*, \ *add,  commit e push.*

Para enviar as alterações para o repositório do GitHub a partir da
segunda vez, use apenas:

.. code-block:: shell

    ~$ git push

Se este post te ajudou, comente, agradeça e se ainda  tem duvida entre
em contato.

Em breve estarei fazendo um post bem legal sobre como trabalhar com
***branch*** utilizando os comandos ***rebase, merge*** entre outros

.. |image1| image:: /img/git/gitstatus.png
   :target: http://jesuejunior.com/aprendendo-github-primeiros-passos/gitstatus/
.. |image2| image:: /img/git/gitstatus2.png
   :target: http://jesuejunior.com/aprendendo-github-primeiros-passos/gitstatus2/
.. |image3| image:: /img/git/gitcommit.png
   :target: http://jesuejunior.com/aprendendo-github-primeiros-passos/gitcommit/
.. |image4| image:: /img/git/chave-rsa.png
   :target: http://jesuejunior.com/aprendendo-github-primeiros-passos/chave-rsa/
.. |image5| image:: /img/git/chave-rsa2.png
   :target: http://jesuejunior.com/aprendendo-github-primeiros-passos/chave-rsa2/
.. |image6| image:: /img/git/remote-show.png
   :target: http://.jesuejunior.com/aprendendo-github-primeiros-passos/remote-show/
