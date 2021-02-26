sudo apt-get install python3-pip
pip3 install autoenv
echo "source 'which activate.sh'" >> ~/.bashrc
source ~/.bashrc
if [ ! -d "env" ]; then
    echo --------------------
    echo Creating virtualenv
    echo --------------------
    python3 -m venv env
fi
if [ -d "env/bin" ]; then
	echo --------------------
	echo env/env/bin
	echo --------------------
	source env/bin/activate
else
	echo --------------------
	echo env/Scripts
	echo --------------------
	source env/Scripts/activate
fi
pip install -r requirements.txt

echo --------------------
echo env variables
echo --------------------
export FLASK_APP=main.py
export APP_SETTINGS="config.DevelopmentConfig"
