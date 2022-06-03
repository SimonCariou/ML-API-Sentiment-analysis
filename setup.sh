docker image build -t api-ratings:latest .

docker run --rm --network host api-ratings:latest

docker-compose up --build
