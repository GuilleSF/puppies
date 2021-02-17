if [ ! -d "venv" ]; then
    echo --------------------
    echo Creating virtualenv
    echo --------------------
    python3.9 -m venv env
fi
source venv/bin/activate

pip install -r requirements.txt