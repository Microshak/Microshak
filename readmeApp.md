docker build -f Dockerfile -t web:latest .
docker run -p 5000:5000 -t web:latest 

docker tag web:latest microshak/web:latest
docker push microshak/web:latest

docker run -p 5000:5000 -t microshak/web:latest 




kubectl apply -f deployment.yaml



https://www.de-ny.com/services/