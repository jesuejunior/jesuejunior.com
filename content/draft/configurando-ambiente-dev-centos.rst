:title: Configurando um ambiente de desenvolvimento com CentOS
:author: jesuejunior
:date: 2016-04-14 12:22
:lang: pt
:translation: true
:tags: centos, linux, vagrant, devops

Recentemente comecei em um novo desafio profissional e o primeiro **desafio** foi ter que trabalhar em uma estação
*Windows*, porém com todas as ferramentas que se sairiam melhor no universo Linux, como por exemplo Python,
Mongo, RabbitMQ e etc.

Então uma possivel *solução* ou *mitigação* era usar Vagrant(VirtualBox), mesmo já sabendo que haveria problemas
que poderiam impactar-me no futuro. Assumi o risco. :)

Vou tentar deixar um passo a passo de como deixar um CentOS pronto para desenvolvimento.

Ao fim, você terá instalado: *vim, tmux, htop, zsh, docker, docker-compose, virtualenv(wrapper) e etc*

Primeiro, faremos um update do sistema operacional.

.. code-block:: shell

    $ sudo yum update -y
    
Vamos começar instalando algumas dependências do centOS.

.. code-block:: shell

    $ sudo yum -y install gcc kernel-devel kernel-headers make bzip2 cmake epel-release
    tmux dkms python-devel mysql-devel net-tools htop vim zsh git python-pip


Aproveite a faça upgrade do *PIP*.

.. code-block:: shell

    $ sudo pip install --upgrade pip


Vamos instalar alguns pacotes essenciais via *PIP* como root.

.. code-block:: shell

    $ sudo pip install virtualenvwrapper docker-compose ansible


Iniciando a instalação e configuração do docker.

Adicionando o repositório do docker para *YUM*.

.. code-block:: shell

    $ sudo tee /etc/yum.repos.d/docker.repo <<-'EOF'
    [dockerrepo]
    name=Docker Repository
    baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
    enabled=1
    gpgcheck=1
    gpgkey=https://yum.dockerproject.org/gpg
    EOF

Pronto, agora que já temos o repositório do docker configurado, vamos realizar algumas configurações adicionais
e já deixar o docker-engine iniciando no boot do centOS.

OBS: Note que existe um *vagrant*, esse é o usuário padrão utilizado pelo *Vagrant* [1]_.

.. code-block:: shell

    $ sudo yum update && \ #Validando a adição do repositório.
    sudo groupadd docker && \ #Criando um grupo docker
    sudo yum install -y docker-engine && \ #Instalando o docker
    sudo usermod -aG docker vagrant && \ #Adicionando o usuário vagrant no grupo do docker para que possa executar o docker sem ser root
    sudo service docker start && \ #Iniciando o serviço do docker.
    sudo chkconfig docker on #Colocando o docker para ser iniciado no boot


Clonando o repositório(dotfiles) que tem umas configurações iradas que eu *cultivo*.

.. code-block:: shell

    $ cd ~ && git clone https://github.com/jesuejunior/dotfiles.git --recursive

.. code-block:: shell

    $ cd dotfiles

Vamos executar um script que fará algumas instalações e configurações essenciais que podem ser verificadas no github.

.. code-block:: shell

    $ bash bootstrap.sh


Bônus
^^^^^

Instalando python 3.5 no CentOS

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


Confirmando a versão do python 3

.. code-block:: shell

    $ python3 --version

Apagando arquivos pós instalação do Python 3

.. code-block:: shell

    $ cd ..
    $ rm -rf Python-3.5.0*

Limpando os caches do centos após as instalações

.. code-block:: shell

    $ sudo yum clean all

Referências
+++++++++++

.. [1] -> https://www.vagrantup.com/