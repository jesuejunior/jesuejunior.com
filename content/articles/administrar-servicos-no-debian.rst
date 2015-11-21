:title: Administrar serviços no Debian/Ubuntu
:date: 2012-06-02 20:40
:author: jesuejunior
:category: Debian
:tags: Debian
:slug: administrar-servicos-no-debian
:lang: pt


Estou sempre precisando gerenciar alguns serviços no Debian/Ubuntu e percebi que havia esquecido, então aqui vai a dica.

**nome do serviço** é o nome_do_servico que quer iniciar no boot (apache2 por exemplo).

**NN** é o número da sequencia na qual o serviço será inicializado (por exemplo, 1, 10, 20 ou 99).

**runlevel** é em qual runlevel deseja que este serviço seja inicializado (aqui você pode colocar em todos os *runlevel*
de boot ou em apenas o que desejar) e não esqueça do ponto (**.**) no final do comando.

Administração dos serviços no boot, use:

.. code-block:: shell

    ~# update-rc.d nome_do_servico start NN runlevel runlevel

E esse aqui para os runlevel de saída (desligar ou reiniciar por exemplo):

.. code-block:: shell

    ~# update-rc.d nome_do_serviço stop NN runlevel runlevel

Para retirar um serviço do boot o comando é:

.. code-block:: shell

    ~# update-rc.d -f nome_do_serviço remove

Adicionado serviços na inicialização.
Para colocar um serviço na inicialização do Linux podemos utilizar uma ferramenta
chamada ntsysv, porém é interessante saber como funciona executar esta tarefa manualmente.
Os serviços do Linux ficam no diretório **/etc/rc.d/init.d**. Na inicialização os serviços localizados no diretório
**/etc/rc.d/rc[n].d** são inicializados ou parados. O **[n]** é o número correspondente ao run level, ou seja, é só
adicionar um link do serviço para este diretório com a seguinte nomenclatura:

.. code-block:: shell

    [S¦K]56[nomedoserviço]

Sendo: [S\N]:
Isto quer dizer se o serviço ou programa deve ser iniciado ou não;

**S**: start (iniciar);

**K**: kill (matar, parar).

**56**: É o número da fila em que ele deverá ser executado, se o número for menor ele será executado antes que os outros serviços;

**[nomedoserviço]**: somente para identificação humana, não interfere em nada.

Pronto, para inicializar um script primeiro você copia este script para o **/etc/init.d**:

.. code-block:: bash

    ~# cp /root/rotina.sh /etc/init.d

Depois crie um link simbólico para o diretório **/etc/rc.d/rc.[n]d** (para qual run level você quiser):

.. code-block:: shell

    ~# ln -s /etc/rc.d/init.d /etc/rd.c/rc3.d/S24rotina

Pronto, na inicialização em run level 3 o script rotina será executado.

Outro método para fazer:

.. code-block:: shell

    ~# vim /etc/init.d/meuscript

.. code-block:: shell

    #!/bin/bash
    echo "Olá mundo"

Agora é só dar a permissão para execução:

.. code-block:: shell

    ~# chmod 755 /etc/init.d/meuscript

Quase pronto, agora é só colocar para inicializar junto com o sistema:

.. code-block:: shell

    ~# update-rc.d meuscript defaults

Bom é isso ai, coisa simples.


