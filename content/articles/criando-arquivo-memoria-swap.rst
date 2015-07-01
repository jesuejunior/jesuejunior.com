:title: Criando um arquivo como memória SWAP
:date: 2013-12-19
:tags: swap, memoria, linux, ubuntu
:category: sysadmin
:summary: Criando um arquivo como memória SWAP

Esse post é mais uma dica rápida do que um post super completo, mas recentemente precisei criar um arquivo como swap, pois o servidor já estava em produção e não tinha mais partição disponível.

No exemplo, criaremos um arquivo em /mnt chamado mem.swap:

$ sudo dd if=/dev/zero of=/mnt/mem.swap bs=1M count=4096
4096 é o tamanho do arquivo/partição.
Daí seguiremos com a criação do sistema de arquivos no arquivo alvo:

$ sudo mkswap /mnt/mem.swap
E ativamos a nova SWAP:

$ sudo swapon /mnt/mem.swap
No ultimo comando ativamos a partição e já está funcionando, então para tornar as mudanças definitivas, ou seja, para que essa SWAP esteja disponível para uso do sistema a cada reinicialização, adicionaremos uma entrada no arquivo /etc/fstab assim:

$ sudo vim /etc/fstab

/mnt/mem.swap swap swap defaults 0 0
Feito isto basta reiniciar o sistema e testar com o comando:

$ free -m

	Modo hardcore?

	$ sudo dd if=/dev/zero of=/mnt/mem.swap bs=1M count=4096 &&
	sudo mkswap /mnt/mem.swap &&
	sudo swapon /mnt/mem.swap &&
	sudo echo '/mnt/mem.swap swap swap defaults 0 0' >> /etc/fstab

E pronto já vai estar tudo pronto, mas de qualquer forma sugiro ler todo o post para entender oq eu foi feito, caso queira desfazer no futuro.