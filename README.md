# Example of a Bookstore using FastAPI

You can use this example as a simple application to be used in the technical test of DevOps.

## Run

```bash
git clone git@github.com:ahioros/Bookstore-demo.git
cd Bookstore-demo
python -m venv venv
```

```bash
source venv/bin/activate
export DATABASE=mydatabase.db
export SECRET_TOKE="SUPER_SECRETPASSW0RD"
pip install -r requirements.txt
python app.py
```

Open http://localhost:8000 in your browser:

http://localhost:8000/secret

http://localhost:8000/books/

## Extra info

Insert a new book

```bash
curl -X POST http://localhost:8000/books/ -H "Content-Type: application/json" -d '{
"title": "New book title",
"author": "Author of the book",
"topic": "Topic of the book"
}'
```

Update book info

```bash
curl -X PUT http://localhost:8000/books/1 -H "Content-Type: application/json" -d '{
"title": "Title update",
"author": "Author update",
"topic": "Topic Update",
"id": "1"
}'
```

Delete book

```bash
curl -X DELETE http://localhost:8000/books/1 -H "Content-Type: application/json" -d '{}' "
```

## TEST

```bash
pytest -v
```

## Tasks

- Create a container image, use everything you need:

  - env vars,
  - run user,
  - port,
  - healthcheck,
  - etc.

- Create a CI Pipeline:

  - Code Build
  - Unit Test
  - Static Code analysis
  - Code Coverage
  - Build and Push the container image.
  - Optional:
    - Vulnerability scanning
    - Add more test if you need

- Deploy the container image to a Kubernetes cluster, cloud provider (AWS, GCP, Azure) or on-premise (minikube, k3s, etc.):

  - Use all the resources you need
  - 2 replicas
  - HPA
  - Configmaps
  - Secrets
  - Ingress
  - Etc.

- Add the deploy pipeline to the CI pipeline

- Create a Documentation file README.md and add:

  - Diagrams
  - If you deploy to AWS, GCP, etc., add the link to the cluster

## Revision:

- Correct image creation
- Good practice on kubernetes resources
- Good practices on CI/CD pipeline
- Good documentation and diagrams.
- If you could not fulfill any task, please indicate the reason for it

Extra points:

- Create a Docker Compose file
- If you use IaC tools, add the apply/outputs, CloudFormation (events/resources), etc.

## License

GPL
