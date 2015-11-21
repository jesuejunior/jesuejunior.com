Instalando o Opera no Debian 6
##############################
:date: 2012-05-25 23:30
:author: jesuejunior
:category: Debian
:tags: Debian
:slug: instalando-o-opera-no-debian-6

Certa fez precisei instalar o Opera no Debian , que é a
distribuição que adotei  para alguns dos servidores do trabalho,  porem
apenas um cliente usa com interface gráfica, então vou postar a dica
para eu não esquecer quando precisar novamente.

Instala através do repositório do próprio Opera para o debian…

.. code-block:: shell

    sudo vim /etc/apt/sources.list

Adiciona a linha no final:

.. code-block:: shell

    deb http://deb.opera.com/opera/ lenny non-free

salva e saia:

.. code-block:: shell

    wget -O - http://deb.opera.com/archive.key | apt-key add -

.. code-block:: shell

    sudo apt-get update && sudo apt-get install opera


Pronto! Agora é só testar.

