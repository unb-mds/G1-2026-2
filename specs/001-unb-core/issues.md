# Issues de Implementacao: UNB CORE

**Fonte:** [plan.md](plan.md) e [tasks.md](tasks.md)  
**Branch:** `001-unb-core`  
**Data de geracao:** 2026-09-10

Este arquivo organiza as issues do plano por Sprint. Cada issue corresponde a uma fase de implementacao, preserva o milestone de produto e mantem os IDs das tasks originais para facilitar o acompanhamento.

## Sprints

| Sprint | Objetivo | Milestone | Issues |
|---|---|---|
| Sprint 0 | Preparar a estrutura e os componentes compartilhados | M0 - Fundacao do projeto | #001, #002 |
| Sprint 1 | Entregar a Central de Editais e a Base de Conhecimento | M1 - Consulta publica | #003, #004 |
| Sprint 2 | Permitir cadastro, autenticacao e acompanhamento de contribuicoes | M2 - Contribuicoes | #005 |
| Sprint 3 | Entregar moderacao, denuncias e administracao | M3 - Governanca | #006 |
| Sprint 4 | Consolidar acessibilidade, documentacao e validacao | M4 - Qualidade do MVP | #007 |

## Taxonomia de labels e types

### Types

- `type:feature`: entrega de funcionalidade ou incremento do produto.
- `type:chore`: infraestrutura, documentacao, qualidade ou manutencao transversal.

### Labels complementares

- `area:backend`: API, dominio, servicos, persistencia ou seguranca no backend.
- `area:frontend`: paginas, componentes, estado ou integracao da interface.
- `area:fullstack`: entrega que envolve backend e frontend.
- `area:docs`: documentacao, compatibilidade ou validacao documentada.
- `priority:P1`: entrega prioritaria do MVP.
- `priority:P2`: entrega posterior ao primeiro incremento publico.
- `phase:setup`: preparacao inicial do projeto.
- `phase:foundation`: componentes compartilhados e bloqueadores.
- `phase:public-consultation`: consulta publica.
- `phase:contribution`: autenticacao e contribuicoes.
- `phase:governance`: moderacao e administracao.
- `phase:polish`: qualidade e consolidacao.
- `sprint:0`: setup e fundacao compartilhada.
- `sprint:1`: consulta publica institucional e academica.
- `sprint:2`: cadastro, autenticacao e contribuicoes.
- `sprint:3`: moderacao, denuncias e administracao.
- `sprint:4`: acessibilidade, documentacao e validacao.

---

## Sprint 0 - Setup e fundacao

**Milestone:** `M0 - Fundacao do projeto`

Entrega a estrutura inicial e a fundacao compartilhada que desbloqueia as funcionalidades do MVP.

### #001 - Setup da aplicacao e infraestrutura inicial

- **Sprint:** `Sprint 0`
- **Milestone:** `M0 - Fundacao do projeto`
- **Type:** `chore`
- **Labels:** `area:fullstack`, `area:docs`, `phase:setup`, `sprint:0`
- **Priority:** `P1`
- **Depends on:** nenhuma
- **Tasks:** T001-T005

#### Objetivo

Preparar a estrutura minima do backend e frontend, as dependencias principais, o ponto de entrada da API e as instrucoes iniciais de execucao.

#### Escopo

- Criar a estrutura de diretorios definida no plano.
- Configurar dependencias Python e JavaScript.
- Criar a aplicacao FastAPI e documentar seu ponto de entrada.
- Atualizar o `README.md` com configuracao e execucao local.

#### Criterios de aceite

- [ ] A estrutura de backend, frontend e testes existe conforme o plano.
- [ ] Backend e frontend possuem suas dependencias declaradas.
- [ ] A aplicacao FastAPI possui ponto de entrada executavel.
- [ ] O README explica os comandos basicos de configuracao e execucao.

---

### #002 - Fundacao compartilhada, persistencia e autenticacao

- **Sprint:** `Sprint 0`
- **Milestone:** `M0 - Fundacao do projeto`
- **Type:** `feature`
- **Labels:** `area:fullstack`, `phase:foundation`, `sprint:0`
- **Priority:** `P1`
- **Depends on:** #001
- **Tasks:** T006-T016

#### Objetivo

Implementar os componentes compartilhados que desbloqueiam todas as historias: configuracao, SQLite, modelos, erros, autenticacao, permissoes, roteamento e base da interface.

#### Escopo

- Configurar ambiente, banco SQLite e sessoes SQLModel.
- Normalizar os modelos de usuario, curso, disciplina, submissao, contribuicao, conteudo e fontes.
- Criar modelos de publicacao e denuncia.
- Padronizar erros da API.
- Implementar cadastro, login, hash de senha e sessao/token.
- Criar verificadores de usuario, moderador e administrador.
- Registrar rotas sob `/api/v1`.
- Criar cliente HTTP, estado de autenticacao e componentes base do frontend.

