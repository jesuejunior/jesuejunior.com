Ativando conexões remotas ao PostgreSQL
#######################################
:date: 2012-07-06 22:19
:author: jesuejunior
:category: Banco de Dados, PostgreSQL
:tags: PostgreSQL
:slug: ativando-conexoes-remotas-postgresql
:status: published

Neste tópico vou *tentar* explicar como liberar conexões remotas pela rede a uma base de dados PostgreSQL (9.1).

Por padrão o PostgreSQL vem configurado para receber apenas conexões locais (localhost ou 127.0.0.1). Para conectar de outra máquina
na rede é preciso alterar algumas configurações básicas em 2 arquivos.

(Linux)

São eles:  **postgresql.conf** e **pg_hba.conf**.

 

No  **postgresql.conf** vamos editar a seguinte linha:

.. code-block:: shell

    #listen_addresses = ‘localhost’ # what IP address(es) to listen on

Como em todo arquivo de configuração em programas linux, o # na frente
da linha significa um comentário e com isso desabilita o parâmetro
seguinte, tomando seu valor default, que no caso é localhost. Descomente
essa linha e substitua seu valor por \*. Assim seu PostgreSQL estará
apto a ouvir conexões de qualquer IP.Então essa linha ficará da seguinte
forma:

.. code-block:: shell

    listen_addresses = '*' # what IP address(es) to listen on

Isso não quer dizer que ele estará aberto para qualquer IP da rede. É
possível criar políticas de acesso através de outro arquivo que
falaremos a seguir.

Liberando as conexões no arquivo \ **pg\_hba.conf**:

Este é o arquivo do Postgres responsável pela liberação de usuários,
hosts e bancos de dados. Nele é possível dizer qual usuário de qual ip
(ou rede) conectará a qual banco. É possível liberar qualquer usuário
para conectar a qualquer banco, mas esta é uma regra cautelosa a ser
seguida pois pode comprometer a segurança do seu servidor de bases de
dados.

**Por padrão o arquivo vem com a seguinte configuração:**

.. code-block:: shell

     #“local” is for Unix domain socket connections only
     local all all trust
     # IPv4 local connections:
     host all all 127.0.0.1/32 trust
     # IPv6 local connections:
     host all all ::1/128 trust

Pode haver alguma variação das configurações padrões de acordo com a
versão utilizada, mas geralmente é algo que represente essas
informações. Basicamente elas querem dizer que todas as conexões locais
podem ser realizadas por qualquer usuário do banco a qualquer banco de
dados.

Para liberar o acesso remoto basta criar uma nova regra seguindo o
seguinte padrão:

.. code-block:: shell

    host all all 0.0.0.0/0 trust

Com essa regra qualquer usuário de qualquer IP poderá se conectar a
qualquer database.

**Importante**: O parâmetro trust quer dizer que não será solicitada
qualquer senha para conectar ao banco de dados. Então, qualquer pessoa
com acesso à sua rede poderá se conectar ao servidor PostgreSQL sem
nenhuma restrição. Se a sua rede for restrita como uma turma de um curso
ou um ambiente de desenvolvimento interno de empresa não há riscos,
porém, é necessário possuir um ambiente de rede interno isolado.

Este parâmetro é útil quando você ainda não se conectou ao banco para
criar uma senha de acesso ao usuário postgres (do banco e não do sistema
operacional). Então você se conecta e reseta a senha do usuário. Logo em
seguida, altere o parâmetro para md5. Assim, uma senha será solicitada
ao tentar conectar-se ao servidor Postgre.

**Assim ficará a regra de liberação:**

.. code-block:: shell

    host all all 0.0.0.0/0 md5

**É possível também liberar o acesso apenas a uma rede específica:**

.. code-block:: shell

    host all all 192.168.0.0/32 md5

**Ou também, informar qual usuário poderá conectar:**

.. code-block:: shell

    host all usuariodobanco 192.168.0.0/32 md5

**Também informar qual o banco de dados a ser conectar por este
usuário:**

.. code-block:: shell

    host db userdb 192.168.0.0/32 md5

Na regra acima, o usuário \ *userdb* do banco  poderá conectar-se apenas
ao banco db apenas se estiver dentro da rede 192.168.0.0.

Essa é a dica, precisei muito disso e quebrei a cabeça um pouco então
fica guardado agora, espero que possa ajudar alguém.
