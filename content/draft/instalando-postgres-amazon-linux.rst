Instalando postgres no Amazon Linux
###################################
:date: 2015-10-12
:author: jesuejunior
:category: Banco de Dados, Linux, PostgreSQL
:tags: Banco de Dados, PostgreSQL
:slug: instalando-postgres-amazon-linux

.. code-block:: shell

	$ sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs -y

.. code-block:: shell

	$ sudo service postgresql initdb

.. code-block:: shell
	$ sudo vim /var/lib/pgsql/data/pg_hba.conf ou sudo vim /var/lib/pgsql92/data/pg_hba.conf

	Criar o arquivo *pg_hba.conf* com os seguintes dados:

.. code-block:: shell

	local   all         all                                  trust
	host    all         all         0.0.0.0/0          md5


.. code-block:: shell

	$ sudo vim /var/lib/pgsql92/data/postgresql.conf


Colocar esse conteudo se quiser acesso de qualquer IP, conforme falei nesse post.

.. code-block:: shell

	listen_addresses = ‘*’


