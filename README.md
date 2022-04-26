# Maior número romano em uma string
A aplicação deve receber uma entrada do tipo string, e deve ser retornado o número de maior valor em algarismos romanos contido nessa entrada, por exemplo:

* input:
```json
{
    "text": "AXXBLX"
}
```
* output:
```json
{
    "number": "LX",
    "value": 60
}
```

#
## Setup
Para setup da aplicação via container, é necessário rodar o seguinte comando:
```bash
docker-compose up --build
```
A porta padrão da aplicação é 8080.

#
## Tecnologias
Para construção da aplicação, foi utilizada a linguagem Python com o framework [FastAPI](https://fastapi.tiangolo.com/), com as dependências [Uvicorn](https://www.uvicorn.org/) para implementação do server, [Pydantic](https://pydantic-docs.helpmanual.io/) para validação de requests, e [Strawberry](https://strawberry.rocks/) para integração com GraphQL. Além de [Roman](https://pypi.org/project/roman/) para os conversão dos algarismos romanos.

#
## REST
Para retorno dos dados via requisição de API REST:
* método: POST
* url: http://127.0.0.1:8080/search
* input:
```json
{
    "text": "AXXBLX"
}
```
* cURL da requisição:
```cURL
curl --request POST \
  --url http://127.0.0.1:8080/search \
  --header 'Content-Type: application/json' \
  --data '{
	"text": "AXXBLX"
}'
```

#
## GraphQL
Para retorno dos dados via requisição GraphQL:
* método: POST
* url: http://127.0.0.1:8080/graphql
* input:
```graphql
mutation {
    search(text: "AXXBLX") {
        number
        value
    }
}
```
* output:
```json
{
  "data": {
    "search": {
      "number": "LX",
      "value": 60
    }
  }
}
```
