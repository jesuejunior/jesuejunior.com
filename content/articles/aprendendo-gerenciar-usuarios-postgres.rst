Aprendendo a criar e gerenciar usuários no PostgreSQL(Primeiros Passos)
#######################################################################
:date: 2012-10-12 21:04
:author: jesuejunior
:category: Banco de Dados, Linux, PostgreSQL
:tags: Banco de Dados, PostgreSQL
:slug: aprendendo-gerenciar-usuarios-postgres

Confesso que logo de cara quando comecei a usar PSQL fiquei
meio perdido (usava MySQL), então estou escrevendo essa dica para eu
relembrar e deixar o legado. kkkk

Criando seu 1° super usuário no PostgreSQL.
Depois de instalado seu SGBD postgres, como criar seu 1° usuário?
Qual a senha de root? Qual a senha padrão?

Esta dica é para iniciantes.
Simples, na máquina com o banco instalado siga os seguintes passos,
existem varias maneiras de fazer isso, e essa foi a maneira
mais básica/simples que eu achei para explicar.

Logue-se como root, digite "su root" ou "sudo -i" ou "sudo su" (no
terminal a mensagem padrão deve terminar com #).
Entre como usuário postgres com o comando:

.. code-block:: shell

    # su postgres

Conecte ao Shell do postgres (por padrão você se conecta ao DB postgres)
comando:

.. code-block:: shell

    $ psql

Agora deve aparecer uma frase de boas vindas (Bem vindo ao psql...) e
você está no terminal do posgres, note que o shell mudou antes era
**root@pc #** agora ficou **postgres=#**
Isso quer dizer que agora você está no shell do PostgreSQL conectado
no banco *postgres*.

Para criar nosso superuser, digite o comando:

.. code-block:: sql

    CREATE USER nomedousuario SUPERUSER INHERIT CREATEDB CREATEROLE;

Depois temos que alterar a senha, então digite  o comando:

.. code-block:: sql

    ALTER USER nomedousuario PASSWORD 'senha';

Olha que maravilha! Super Usuário criado.

Comandos básicos, para você que está acostumado com o golfinho, o Mamute
é bem diferente.

.. code-block:: postgres

	# psql
	\l => "Lista todos os bancos de dados."
	\c nome-banco  => "Conecta no banco *nome-banco*"
	\d  => "Lista as tabelas do banco de dados conectado."
	\d  table-name => "Descrimina as colunas da tabela."
	\dg => "Lista usuários existentes, as permissões e grupos que o usuário pertence."
	\password [usuario] => "Troca a senha do usuário com segurança, ou seja você não vê a senha que foi digitada e não é possível ver através do histórico de comandos"
	select * from table-name;  => "Lista o conteúdo das tabelas. (o.O)"

Poderíamos usar essas opções da mesma forma, mas criando um usuário comum e colocando as permissões mais restritivas.

.. code-block:: sql

    CREATE USER jesuejunior WITH PASSWORD 'supersecret';

Para conceder a permissão de executar somente Update ou Select ou Insert ou Delete ou Role(dono)

.. code-block:: sql

    GRANT UPDATE ON nomedatabela to jesuejunior

.. code-block:: sql

    GRANT SELECT ON nomedatabela to jesuejunior

.. code-block:: sql

    GRANT INSERT ON nomedatabela to jesuejunior

.. code-block:: sql

    GRANT DELETE ON nomedatabela to jesuejunior

.. code-block:: sql

    GRANT RULE ON nomedatabela to jesuejunior

E para dar permissão para fazer todas as operações.

.. code-block:: sql

    GRANT ALL PRIVILEGES ON nomedatabela to public

Partindo do principio que você já está conectado com o usuário postgres.

Para apagar um usuário:

.. code-block:: shell

    $ dropuser jesuejunior

Bom isso já me ajudou a ganhar muito tempo, e espero que ajude outras pessoas.

Em breve estarei postando sobre gerenciar databases.

.. |image0| image:: http://blog.jesuejunior.com/wp-content/uploads/2012/07/postgresql.png
   :target: http://blog.jesuejunior.com/wp-content/uploads/2012/07/postgresql.png
