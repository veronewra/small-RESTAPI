sudo docker build --tag weavegrid .
mirror="/local_filesystem"
sudo docker run \
    -p 5000:5000 \
    --mount type=bind,source="/",target=$mirror \
    weavegrid \
    python3 -m flask --app "app:create_app(\"$mirror/$1\")" run --host="0.0.0.0"