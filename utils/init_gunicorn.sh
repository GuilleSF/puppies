echo ---------------
echo Move puppies service to:
echo     /etc/systemd/system
echo --------------
sudo cp puppies.service /etc/systemd/system/puppies.service
echo ---------------
echo Starting gunicorn service
echo --------------
sudo systemctl start puppies.service
sudo systemctl enable puppies.service
echo ---------------
echo Check status
echo --------------
sudo systemctl status puppies.service