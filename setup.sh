sudo docker image build -t api-ratings:latest .

sudo docker run --rm --network host api-ratings:latest