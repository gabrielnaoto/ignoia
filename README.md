## Install Python

    sudo apt-get install python3.7

## Install PIP

    apt install python3-pip

### Instalando pacotes necessários

Execute instale os arquivos do arquivo requirements.txt

    pip install -r -requirements.txt


## Install Apache

Install Apache

    $ sudo apt-get update
    $ sudo apt-get -y install apache2

Test that it works. You can use Firefox or just command line curl:

    $ curl -s localhost|grep title
     <title>Apache2 Ubuntu Default Page: It works</title>

Test page appears. Let’s remove the test page

    $ echo "Hello static" > /var/www/html/index.html

And verify it’s removed

    $ curl -s localhost
    Hello static

Now we have Apache web server installed, and we have replaced the static test page with a page that says “Hello static”.

## Install Python 3 mod_wsgi

Install the Python 3 version of the Apache WSGI module. Note the ‘-py3′ ending in the packet name.

    $ sudo apt-get install libapache2-mod-wsgi-py3

Restart Apache to use the new module

    $ sudo service apache2 restart

Check that your module is enabled

    $ apache2ctl -M|grep -i wsgi
    wsgi_module (shared)

## Create Apache VirtualHost for WSGI

With Apache, VirtualHost means a new website in the Apache installation. For example, terokarvinen.com and botbook.com are VirtualHosts in the same Apache installation.

Here, we create and enable a new VirtualHost for use with WSGI Python programming.

With Apache, we first create a VirtualHost in sites-available/, then enable it by linking from sites-enabled and restarting Apache daemon.

Create the new site. The name must end with “.conf”.

    $ sudoedit /etc/apache2/sites-available/ignoia.conf

Write the contents.

    <VirtualHost *:80>
        ServerName ignoia.example.com

        WSGIScriptAlias / /home/ignoia/ignoia.wsgi
        <Directory /home/ignoia/>
            Require all granted
        </Directory>

    </VirtualHost>

Only WSGIScriptAlias is specific to WSGI. Otherwise, everything looks just like any VirtualHost setup. In fact, the only change for a static web site would be using DocumentRoot directive in place of WSGIScripAlias.

WSGIScriptAlias tells the ULR path “/” should be handled by a Python program “/home/terowsgi/public_wsgi/tero.wsgi”. So when a users Firefox address bar shows “http://terowsgi.example.com/”, Apache mod_wsgi will call tero.wsgi Python program.

The sites (VirtualHosts) in sites-available/ are not used until they are linked from sites-enabled/. There is a inconvenience command to do this

    $ sudo a2ensite ignoia.conf


We just modified some configuration under /etc/. As always, we must restart the daemon for the changes to take effect.

    $ sudo service apache2 restart

## Criando arquivos de variáveis de ambiente

Você pode definir as variáveis de ambiente através do próprio OS, entretanto, você também pode criar um arquivo .env na mesma pasta que o arquivo manage.py contendo as seguintes informações

    EMAIL_HOST_USER=ainscricao77@gmail.com
    EMAIL_HOST_PASSWORD=ynCnM6Ax
    DEBUG=False

## Configurando o banco de dados

Para você configurar outro banco de dados a não ser o sqlite, você deverá instalar o banco de dados necessário, instalar o pacote do python que faz a conexão com o banco desejado, definir as credenciais de acesso no arquivo de variáveis de ambiente através da variável DATABASE_URL, seguindo o padrão a seguir:

https://github.com/kennethreitz/dj-database-url

Para criar a estrutura do banco de dados, você precisa executar as migrações

    python manage.py migrate


Links úteis:

https://python.org.br/instalacao-linux/
https://www.tecmint.com/install-pip-in-linux/
http://terokarvinen.com/2017/write-python-3-web-apps-with-apache2-mod_wsgi-install-ubuntu-16-04-xenial-every-tiny-part-tested-separately
https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-debian-8
https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04
https://docs.djangoproject.com/pt-br/2.1/howto/deployment/wsgi/
http://pythonclub.com.br/configurando-ambiente-django-com-apache-e-mod-wsgi.html



