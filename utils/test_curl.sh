curl -X POST -F 'dog_image=@00e9ed3fab1d2032603d1a90e557976f.jpg' 'http://127.0.0.1:5000/api/breed'
curl -X POST -F 'dog_image=@4ca18a5617593265513954b17b30f37a.jpg' 'http://127.0.0.1:5000/api/breed'
curl 'http://127.0.0.1:5000/api/breed'

read -p "Press [Enter] key to start backup..."