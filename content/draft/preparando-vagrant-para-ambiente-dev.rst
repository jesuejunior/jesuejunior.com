.. code-block:: shell
  
  $ sudo wget -c http://download.virtualbox.org/virtualbox/5.0.16/VBoxGuestAdditions_5.0.16.iso \ 
  -O VBoxGuestAdditions_5.0.16.iso

.. code-block:: shell
  
  $ sudo mount VBoxGuestAdditions_5.0.16.iso -o loop /mnt

.. code-block:: shell

  $ cd /mnt

.. code-block:: shell
  
  $ sudo sh VBoxLinuxAdditions.run --nox11

.. code-block:: shell
  
  $ sudo rm *.iso

Versões de VirtualBox disponiveis.

- http://download.virtualbox.org/virtualbox
