Instalando e configurando o no-ip no Ubuntu
###########################################
:date: 2012-05-30 22:57
:author: jesuejunior
:category: Debian, ubuntu
:tags: Debian, no-ip
:slug: instalando-e-configurando-o-no-ip-no-ubuntu


A distribuição usada foi a Ubuntu 10.04 Server. Todos os comandos foram
dados como root. Baixando e descompactando o cliente para Linux do site
oficial do no-ip: http://www.no-ip.com

**Baixando o cliente no-ip com os comandos:**

.. code-block:: shell

    ~# wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz

**Descompacte o arquivo:**

.. code-block:: shell

    ~# tar -zvxf noip-duc-linux.tar.gz

**Entre no diretorio onde estão os arquivos:**

.. code-block:: shell

    ~# cd no-ip

**Para instalar execute o comando:**

.. code-block:: shell

    ~# make && make install

**Após o termino da instalação, será apresentada na tela algumas perguntas:**

.. code-block:: shell

	Please enter the login/email string for no-ip.com: "login/email cadastrado no site no-ip.com."
	Please enter the password for user `seu login/email será apresentado  aqui`: "digite sua senha."
	Please enter a update interval: [30]: "intervalo de atualização em minutos"
	Do you wish to run something at successful update?[N] (y/N) "n"

**Colocando para carregar no boot.**

Para que o cliente no-ip seja carregado cada vez que você ligar a
máquina, siga estes passos. Dentro da pasta noip criada anteriormente, digite:

.. code-block:: shell

    # cp noip-2.1.1/debian.noip2.sh /etc/init.d/
    # chmod +x /etc/init.d/debian.noip2.sh
    # ln -s /etc/init.d/debian.noip2.sh /etc/rc2.d/S20noip

Está assim terminada a instalação e configuração do cliente no-ip.
Espero que este guia seja útil a alguém. Aqui segue todo o os comandos
digitados e as opções conforme saída dos comandos:

.. code-block:: shell

    root@backup01:/home/ubuntu# cd noip
    root@backup01:/home/ubuntu/noip# make && make install
    gcc -Wall -g -Dlinux -DPREFIX=\"/usr/local\" noip2.c -o noip2
    if [ ! -d /usr/local/bin ]; then mkdir -p /usr/local/bin;fi
    if [ ! -d /usr/local/etc ]; then mkdir -p /usr/local/etc;fi
    cp noip2 /usr/local/bin/noip2
    /usr/local/bin/noip2 -C -c /tmp/no-ip2.conf

.. code-block:: shell

	Auto configuration for Linux client of no-ip.com. Please enter the
	login/email string for no-ip.com **user@gmail.com** Please enter the
	password for user 'user@gmail.com' ********** 2 hosts are registered to this account.
	Do you wish to have them all updated?[N] (y/N) **N**
	Do you wish to have host [backup01.no-ip.info] updated?[N] (y/N) **y[1]**
	Do you wish to have host [server02.no-ip.info] updated?[N] (y/N) **N[2]**
	Please enter an update interval:[30] **15**
	Do you wish to run something at successful update?[N] (y/N) **y**
	Please enter the script/program name **backup01   [3]**
	New configuration file '/tmp/no-ip2.conf' created.
	mv /tmp/no-ip2.conf /usr/local/etc/no-ip2.conf

**[1]** - Coloque YES para ser o dominio a ser usado por este  computador.

**[2]** - Deixe NO para usar apenas um dos domínio se você tiver mais faça o mesmo para os outros. No meu caso eu tinha mais de um host associado ao mesmo login.

**[3]** - Aqui é apenas o nome do script que vai ser gerado e para depois voce colocar na inicialização do S.O.


