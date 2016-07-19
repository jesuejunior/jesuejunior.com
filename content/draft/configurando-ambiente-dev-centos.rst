:title: Configurando um ambiente de desenvolvimento com CentOS
:author: jesuejunior
:date: 2016-04-14 12:22
:lang: pt
:translation: true
:tags: centos, linux, vagrant, devops

Precisei trabalhar em uma estação *Windows*, porém com todas as ferramentas que funcionam melhor no Linux, 
como por exemplo Python, Mongo, RabbitMQ e etc.

Então uma possível *solução* ou *mitigação* era usar Vagrant(VirtualBox), mas existem outras 
soluções, eu optei por vagrant pois já conhecia e já havia usado anteriormente. :)

Vou tentar deixar um passo a passo de como deixar um _CentOS 7_ pronto para desenvolvimento.

Ao fim, você terá instalado: *vim(dev IDE), tmux, htop, zsh, docker, docker-compose, virtualenv(wrapper)*
e um conjunto completo de ferramentas para desenvolvimento.

Clonando o repositório(dotfiles) onde vou guardando configurações basicas do dia-a-dia para uma possível troca de PC.
Se notar que esse repositório já existe a bastante tempo e vou evoluindo a medida que vou precisando de mais configurações básicas.

.. code-block:: shell

    $ cd ~ && git clone https://github.com/jesuejunior/dotfiles.git --recursive

Vamos executar um script que fará algumas instalações e configurações essenciais que podem ser verificadas no github.

.. code-block:: shell

    $ cd dotfiles && bash bootstrap.sh

Aproveite a faça upgrade do *PIP*.

.. code-block:: shell

    $ sudo pip install --upgrade pip

Vamos instalar alguns pacotes essenciais via *PIP* como _root_.

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

Bônus
^^^^^

Esse script(bootstrap) já instala o python 3.5.0, porem fique a vontade para altera-lo.

Confirmando a versão do python 3

.. code-block:: shell

    $ python3 --version

Limpando os caches do centos após as instalações

.. code-block:: shell

    $ sudo yum clean all

Referências
+++++++++++

.. [1] -> https://www.vagrantup.com/
