:title: Configurando um ambiente de desenvolvimento com CentOS
:author: jesuejunior
:lang: pt
:translation: true

Vou tentar deixar um passo a passo para deixar um CentOS pronto para desenvolvimento.

Ao fim, você terá instalado: vim, tmux, zsh, docker, docker-compose, virtualenv(smart) e ansible

Fazendo um update inicial.

.. code-block:: shell

    $ sudo yum update -y
    
Começando a instalação das dependencias do centOS.

.. code-block:: shell

    $ sudo yum -y install gcc kernel-devel kernel-headers make bzip2 cmake epel-release
    tmux dkms python-devel mysql-devel net-tools htop vim zsh git python-pip


Aproveitando e já fazendo upgrade do `PIP`.

.. code-block:: shell

    $ sudo pip install --upgrade pip


Vamos instalar alguns pacotes essenciais via `PIP`como root.

.. code-block:: shell

    $ sudo pip install virtualenvwrapper docker-compose ansible


Iniciando a instalação e configuração do docker.

Adicionando o repositório do docker.

.. code-block:: shell

    $ sudo tee /etc/yum.repos.d/docker.repo <<-'EOF'
    [dockerrepo]
    name=Docker Repository
    baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
    enabled=1
    gpgcheck=1
    gpgkey=https://yum.dockerproject.org/gpg
    EOF

 Isso mesmo, vamos precisar realizar algumas configurações e já deixar o docker iniciando no boot do centOS.

 OBS: Note que tem um `vagrant` ali, pois estou fazendo essas configurações dentro de uma VM Vagrant.

.. code-block:: shell

    $ sudo yum update && \ #Validando a adição do repositório.
    sudo groupadd docker && \ #Criando um grupo docker
    sudo yum install -y docker-engine && \ #Instalando o docker
    sudo usermod -aG docker vagrant && \ #Adicionando o usuário vagrant no grupo do docker para que possa executar o docker sem ser root
    sudo service docker start && \ #Iniciando o serviço do docker.
    sudo chkconfig docker on #Colocando o docker para ser iniciado no boot



Clonando o repositório(dotfiles) que tem umas configurações iradas que eu _cultivo_.

.. code-block:: shell

    $ git clone https://github.com/jesuejunior/dotfiles.git --recursive

.. code-block:: shell

    $ cd dotfiles

Aqui vamos executar um script que fará algumas instalações e configurações essenciais. 

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

.. code-block:: shell

    $ python3 --version


Limpando os caches do centos após as isntalações

.. code-block:: shell

    $ sudo yum clean all
