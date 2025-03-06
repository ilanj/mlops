#load images to minikube
        minikube start

        * minikube image load fastapi-square:1.1  
        * kubectl apply -f deployment.yaml 
        * kubectl apply -f service.yaml 
        * minikube service fastapi-service

        from above command you could get a result like "🏃  Starting tunnel for service fastapi-service.
        |-----------|-----------------|-------------|------------------------|
        | NAMESPACE |      NAME       | TARGET PORT |          URL           |
        |-----------|-----------------|-------------|------------------------|
        | default   | fastapi-service |             | http://127.0.0.1:51619 |
        |-----------|-----------------|-------------|------------------------|

   goto    http://127.0.0.1:51619/docs for swagger ui

   # poetry commands
* pip install poetry
* poetry init
* portry lock
* poetry install --no-root
