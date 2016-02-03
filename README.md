# runner

make a runner from the host OS:
```bash
lxc-create -t download -n ubuntu-runner -- -d ubuntu -r trusty -a amd64
```

then start and attache to the container so we can install and set up.
```bash
lxc-start -n ubuntu-runner -d
lxc-attach -n ubuntu-runner
```
now that you are in the container, lets install the packages we need,
```bash
apt-get install git apache2 python3-dev python3-pip libapache2-mod-wsgi-py3 nodejs npm -y
pip3 install virtualenv
npm install forever -g
ln -s /usr/bin/nodejs /usr/bin/node
```
Add the runner user:
```bash
adduser runner --gecos "runner,0,0,0" --disabled-password
```

get the runner server:
```bash
git clone https://github.com/wmantly/runner.git /var/www/runner
chown -R runner:runner /var/www/runner
```

Set us the Apache vhost config file:
```bash
echo '<VirtualHost *:80>' > /etc/apache2/sites-available/runner.conf
echo '    WSGIDaemonProcess runner user=runner group=runner python-path=/var/www/runner:/var/www/runner/env/lib/python3.4/site-packages' >> /etc/apache2/sites-available/runner.conf
echo '    WSGIProcessGroup runner' >> /etc/apache2/sites-available/runner.conf
echo '    WSGIScriptAlias / /var/www/runner/project/wsgi.py' >> /etc/apache2/sites-available/runner.conf
echo '</VirtualHost>' >> /etc/apache2/sites-available/runner.conf
rm /etc/apache2/sites-enabled/000-default.conf
ln -s /etc/apache2/sites-available/runner.conf /etc/apache2/sites-enabled/runner.conf
```




