:title: Instalando e configurando Chef Client(knife)
:date: 2014-02-25 00:08
:author: jesuejunior
:category: CD, Chef, CI, Linux
:tags: chef, chef-client, chef-server, Continuos Deploy
:slug: configurando-chef-client

O Chef, resolvi  escrever o post que havia prometido.

Acreditando fortemente que você já passou por
`aqui <http://jesuejunior.com/instalando-chef-server>`__ e já tem
o Chef Server instalado.

**Sugestão 1:** Instale o tmux vim curl wget com o comando abaixo ou
equivalente a sua distribuição.

.. code-block:: shell

    $ apt-get install tmux vim curl wget

**Instalando e configurando sua workstation.**

Embora uso Macbook(OSX) estarei fazendo toda a configuração de um
Ubuntu, peço que fiquem atento aos paths caso seu equipamento de
trabalho seja um Mac.

Download do *Chef Omnibus installer* e já passando no pipeline para a instalação:

.. code-block:: shell

    $ curl -O -L http://www.opscode.com/chef/install.sh | sudo sh install.sh

A parte legal do comando acima é que ele descobre sua distribuição e
instala o *chef-client* de acordo com o gerenciador de pacotes (RPM -
RHEL e DEB -Debian).

Criei uma pasta chamada *code* e depois trabalho de dentro da mesma, ou seja:

.. code-block:: shell

    $ mkdir code && cd code

Agora vamos clonar o repositório base do *Chef*.

.. code-block:: shell

    $ git clone https://github.com/opscode/chef-repo.git chef

Agora podemos ir acessar nosso *Chef Server* no browser, com o endereço
FQDN que você já tem configurado, no meu caso ficou
[STRIKEOUT:https://chef2.cloudfish.in.]

Agora precisamos re-gerar as chave privada \ *chef-validator.*

No menu, vá em  **Clients > chef-validator > Edit,** Marque a
opção\ ** Regenerate Private Key**, e clique em **Save Client.** Agora
copie a nova chave privada para *~/code/chef/.chef/chef-validator.pem*
na sua maquina.

**Sugestão 2:** Não colocar suas permissões de de acesso/execução
(knife.rb e \*.pem) no *repositório, geralmente o que eu faço e todos
amigos que trabalham comigo é, cada um coloca na sua home ~/.chef/,* mas
isso fica a critério de organização, e não esqueça que fazendo isso as
configurações dentro do seu knife.rb mudaram\ *.*

Agora vamos criar um usuário que fará o gerenciamento do chef.

Clique na Aba \ **Users > Create,** marque a opção **Admin,** preencha
*username* e *senha* eu estou criando um usuário chamado ***jj*** para o
exemplo, fique atento a isso e depois clique em **Create User.**

Vamos copiar a chave privada do nosso novo usuário, clique  em Users >
edit > do usuário ***jj***, irá aparecer  a sua chave publica e privada,
copie a privada para ~/code/chef/.chef/jj.pem.

OBS: Note que você é advertido, pois a chave privada só pode ser
acessada uma única vez, like AWS.

Finalmente, abra seu terminal e vamos rodar o ***knife
configure.*** Preencha os campos a seguir conforme sua necessidade,
segue uma imagem para ilustrar e tirar supostas duvidas que possa surgir.

.. code-block:: shell

    $ knife configure

|image0|

Neste ponto que e a configuração do knife conecta com a interface do
nosso servidor Chef Open Source que você já tem instalado anteriormente.
Para testar vamos rodar um comandos basicos para listar a lista de
clientes cadastrados e a lista de nodes(servidores).

|image2|

Não se esqueça que você precisa está no seu repositório para quando for
usar o comando *knife* para conectar no seu Chef server. ë planamente
possível se conectar em vários Chef server, pois o que manda é onde está
o seu *.chef/knife.rb* e suas chaves. A principio seria necessário
apenas ter outro clone do repositório base e gerar os arquivos de
configuração, assim quando fosse executar os comandos você entraria no
diretório/repositório responsável por cuidar de tal servidor.

Referência
`Install Chef 11.x on a  Workstation <http://docs.opscode.com/chef/install_workstation.html>`__


.. |image0| image:: /img/chef/command_knife_configure.jpg
   :target: /img/chef/command_knife_configure.jpg
.. |image2| image:: /img/chef/knife-list.png
   :target: http://jesuejunior.com/img/chef/knife-list.png
