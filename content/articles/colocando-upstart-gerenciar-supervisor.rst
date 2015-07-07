Colocando Upstart para gerenciar o Supervisor
#############################################
:date: 2013-12-14 03:22
:author: jesuejunior
:category: Debian, Linux, ubuntu
:tags: Linux, supervisord, ubuntu, upstart
:slug: colocando-upstart-gerenciar-supervisor


Depois de um tempo afastado do Blog, estou  organizando melhor o uso do
meu tempo, ou seja, em breve estarei criando mais posts que inclusive já
tenho alguns em rascunho.

Hoje faço parte de uma equipe de devOps. Então cada vez utilizo mais
desenvolvimento para resolver problemas de deploy, escalabilidade entre
outros. Baseado nisso, recentemente implementei na receita do Chef para
o `Upstart <http://upstart.ubuntu.com/>`__ controlar o `Supervisord <http://supervisord.org/>`__.

 

-   Mas o que é o Supervisord?

Supervisor é um sistema client /server que permite que seus usuários
possam monitorar e controlar um número de processos que podem ser grupos
de processos.

-  Mas o que é o Upstart?

Upstart é daemon de substituição ao /sbin/init  que lida com a
inicialização de tarefas e serviços durante o boot, impedindo-os durante
o desligamento e supervisionando-os enquanto o sistema está funcionando.
E como ele está no nível init (embutido no kernel), seu processo
dificilmente ficará desligado. Por exemplo, caso seu processo apresente
erro e feche o upstart vai tentar reinicia-lo e caso não consiga, vai
continuar tentando no intervalo de tempo pré-configurado.

Pois bem, aqui vou mostrar como implementar manualmente o que já é de
muita ajuda se você precisar de algo controlando um grupo de processos e
não deixando-os morrerem.

OBS: Estou assumindo que o sistema operacional é baseado em Debian

Parando e removendo o supervisorD do boot
=========================================

.. code-block:: shell

    $ sudo /etc/init.d/supervisord stop

.. code-block:: shell

    $ sudo update-rc.d -f supervisor remove

Este ultimo comando remove o arquivo **/etc/init.d/supervisord** e caso
queira voltar ao modo antigo de troque o *remove* por *enable.*

Criando um script Upstart
=========================

Crie um arquivo  **/etc/init/supervisor.conf**.  Com o seguinte
conteudo:

.. code-block:: shell

    description "supervisor" 

    start on runlevel [2345] 

    stop on runlevel [!2345] 

    respawn 

    exec /usr/local/bin/supervisord --nodaemon --configuration /etc/supervisord.conf

Perceba que nós estamos usando o mesmo *supervisord*, logo não há nada
para mudar aqui. hehehe

usando supervisord com upstart
==============================

Nós podemos iniciar e parar o **supervisord** com os comandos padrões do
**Upstart**:

.. code-block:: shell

    $ sudo stop supervisor

.. code-block:: shell

    $ sudo start supervisor

Para verificar o status do \ *supervisor, faça:*

.. code-block:: shell

    $ initctl list

.. code-block:: shell

    $ initctl status supervisor

HERE WE GO!
===========

Confirmando que o supervisor está sendo executado, os comandos para
gerencia-lo não mudam em nada, continuamos a ter o  **supervisorctl**  e
podemos ver os processos que ele está controlando, pois continuamos
usando o mesmo arquivo de configuração padrão que fica em
*/etc/supervisord.conf.*

Então é isso, qualquer duvida não deixe de postar nos comentários, será
um prazer ajudar.

