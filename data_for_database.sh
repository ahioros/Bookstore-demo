#!/bin/bash
curl -X POST http://localhost:8000/table/ -H "Content-Type: application/json" -d '{
"create": "True"
}'

curl -X POST http://localhost:8000/book/ -H "Content-Type: application/json" -d '{
"title": "Cien años de soledad",
"author": "Gabriel Garcia M",
"topic": "Fantasía"
}'

curl -X POST http://localhost:8000/book/ -H "Content-Type: application/json" -d '{
"title": "El coronel no tiene quien le escriba",
"author": "Gabriel Garcia M",
"topic": "Fantasía"
}'

curl -X POST http://localhost:8000/book/ -H "Content-Type: application/json" -d '{
"title": "IT",
"author": "Stephen King",
"topic": "Terror"
}'

curl -X POST http://localhost:8000/book/ -H "Content-Type: application/json" -d '{
"title": "The Mist",
"author": "Stepehen King",
"topic": "Terror"
}'