#### Criterios de aceite

- [ ] A API inicia com SQLite e cria as tabelas necessarias.
- [ ] Os modelos compartilhados refletem o `data-model.md`.
- [ ] Erros de validacao, autenticacao, permissao, recurso ausente e fonte indisponivel possuem formato comum.
- [ ] Senhas nao aparecem em respostas, erros ou registros de operacao.
- [ ] Rotas protegidas conseguem identificar o usuario e seu perfil.
- [ ] O frontend consegue armazenar a sessao e exibir erros com foco visivel.

---

## Sprint 1 - Consulta publica

**Milestone:** `M1 - Consulta publica`

Entrega os dois espacos de consulta publica do UNB CORE.

### #003 - Central publica de editais e avisos

- **Sprint:** `Sprint 1`
- **Milestone:** `M1 - Consulta publica`
- **Type:** `feature`
- **Labels:** `area:fullstack`, `priority:P1`, `phase:public-consultation`, `sprint:1`
- **Depends on:** #002
- **Tasks:** T017-T023

#### Objetivo

Permitir que qualquer pessoa consulte publicacoes institucionais cadastradas manualmente, aplique filtros e veja a origem e o estado de verificacao.

#### Escopo

- Criar servico e schemas de publicacoes.
- Implementar listagem, filtros, busca por termo e detalhamento.
- Implementar a separacao entre resultados academicos e institucionais na busca unificada.
- Criar as paginas de listagem e detalhe da Central de Editais e Avisos.
- Integrar a navegacao entre os dois espacos publicos.

#### Criterios de aceite

- [ ] `GET /api/v1/publicacoes` lista publicacoes sem autenticacao.
- [ ] `GET /api/v1/publicacoes/{id}` exibe origem, estado, prazo e data de verificacao.
- [ ] Os filtros por termo, categoria, unidade, curso, estado e prazo funcionam.
- [ ] Publicacoes sem prazo ou sem verificacao sao identificadas claramente.
- [ ] A interface possui estado vazio e link para a fonte oficial.
- [ ] A busca unificada separa resultados academicos e institucionais.

---

### #004 - Base publica de conhecimento academico

- **Sprint:** `Sprint 1`
- **Milestone:** `M1 - Consulta publica`
- **Type:** `feature`
- **Labels:** `area:fullstack`, `priority:P1`, `phase:public-consultation`, `sprint:1`
- **Depends on:** #002
- **Tasks:** T024-T030

#### Objetivo

Permitir que estudantes encontrem conteudos publicados por curso, disciplina e tipo, com informacoes de autoria, origem e atualizacao.

#### Escopo

- Criar servicos e schemas para cursos, disciplinas e conteudos.
- Implementar os endpoints de disciplinas e conteudos.
- Integrar conteudos academicos a busca unificada.
- Criar a pagina de consulta da Base de Conhecimento.
- Criar cards e detalhe de conteudo com autoria, origem e data de atualizacao.

#### Criterios de aceite

- [ ] `GET /api/v1/cursos/{curso_id}/disciplinas` lista disciplinas.
- [ ] `GET /api/v1/disciplinas/{disciplina_id}/conteudos` lista conteudos e aceita filtro por tipo.
- [ ] A consulta funciona sem autenticacao.
- [ ] A interface permite selecionar curso, disciplina e tipo.
- [ ] Conteudos academicos aparecem separados na busca unificada.
- [ ] A tela oferece caminho para contribuir quando aplicavel.

---

## Sprint 2 - Contribuicoes

**Milestone:** `M2 - Contribuicoes`

Entrega o fluxo autenticado de cadastro, envio e acompanhamento de contribuicoes.

### #005 - Cadastro, autenticacao e contribuicoes pendentes

- **Sprint:** `Sprint 2`
- **Milestone:** `M2 - Contribuicoes`
- **Type:** `feature`
- **Labels:** `area:fullstack`, `priority:P2`, `phase:contribution`, `sprint:2`
- **Depends on:** #002 e #004
- **Tasks:** T031-T037

#### Objetivo

Permitir que uma pessoa crie uma conta, entre no sistema, envie uma contribuicao valida e acompanhe seu estado de moderacao.

#### Escopo

- Criar paginas de cadastro e login.
- Criar schemas e endpoints de cadastro e autenticacao.
- Validar campos obrigatorios e diferenciar criacao de alteracao de conteudo.
- Criar endpoints de envio e consulta das contribuicoes do usuario.
- Criar formulario e pagina de acompanhamento no frontend.

