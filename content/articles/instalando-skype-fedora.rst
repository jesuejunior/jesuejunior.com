Instalando o Skype no Fedora 15 64 bits
#######################################
:date: 2012-05-25 03:52
:author: jesuejunior
:category: fedora, Linux
:tags: fedora
:slug: instalando-skype-fedora

Bom esse é meu primeiro post, estou migrando do Ubuntu (Unity) para o
Fedora 15 (GNOME 3) e estou enfrentando alguns problemas basicos, já esperados.
E nessa jornada irei postando aqui, para eu lembrar posteriormente e talvez ajudar alguem.

Como no site do Skype não tem a versão nativa 64bits em RPM, só a 32
bits, criei esse ‘howto’ de como instalar o comunicador no Fedora 64 bits:

1 – Instale as dependências necessárias:

.. code-block:: shell

    yum install glibc.i686 alsa-lib.i686 libXv.i686 libXScrnSaver.i686
    qt.i686 qt-x11.i686 alsa-plugins-pulseaudio.i686 libv4l.i686 -y

2 – Baixe o pacote RPM 32bits no site do Skype:

.. code-block:: shell

    wget http://download.skype.com/linux/skype-2.2.0.35-fedora.i586.rpm

3 – Agora instale o pacote usando o yum, com o comando:

.. code-block:: shell

    yum --nogpgcheck localinstall skype-2.2.0.35-fedora.i586.rpm

Para utilizar é só ir ao menu ATIVIDADES > APLICATIVOS > SKYPE.

Espero que possa ajudar!
