Instalando Chef Server Opensource
#################################
:date: 2013-12-31 19:54
:author: jesuejunior
:category: Chef, Debian, Linux, ubuntu
:tags: chef, Linux, opensource, opscode, ubuntu
:slug: instalando-chef-server

Instalando o Chef server opensource (`OpsCode <http://www.getchef.com/>`__)
Estarei criando um servidor do chef para gerenciar deploy do cloudfish(link) e com isso estou escrevendo esse tutorial.


*Cenário*
=========

Estou usando uma instancia de 512MB com Ubuntu 12.04 do Digital Ocean.

Ainda não criei usuários, então estou executando como root, depois todas as configurações serão feitas pelo chef.

Primeiro passo é baixar o arquivo para a distribuição que no caso é ubuntu, no presente momento a versão mais atual é a 11.0.10-1.

Logo o arquivo a ser baixado será:

`chef-server_11.0.10-1.ubuntu.12.04_amd64.deb <https://opscode-omnibus-packages.s3.amazonaws.com/ubuntu/12.04/x86_64/chef-server_11.0.10-1.ubuntu.12.04_amd64.deb>`__

Você pode sempre encontrar a versão mais atual na aba *server* do link:

http://www.getchef.com/chef/install/

Baixando o arquivo com todas as configurações do chef-server.

.. code-block:: shell

    # wget https://opscode-omnibus-packages.s3.amazonaws.com/ubuntu/12.04/x86_64/chef-server_11.0.10-1.ubuntu.12.04_amd64.deb

Agora vamos executar a instalação.

.. code-block:: shell

    # dpkg -i chef-server_11.0.10-1.ubuntu.12.04_amd64.deb

Pronto seu Chef server está instalado, vamos configura-lo.

Mas primeiro, *o grande segredo que me fez escrever esse post* para uma instalação bem sucedida.

Para o Chef server é necessário que o hostname e hosts seja o seu FQDN ou seja:

.. code-block:: shell

    # vim /etc/hosts

Deixe as linhas de seu arquivo parecida com essas.

.. code-block:: shell

    127.0.0.1 localhost chef
    127.0.0.2 chef.jesuejunior.com chef

    # The following lines are desirable for IPv6 capable hosts
    ::1 ip6-localhost ip6-loopback
    fe00::0 ip6-localnet
    ff00::0 ip6-mcastprefix
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters

E mudaremos o hostname da mesma forma.

.. code-block:: shell

    # vim /etc/hostname

Verifique o nome do seu servidor e/ou altere, caso seja necessário.

.. code-block:: shell

    chef.jesuejunior.com

Após a instalação ser concluída com sucesso e ter feito o *segredo do sucesso*, precisamos executar o comando para
instalar/configurar as dependências do chef-server.

.. code-block:: shell

    # chef-server-ctl reconfigure

OBS: Essa instalação precisa de muita memória, na primeira tentativa apareceu esse erro:

.. code-block:: shell

    "FATAL: Errno::ENOMEM: Cannot allocate memory - fork(2)"

Mas não se desespere, no meu caso precisei usar uma instancia com poucos recursos e esse erro se da por falta de memória, por padrão as instancias do
*Digital Ocean*  não vem com o SWAP habilitada, então siga esse tutorial (`aqui <http://www.jesuejunior.com/criando-um-arquivo-como-memoria-swap>`__) 
para habilitar um swap dentro de um arquivo em disco.

Depois de ter criado um pouco mais de *memória* para o processo,  execute o comando novamente, sua instalação vai exibir a seguinte mensagem:

|image1|

Já comecei a redigir o próximo post que será a parte da configuração de repositório para adicionar cookbooks, roles e sua chave para acessar o
server, configurar seu knife.rb, ou seja a configuração para quem vai trabalhar com o chef.

Espero que possa ser útil, qualquer duvida não deixe de perguntar.

.. |image0| image:: http://blog.jesuejunior.com/wp-content/uploads/2013/12/my_Chef_Logo.png
   :target: http://blog.jesuejunior.com/wp-content/uploads/2013/12/my_Chef_Logo.png
.. |image1| image:: /img/chef/prompt-install-chef-server.png
   :target: /img/chef/prompt-install-chef-server.png
