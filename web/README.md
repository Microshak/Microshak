# web

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).





docker build -f Dockerfile -t web:latest .
docker run -p 8082:8082 -t web:latest 

docker tag web:latest microshak/web:latest
docker push microshak/web:latest

docker run -p 5001:8081 -t microshak/web:latest 




kubectl apply -f deployment.yaml



https://www.de-ny.com/services/