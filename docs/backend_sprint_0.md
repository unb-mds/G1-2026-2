[README.md](https://github.com/user-attachments/files/31618279/README.md)
# Aprendizado Back-end

## Começo
Para começar, precisei decidir primeiro a linguagem e o framework que iria utilizar. Pelo que observei nos projetos anteriores, tive duas escolhas principais: FastAPI com Python ou NestJS e suas diversas APIs. Eu escolhi FastAPI com Python, pois já conheço a linguagem. Além disso a diferença principal entre as opções, que seria a performance, não valeria a pena considerando o escopo atual do projeto, e tambem a dificuldade de aprender uma nova linguagem.

## FastAPI
Ao utilizar o FastAPI, antes  de começar, é recomendado o uso da biblioteca Pydantic. Essa extensão faz com que o Python tenha tipagem de dados explícita, de forma semelhante ao Java ou C. Ou seja, para declarar uma variável, é necessário definir o tipo dela. Isso ajuda a entender o código, pois deixa claro qual é o tipo esperado nos métodos, além de fazer com que o programa apresente um crash caso receba a tipagem errada. Isso é muito melhor do que deixar o programa rodar com o tipo de dado incorreto e dar erro mais tarde.

Uma das principais vantagens desse framework é a adaptação automática de dados em JSON para os modelos do Pydantic, o que facilita bastante a entrada e a saída de dados.E ele tem uma excelente integração com o SQLModel, sobre o qual falarei mais à frente.

Para testar o servidor,é possivel usar o uvicorn, com o sequinte comando: 

uvicorn nome_python:app --reload

Para estruturar a aplicação, utilizamos o decorador `@app`, que precisa ser declarado logo no início do código com `app = FastAPI()`. Esse recurso é usado para criar os endereços do site, além de gerenciar as funções de *input* e *output*, sendo bem simples de entender. 

Por exemplo, ao usar `@app.get("/endereco_site/{input}")`: o método `get` indica que o sistema deve buscar uma informação quando o cliente acessar aquele endereço, e ele também pode receber um *input*, o qual podemos usar para procurar um dado específico. Se quiser mais detalhes, a própria documentação deles é excelente: [https://fastapi.tiangolo.com/learn/](https://fastapi.tiangolo.com/learn/).

## SQLModel
Eu usei o SQLModel junto com o SQLite para criar um banco de dados rápido. Nessa fase inicial, criei tudo usando apenas um arquivo local db, o que foi bem fácil de implementar. O SQLModel adapta as classes criadas no Pydantic automaticamente para as tabelas do banco de dados. Além disso, as funções do session são bastante intuitivas de usar: primeiro você adiciona, depois faz o `commit` e, por último, executa um refresh. Também recomendo a documentação oficial do SQLModel: [https://sqlmodel.tiangolo.com/learn/](https://sqlmodel.tiangolo.com/learn/).
