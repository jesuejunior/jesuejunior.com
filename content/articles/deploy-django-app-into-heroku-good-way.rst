Migrando Django app para o heroku (Tips and Tricks) 
###################################################
:date: 2016-12-12
:author: jesuejunior
:category: Heroku, Django, Web, app, Deploy, PostgreSQL
:tags: Heroku, Django, Web, DevOps, PostgreSQL, Deploy
:slug: deploy-app-into-heroku-the-good-way
:lang: pt-br
:translation: true

Cenário
-------

Faz um bom tempo que tenho alguns servidores na `Digital Ocean`_ , tenho um em específico que está 
com pouco mais de 1 ano de uptime com alguns serviços(sites, blogs e webapps) meus e de clientes, com
docker e sem docker. :)

Percebi que tinham algumas apps nesse servidor que eu poderia migrar para um serviço *gratuito* 
ou até mesmo desligar. Um forte candidato para as migrações seria o heroku, AWS Free Tier ou GCP Free. 
Eu já havia trabalhado há um tempo atrás com o heroku e sabia que seria bem simples fazer essa migração,
pois as minhas aplicações já eram baseadas no 12factor_, então seria tranquilo e 
diferente do AWS Free Tier ou GCP Free Tier, a aplicação ficará ativa sem cobranças mesmo depois de 1 ano. :)

O droplet escolhido.

|image0|

A Aplicação
-----------

Está aplicação web que desenvolvi para um amigo é basicamente um registro de blocos de granito
para exportações, bem simples, vincula uma identificação de nota fiscal ao código gerado para
o bloco a ser exportado. Uma Aplicação muito simples usando Django, PostgreSQL e Bootstrap.

Algumas telas responsivas para utilizar via celular.

|image2|

O deploy
--------

Construí um docker-compose.yml que tem todas as configurações necessárias e o provisionamento da
instância é executado via ansible, onde é instalado o Docker Engine e algumas configurações adicionais. 

**docker-compose.yml**

.. code-block:: yaml

    stone:
    image: jesuejunior/stone
    environment:
        MEMCACHED_HOST: memcached
        DATABASE_HOST: postgres
    env_file:
        - stone.env
    links:
        - memcached:memcached
        - postgres:postgres

    nginx:
    image: jesuejunior/nginx:latest
    ports:
        - "80:80"
    expose:
        - 80
    links:
        - stone:app
    volumes:
        - /stone/static/collect:/app/static:rw

    postgres:
    image: postgres:9
    env_file:
        - stone.env
    ports:
        - "5432:5432"
    volumes:
        - /opt/postgresql/data:/var/lib/postgresql/data:rw

    memcached:
    image: memcached
    ports:
        - "11211:11211"
    expose:
        - 11211

Resultado
+++++++++

|image1|

Porque Heroku?
--------------

Heroku é uma plataforma bastante madura que chegou apenas para resolver um problema específico,
conseguir fazer deploy de aplicações Ruby de forma simples e permiti-las escalar de forma simples.

Mas a plataforma evoluiu muito! Para saber mais como funciona hoje recomendo a leitura de |heroku_works|.

Com a constante criação e evolução de startups muito pequenas que muitas vezes têm apenas 1
desenvolverdor, a velocidade e simplicidade do Heroku se mostra a frente de um leve custo
adicional.
Se você precisa fazer um deploy para demonstrar algo novo, ou se você não quer perder tempo configurando
a infraestrutura, eliminar a necessidade de equipe de infraestrututra.

É possivel fazer a maioria das ações via web, acompanhar sua aplicação com métricas, logs e etc.
A facilidade para conseguir fazer um deploy e/ou escalar uma aplicação ou um banco de dados, é
surpreendente, alguns detalhes mudaram bastante, como a forma de *ligar* a aplicação ao banco de
dados(PGSQL) ou ao cache(Redis).

A plataforma é executada dentro sobre a AWS e você acaba pagando alguns centavos a mais pela
comodidade, nada mais justo, certo?

Então você pode criar sua conta sem precisar adicionar o cartão de crédito diretamente no site do
heroku_.

Vamos por a mão na massa!

Instalando o heroku toolbelt
----------------------------

O que é o toolbelt_ ?

Simples, é o gerenciador do heroku via command-line, com ele você conseguirá gerenciar toda a suas
aplicações, serviços e opções que podem ou não estar disponíveis na versão web, de forma que com o
CLI você consegue automatizar tarefas de deploy, auto-scaling e etc.

Instalar no macOS é tão simples quanto no linux se você usa o *brew*.

.. code-block:: shell

    > brew install heroku

E pronto! Agora é só efetuar o login com sua conta previamente criada e seguir o step-by-step.

.. code-block:: shell

    > heroku login

Escolher a versão do python
---------------------------

O Heroku tem disponibilidade em usar as duas versões do Python, que são 2 e 3.

Para definir a versão é necessário adicionar o arquivo *runtime.txt* com o seguinte conteúdo e 
no mesmo diretório que seu *Procfile*.

.. code-block:: shell

   > cat runtime.txt
   python-3.6.1

Por default o Heroku assume o python 2, mas se quiser usar  Python 3 basta trocar a versão no
arquivo *runtime.txt*.

