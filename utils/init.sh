cd ..
if [ ! -d "env" ]; then
    echo --------------------
    echo Creating virtualenv
    echo --------------------
    python3.9 -m venv env
fi
cd env
if [ ! -d "env/bin"]; then
	echo --------------------
	echo env/bin
	echo --------------------
	source bin/activate
else
	echo --------------------
	echo env/Scripts
	echo --------------------
	source Scripts/activate
fi
cd ..
pip install -r requirements.txt