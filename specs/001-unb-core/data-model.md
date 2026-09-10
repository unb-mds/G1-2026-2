# Data Model: UNB CORE

## Usuário

Representa uma pessoa que consulta o sistema e, quando autenticada, pode enviar contribuições.

- `id`: identificador único.
- `nome`: nome exibido.
- `email`: endereço único usado no acesso.
- `senha_hash`: senha armazenada de forma protegida; nunca deve ser retornada pela API.
- `perfil`: `usuario`, `moderador` ou `administrador`.
- `ativo`: indica se a conta pode acessar funções autenticadas.
- `criado_em`, `atualizado_em`: datas de controle.

Regras:

- O e-mail deve ser único.
- Qualquer conta ativa e autenticada pode enviar contribuição.
- Apenas moderadores podem decidir sobre contribuições.
- Apenas administradores podem cadastrar ou alterar publicações institucionais.

## Curso

Agrupa disciplinas e organiza filtros acadêmicos.

- `id`: identificador único.
- `nome`: nome do curso.
- `sigla`: sigla do curso.
- `ativo`: indica disponibilidade para consulta.

## Disciplina

Unidade curricular vinculada a um curso.

- `id`: identificador único.
- `curso_id`: referência ao curso.
- `codigo`: código da disciplina.
- `nome`: nome da disciplina.
- `periodo`: período ou semestre relacionado, quando aplicável.
- `ativo`: indica disponibilidade para consulta.

Relacionamento: um curso possui muitas disciplinas; cada disciplina pertence a um curso.

## Conteúdo acadêmico

Material publicado na Base de Conhecimento.

- `id`: identificador único.
- `disciplina_id`: disciplina relacionada.
- `tipo`: `resumo`, `dica`, `dificuldade`, `prova`, `implementacao` ou `link`.
- `titulo`: título do conteúdo.
- `corpo_ou_url`: texto ou endereço do material.
- `autor_id`: usuário responsável, quando aplicável.
- `origem`: fonte ou explicação de autoria.
- `estado`: conteúdo publicado ou arquivado.
- `criado_em`, `atualizado_em`: datas de controle.

## Contribuição

Proposta de criação ou alteração de conteúdo acadêmico.

- `id`: identificador único.
- `autor_id`: usuário autenticado que enviou a proposta.
- `conteudo_id`: conteúdo relacionado quando a proposta for uma alteração.
- `disciplina_id`: disciplina da proposta.
- `tipo`: tipo de conteúdo proposto.
- `payload`: dados submetidos para análise.
- `estado`: `pendente`, `ajustes`, `rejeitada`, `aprovada` ou `arquivada`.
- `justificativa_moderacao`: justificativa opcional da decisão.
- `criado_em`, `atualizado_em`: datas de controle.

Transições:

```text
pendente -> aprovada
pendente -> ajustes
pendente -> rejeitada
pendente -> arquivada
ajustes -> pendente
```

Uma contribuição aprovada cria ou atualiza o conteúdo acadêmico correspondente.

## Fonte institucional

Canal oficial utilizado pelo administrador como origem de publicações.

- `id`: identificador único.
- `nome`: nome da fonte.
- `unidade_responsavel`: órgão ou unidade da UnB.
- `url_base`: endereço principal.
- `estado`: `ativa`, `pausada` ou `indisponivel`.
- `ultima_verificacao`: data da última consulta conhecida.

## Publicação institucional

Edital, aviso ou comunicado cadastrado manualmente por um administrador.

- `id`: identificador único.
- `fonte_id`: fonte oficial relacionada.
- `titulo`: título da publicação.
- `resumo`: resumo apresentado no portal.
- `categoria`: edital, bolsa, monitoria, auxílio, processo seletivo, evento ou comunicado.
- `unidade_responsavel`: unidade que publicou a informação.
- `curso_id`: curso relacionado, quando aplicável.
- `url_oficial`: endereço da fonte original.
- `publicado_em`: data de publicação.
- `prazo_inicio`, `prazo_fim`: datas do prazo, quando informadas.
- `estado`: `ativa`, `nao_verificada` ou `sem_prazo`.
- `ultima_verificacao`: data da última consulta da fonte.
- `criado_em`, `atualizado_em`: datas de controle.

Regras:

- Uma publicação deve manter sua fonte oficial quando disponível.
- O estado `nao_verificada` deve ser visível para o usuário.
- O estado `sem_prazo` deve ser visível para o usuário.
- Apenas administradores podem criar ou alterar registros.

## Denúncia

Relato de problema em uma publicação ou conteúdo.

- `id`: identificador único.
- `autor_id`: usuário que realizou o relato, quando autenticado.
- `publicacao_id`: publicação relacionada, quando aplicável.
- `conteudo_id`: conteúdo relacionado, quando aplicável.
- `tipo`: erro, duplicidade, link quebrado ou desatualização.
- `descricao`: explicação do problema.
- `estado`: `aberta`, `em_analise`, `resolvida` ou `descartada`.
- `criada_em`, `atualizada_em`: datas de controle.

## Relacionamentos principais

- `Curso 1:N Disciplina`.
- `Disciplina 1:N Conteúdo acadêmico`.
- `Usuário 1:N Contribuição`.
- `Disciplina 1:N Contribuição`.
- `Fonte institucional 1:N Publicação institucional`.
- `Usuário 1:N Denúncia`.
- `Publicação institucional 1:N Denúncia`.
- `Conteúdo acadêmico 1:N Denúncia`.
