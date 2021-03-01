echo ---------------
echo Move apache conf to:
echo     /etc/apache2/sites-available/puppies.conf
echo --------------
sudo cp puppies.conf /etc/apache2/sites-available/puppies.conf
echo ---------------
echo Enable apache linking conf to:
echo     /etc/apache2/sites-enabled/
echo --------------
sudo ln -s /etc/apache2/sites-available/puppies.conf /etc/apache2/sites-enabled/
echo ---------------
echo Reload Apache Server:
echo --------------
/etc/apache2/sites-enabled/
