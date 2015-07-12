Habilitando SSH no Fedora 15/16
###############################
:date: 2012-05-26 21:34
:author: jesuejunior
:category: fedora
:tags: fedora
:slug: habilitando-ssh-no-fedora

SSH é um protocolo de rede que permite que dados sejam trocados
através de um canal seguro entre dois dispositivos de rede. Partindo do
principio que você tenha uma nova instalação do Fedora 15, com a super
área de trabalho **GNOME 3**, e precisa descobrir como ativar o **SSH**.
Este artigo é simplesmente uma maneira de utilizar essa ferramenta
primordial para um linux user ou sysadmin. Para executar alguns dos
comandos que você precisa ter a senha da conta root.

Habilitando **SSH Daemon**
Primeiro de tudo, vamos nos certificar de que o daemon ssh está em  execução.
Abra o terminal e digite:

.. code-block:: shell

    $ sudo su

Password:

.. code-block:: shell

    # systemctl start sshd.service

Agora que o serviço foi iniciado, precisamos coloca-lo para iniciar
junto ao boot do sistema, para caso reinicie a maquina o SSH funcione normalmente.

.. code-block:: shell

    # systemctl enable sshd.service

Após executar o comando, aparecerá a mensagem. Isso quer dizer que funcionou!

    *sshd.service is not a native service, redirecting to  /sbin/chkconfig.*
	*Executing /sbin/chkconfig sshd on*

Verificando as configurações do Firewall
Por padrão a porta 22 vem aberta no firewall, mas é interessante verificar para não termos surpresas quando precisar-mos usar SSH.
Abra o system-config-firewall. Você pode acessar da seguinte forma também, acesse

**Atividades > Aplicativos > Firewall**

|image1|

Testando a conexão, abra gnome-terminal e digite:

.. code-block:: shell

	$ ssh user@hostname

Para conectar meu usuário é “jr” e meu computador (IP) 192.168.0.10.
Então digitamos o seguinte comando no terminal: ssh jr@192.168.0.10. O
terminal exibirá uma mensagem de ‘warning’:

.. code-block:: shell

	The authenticity of host ’192.168.0.10 (192.168.0.10)’ can’t be established.
	RSA key fingerprint is [some long identification number in 2-digit sequence]
	Are you sure you want to continue connecting (yes/no)?

Digite “yes”, Após digite a senha para o usuário “jr” e você estará conectado via SSH.

Então é isso.

.. |image1| image:: /img/firewall_fedora.png
   :target: /img/firewall_fedora.png