#### Criterios de aceite

- [ ] O cadastro exige nome, e-mail unico e senha.
- [ ] O login emite uma sessao/token sem retornar a senha.
- [ ] Usuario anonimo nao consegue enviar nem consultar contribuicoes.
- [ ] Contribuicoes novas iniciam no estado `pendente`.
- [ ] Campos obrigatorios ausentes geram mensagens orientativas.
- [ ] O autor consegue acompanhar o estado e a justificativa de moderacao.

---

## Sprint 3 - Governanca

**Milestone:** `M3 - Governanca`

Entrega as operacoes protegidas de moderacao, denuncias e administracao institucional.

### #006 - Moderacao, denuncias e administracao institucional

- **Sprint:** `Sprint 3`
- **Milestone:** `M3 - Governanca`
- **Type:** `feature`
- **Labels:** `area:fullstack`, `priority:P2`, `phase:governance`, `sprint:3`
- **Depends on:** #003 e #005
- **Tasks:** T038-T045

#### Objetivo

Permitir a moderacao de contribuicoes e denuncias e o gerenciamento administrativo de publicacoes, fontes, categorias e disciplinas.

#### Escopo

- Implementar transicoes de moderacao com justificativa.
- Criar servico e endpoints de denuncias autenticadas.
- Restringir decisoes de moderacao a moderadores e administradores.
- Restringir cadastros e alteracoes institucionais a administradores.
- Criar paginas e componentes de moderacao e administracao.
- Integrar o formulario de denuncia nas publicacoes.

#### Criterios de aceite

- [ ] Contribuicoes transitam de `pendente` para `aprovada`, `ajustes`, `rejeitada` ou `arquivada`.
- [ ] Decisoes preservam justificativa quando informada.
- [ ] A aprovacao cria ou atualiza o conteudo correspondente.
- [ ] Usuarios comuns nao conseguem executar acoes de moderacao ou administracao.
- [ ] Administradores conseguem gerenciar publicacoes, fontes, categorias e disciplinas.
- [ ] Denuncias ficam vinculadas ao usuario e possuem ciclo de estados.

---

## Sprint 4 - Qualidade do MVP

**Milestone:** `M4 - Qualidade do MVP`

Consolida acessibilidade, documentacao, compatibilidade e validacao dos cenarios do MVP.

### #007 - Acessibilidade, documentacao e validacao final

- **Sprint:** `Sprint 4`
- **Milestone:** `M4 - Qualidade do MVP`
- **Type:** `chore`
- **Labels:** `area:fullstack`, `area:docs`, `phase:polish`, `sprint:4`
- **Depends on:** #003, #004, #005 e #006
- **Tasks:** T046-T053

#### Objetivo

Consolidar a qualidade transversal do MVP, atualizar a documentacao e validar os cenarios previstos no quickstart.

#### Escopo

- Aplicar nomes acessiveis, foco visivel e navegacao por teclado.
- Padronizar mensagens de erro com causa e orientacao.
- Atualizar o quickstart, requisitos e README.
- Criar o guia de primeira contribuicao.
- Identificar documentos oficiais nao pesquisaveis sem remover o link oficial.
- Registrar a compatibilidade com navegadores desktop atuais e Chrome/Safari mobile.
- Executar e registrar os cenarios de validacao do MVP.

#### Criterios de aceite

- [ ] Fluxos principais possuem nomes acessiveis, foco visivel e navegacao por teclado.
- [ ] Mensagens de erro informam causa e proximo passo quando aplicavel.
- [ ] O guia de contribuicao cobre qualidade, escopo, autoria e fontes.
- [ ] Publicacoes nao pesquisaveis exibem orientacao para consulta no link oficial.
- [ ] `quickstart.md`, `README.md` e `docs/requisitos.md` refletem o comportamento implementado.
- [ ] A compatibilidade prevista esta registrada em `docs/compatibilidade.md`.
- [ ] Os cenarios do quickstart foram executados e as pendencias foram registradas.

---

## Ordem de execucao

1. #001 - Setup da aplicacao e infraestrutura inicial
2. #002 - Fundacao compartilhada, persistencia e autenticacao
3. #003 - Central publica de editais e avisos
4. #004 - Base publica de conhecimento academico
5. #005 - Cadastro, autenticacao e contribuicoes pendentes
6. #006 - Moderacao, denuncias e administracao institucional
7. #007 - Acessibilidade, documentacao e validacao final

As issues #003 e #004 podem ser desenvolvidas em paralelo depois da conclusao de #002. A issue #005 depende dos modelos academicos e a #006 depende da autenticacao, das contribuicoes e das publicacoes. A #007 fecha o MVP depois dos incrementos funcionais.
