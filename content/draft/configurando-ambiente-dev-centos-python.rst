:title: Configurando um ambiente de desenvolvimento para Python com CentOS
:author: jesuejunior
:lang: pt
:translation: true

Recentemente fui convidado para um novo desafio, mas quando cheguei lá eu vi que era um mega
desafio. 


Fazendo um update inicial.

.. code-block:: shell
    $ sudo yum update -y
Começando a instalação das dependencias para ter um bom ambiente de desenvolvimento.

.. code-block:: shell
    $ sudo yum -y install gcc kernel-devel kernel-headers make bzip2 cmake epel-release
    tmux dkms perl python-devel mysql-devel net-tools htop vim zsh git python-pip



.. code-block:: shell
    $ sudo pip install --upgrade pip

.. code-block:: shell
    $ sudo pip install virtualenvwrapper docker-compose ansible

.. code-block:: shell
    $ sudo tee /etc/yum.repos.d/docker.repo <<-'EOF'
    [dockerrepo]
    name=Docker Repository
    baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
    enabled=1
    gpgcheck=1
    gpgkey=https://yum.dockerproject.org/gpg
    EOF


 Instalando e configurando o docker.

.. code-block:: shell
     sudo yum update && \
     sudo groupadd docker && \
     sudo yum install -y docker-engine && \
     sudo usermod -aG docker vagrant && \
     sudo service docker start && \
     sudo chkconfig docker on 


  Clonando o repositorio que tem umas configurações iradas que eu cultivo.

.. code-block:: shell
    $ git clone https://github.com/jesuejunior/dotfiles.git --recursive 


.. code-block:: shell
    $ cd dotfiles

.. code-block:: shell
    $ bash bootstrap.sh


Instalando python 3.5

.. code-block:: shell
    $ sudo yum install yum-utils

.. code-block:: shell
    $ sudo yum-builddep python

.. code-block:: shell
    $ curl -O https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz

.. code-block:: shell
    $ tar xf Python-3.5.0.tgz
    $ cd Python-3.5.0
    $ ./configure
    $ make
    $ sudo make install



.. code-block:: shell
    $ sudo yum-builddep python

.. code-block:: shell
    $ curl -O https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz

.. code-block:: shell
    $ tar xf Python-3.5.0.tgz
    $ cd Python-3.5.0
    $ ./configure
    $ make
    $ sudo make install



.. code-block:: shell
    $ sudo yum-builddep python

.. code-block:: shell
    $ curl -O https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz

.. code-block:: shell
    $ tar xf Python-3.5.0.tgz
    $ cd Python-3.5.0
    $ ./configure
    $ make
    $ sudo make install

Confirmando a versão do python 3

.. code-bloxk:: shell
    $ python3 --version


Limpando os caches do centos após as isntalações

.. code-block:: shell
    $ sudo yum clean all
