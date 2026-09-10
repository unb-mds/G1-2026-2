# API Contract: UNB CORE

Base path: `/api/v1`  
Formato: JSON  
Datas: ISO 8601

## Publicações institucionais

### `GET /publicacoes`

Lista publicações para consulta pública.

Query parameters opcionais: `termo`, `categoria`, `unidade`, `curso_id`, `estado` e `prazo`.

Resposta `200`:

```json
{
  "itens": [
    {
      "id": 1,
      "titulo": "Edital de exemplo",
      "resumo": "Resumo da publicação",
      "categoria": "edital",
      "unidade_responsavel": "Unidade da UnB",
      "url_oficial": "https://exemplo.unb.br/edital",
      "estado": "ativa",
      "ultima_verificacao": "2026-09-09T10:00:00Z"
    }
  ]
}
```

### `GET /publicacoes/{id}`

Retorna detalhes, fonte, estado, datas e aviso de que o canal oficial prevalece em caso de divergência.

### `POST /publicacoes`

Cria uma publicação manualmente. Requer perfil `administrador`.

### `PATCH /publicacoes/{id}`

Atualiza classificação, estado, datas, resumo ou data de verificação. Requer perfil `administrador`.

### `GET /fontes`

Lista fontes institucionais cadastradas. Requer perfil `administrador`.

### `POST /fontes`

Cadastra uma fonte institucional. Requer perfil `administrador`.

### `GET /categorias`

Lista categorias disponíveis para publicações e conteúdos.

### `POST /categorias`

Cadastra uma categoria. Requer perfil `administrador`.

### `POST /disciplinas`

Cadastra uma disciplina vinculada a um curso. Requer perfil `administrador`.

### `PATCH /disciplinas/{id}`

Atualiza nome, código ou estado de uma disciplina. Requer perfil `administrador`.

## Base acadêmica

### `GET /cursos/{curso_id}/disciplinas`

Lista disciplinas ativas de um curso.

### `GET /disciplinas/{disciplina_id}/conteudos`

Lista conteúdos publicados de uma disciplina. Pode receber `tipo` como filtro.

### `GET /search`

Busca unificada em conteúdos acadêmicos e publicações institucionais. A resposta separa os dois grupos:

```json
{
  "conteudos_academicos": [],
  "publicacoes_institucionais": []
}
```

## Autenticação

### `POST /auth/cadastro`

Cria a própria conta do estudante com nome, e-mail único e senha.

### `POST /auth/login`

Autentica o usuário e retorna a sessão ou token de acesso. Senhas não aparecem em respostas ou erros.

## Contribuições

### `POST /contribuicoes`

Cria uma contribuição para o usuário autenticado. O estado inicial é sempre `pendente`.

### `GET /contribuicoes/minhas`

Lista as contribuições do usuário autenticado com estado e justificativa de moderação, quando houver.

Uma contribuição sem `conteudo_id` representa criação de conteúdo; com `conteudo_id`, representa alteração.

### `POST /moderacao/contribuicoes/{id}/decisao`

Registra uma decisão de moderador. Corpo esperado:

```json
{
  "decisao": "aprovar",
  "justificativa": "Conteúdo revisado e adequado."
}
```

Decisões aceitas: `aprovar`, `ajustes`, `rejeitar`, `arquivar`.

## Denúncias

### `POST /publicacoes/{id}/denuncias`

Registra uma denúncia autenticada com tipo e descrição.

### `GET /denuncias`

Lista denúncias para moderadores e administradores.

### `PATCH /denuncias/{id}`

Atualiza o estado de uma denúncia. Requer perfil `moderador` ou `administrador`.

## Erros

Formato comum:

```json
{
  "erro": {
    "codigo": "PERMISSAO_NEGADA",
    "mensagem": "Voce nao possui permissao para executar esta acao.",
    "id": "string"
  }
}
```

Códigos mínimos: `VALIDACAO`, `NAO_ENCONTRADO`, `NAO_AUTENTICADO`, `PERMISSAO_NEGADA`, `FONTE_INDISPONIVEL` e `ERRO_INTERNO`.
