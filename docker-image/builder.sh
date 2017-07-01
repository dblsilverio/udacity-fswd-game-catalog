#!/bin/bash

echo "Building Game Catalog Docker Image"

echo "Preparing resources..."
mkdir resources/

cp ../setup.py resources/
cp -r ../catalog/ resources/

echo "Build image. This may take a while..."
docker build --tag game-catalog:1.0 . &>/dev/null

if [ $? -ne 0 ]; then
    echo "Error building image :)"
else
    echo "Success :)"

    docker ps -a | grep "game-catalog" &>/dev/null

    if [ $? -eq 0 ]; then
        echo "Container already exists."
        exit
    fi

    echo "Running container..."

    docker run --name game-catalog -d -p 5000:5000 game-catalog:1.0

    if [ $? -ne 0 ]; then
        echo "Error running container ='("
   else
        echo "Container is running =)"
    fi
fi

echo "Cleaning resources..."
rm -Rf resources/
