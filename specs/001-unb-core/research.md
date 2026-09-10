# Research: UNB CORE

## Decisão: backend com FastAPI, Python e SQLModel

- **Rationale**: A equipe já iniciou os modelos de domínio em Python com SQLModel, e a documentação técnica do projeto registra FastAPI como escolha do backend. A combinação permite validar dados com Pydantic e expor contratos JSON simples.
- **Alternativas consideradas**: NestJS foi considerado anteriormente, mas exigiria mudar a linguagem escolhida pela equipe. Django seria mais amplo do que o necessário para o MVP.

## Decisão: SQLite no MVP

- **Rationale**: O projeto é acadêmico e precisa de uma execução local simples. SQLite evita configurar um servidor de banco durante o desenvolvimento e atende ao escopo inicial.
- **Alternativas consideradas**: PostgreSQL será mantido como possibilidade de migração futura. Não será necessário no primeiro incremento.

## Decisão: autenticação local simples

- **Rationale**: A consulta permanece pública, mas cadastro de conta e envio de contribuições precisam de identificação. O MVP usará cadastro e login básicos, com senha armazenada de forma protegida e sessão/token de acesso.
- **Alternativas consideradas**: Login institucional da UnB e OAuth foram adiados por dependerem de integração externa e credenciais que não fazem parte do escopo da disciplina.

## Decisão: contribuições moderadas

- **Rationale**: Qualquer usuário autenticado é considerado colaborador e pode enviar uma proposta. A proposta começa como `pendente` e só vira conteúdo publicado após decisão de um moderador.
- **Alternativas consideradas**: Cadastro separado de colaboradores foi descartado na clarificação por adicionar uma etapa de administração sem benefício proporcional para o MVP.

## Decisão: publicações institucionais cadastradas manualmente

- **Rationale**: Administradores consultam as fontes oficiais e registram as publicações no sistema. Essa escolha mantém a origem explícita e evita implementar coletores automáticos, que não são necessários para a apresentação.
- **Alternativas consideradas**: RSS, scraping e integrações automáticas ficam fora do MVP.

## Decisão: API REST versionada

- **Rationale**: A interface React e os testes podem consumir respostas JSON previsíveis. O prefixo `/api/v1` permite organizar os contratos sem criar uma arquitetura complexa.
- **Alternativas consideradas**: GraphQL e comunicação em tempo real não são necessários para os fluxos definidos.

## Decisão: testes focados nos fluxos críticos

- **Rationale**: O projeto deve testar regras de publicação, moderação, permissões e consulta pública. Testes unitários cobrem validações; testes de integração cobrem os principais fluxos da API; a interface terá verificações dos caminhos essenciais.
- **Alternativas consideradas**: Teste de carga, observabilidade avançada e cobertura integral de navegador foram excluídos por não fazerem parte do escopo acadêmico definido.