Configurar as variaveis de ambiente
-----------------------------------

Conforme mostrado no docker-compose eu já tinha um arquivo de variáveis de ambiente. Então via
terminal consegui configurar com o seguinte comando:

.. code-block:: shell

    cat stone.env | awk '{print}' ORS=' ' | xargs heroku config:set

Resultado
+++++++++

|image3|

Mas se você preferir, existe a possibilidade de ser configurado via painel conforme imagem acima.
E ao executar uma alteração via painel imediatamente será refletida na sua aplicação.

Fazendo o sync do banco
-----------------------

Essa parte eu fiz um pouco diferente, mas gostaria de deixar a dica para casos que precisamos
colocar a aplicação do zero e executar o primeiro *migrate*.

Como sabemos o *Django* tem uma *feature* de migração de banco de dados muito precisa e concisa,
sempre que mudamos nosso *model*, precisamos gerar o que chamamos de *migration*, dessa forma
faremos nosso banco de dados refletir as novas alterações que precisamos.

No meu caso como tenho apenas uma aplicação, não precisei passar o nome como parâmetro, ou seja, o
comando a ser executado é o seguinte:

.. code-block:: shell

    $ heroku run python manage.py syncdb

Output:

.. code-block:: shell

    Running python manage.py syncdb on ⬢ stoneblock... up, run.7008 (Free)
    ...

E pronto, suas tabelas e colunas estão criadas de acordo com sua aplicação.

Nota: *No meu caso eu simplesmente fiz dump e restore, falo um pouco de como conectar no PostgreSQL do
Heroku a partir do computador local final deste post.*

Agora vamos criar um superuser inicial.

.. code-block:: shell

    You have installed Django's auth system, and don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Username (leave blank to use 'u13302'): joaozinho
    Email address: stone@gmail.com
    Password:
    Password (again):
    Superuser created successfully.

É muito simples, não muda muito de quando se está trabalhando localmente e é isso que impresiona.

Adicionando domínio customizado.
--------------------------------

Claro que queremos uma url própria! Mas nesse ponto o Heroku exige que configuremos o cartão de
crédito, então entramos no painel e adicionamos o cartão, eles vão verificar se o cartão é valido
cobrando $1, mas pode ficar tranquilo, pois eles estornam o valor. :D


.. code-block:: shell

    > heroku help domains:add
    Usage: heroku domains:add HOSTNAME

    add domain to an app

    -a, --app APP       # app to run command against
    -r, --remote REMOTE # git remote of app to run command against
    --wait

A mensagem é igual tanto no terminal quanto via web, não tem para onde correr.

.. code-block:: shell
   
    > heroku domains:add stone.sixcodes.com
    Adding stone.sixcodes.com to ⬢ stoneblock... !
    ▸    Please verify your account in order to add domains (please enter a credit card) For more information,
    see https://devcenter.heroku.com/categories/billing Verify now at https://heroku.com/verify


Aqui você pode visualizar quando eles exigem |heroku_credit_card|.
Após adicionar o cartão de crédito

.. code-block:: shell

    > heroku domains:add stone.sixcodes.com
    Adding stone.sixcodes.com to ⬢ stoneblock... done
    ▸    Configure your app's DNS provider to point to the DNS Target stone.sixcodes.com.herokudns.com.
    ▸    For help, see https://devcenter.heroku.com/articles/custom-domains

    The domain stone.sixcodes.com has been enqueued for addition
    ▸    Run heroku domains:wait 'stone.sixcodes.com' to wait for completion


E então seu domínio estará pronto

.. code-block:: shell

    > heroku domains:wait stone.sixcodes.com                                                                                                                                          master [+       5] [9c9eb1e] (!)
    Waiting for stone.sixcodes.com... done

Conectando no PostgreSQL de fora do Heroku
------------------------------------------

Como havia falado anteriormente, precisei acessar o PostgreSQL diretamente do meu notebook, eis
que temos uma parte chata que ninguém te conta. Para conseguir conectar no PostgreSQL(heroku),
você precisa adicionar a seguinte querystring a sua string de conexão, desta forma permitindo a conexão:

.. code-block:: shell

    ?ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory


Bom é isso que gostaria de compartilhar. Dúvidas e sugestões, estou a disposição.


.. _Digital Ocean: http://www.digitalocean.com
.. _12factor: https://12factor.net
.. _heroku: https://www.heroku.com/
.. _toolbelt: https://devcenter.heroku.com/articles/heroku-cli

.. |heroku_works| raw:: html

    <a href="https://devcenter.heroku.com/articles/how-heroku-works" target="_blank"> How Heroku Works </a>

.. |heroku_credit_card| raw:: html

    <a href="https://devcenter.heroku.com/articles/account-verification#when-is-verification-required" target="_blank"> cartão de crédito </a>


.. |image0| image:: /img/heroku/do-panel-11m.png
    :scale: 100%
    :align: middle

.. |image1| image:: /img/heroku/docker-compose-do.png
    :scale: 100%
    :align: middle

.. |image2| image:: /img/heroku/stone_app.png
    :scale: 100%
    :align: middle

.. |image3| image:: /img/heroku/config-env.png
    :scale: 100%
    :align: middle
