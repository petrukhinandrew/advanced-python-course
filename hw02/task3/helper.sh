docker build --tag 'example-img' .
docker run --name 'example' 'example-img'
docker cp example:app/example.pdf artifacts/
docker rm 'example'
