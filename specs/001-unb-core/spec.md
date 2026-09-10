# Feature Specification: UNB CORE

**Feature Branch**: `001-unb-core`

**Created**: 2026-09-09

**Status**: Draft

**Input**: User description: "Criar uma plataforma acadêmica e institucional para estudantes da UnB, reunindo uma base de conhecimento colaborativa e uma central de editais e avisos oficiais."

## Clarifications

### Session 2026-09-09

- Q: Quem deve poder enviar contribuições acadêmicas para revisão? → A: Somente usuários previamente cadastrados como colaboradores.
- Q: Como um usuário deve se tornar um colaborador cadastrado? → A: Qualquer usuário autenticado é automaticamente colaborador.
- Q: Quem deve poder cadastrar e alterar editais, avisos e comunicados institucionais? → A: Somente administradores podem cadastrar e alterar publicações.
- Q: Como um estudante deve criar uma conta para acessar as funções autenticadas? → A: O estudante cria a própria conta.
- Q: Como as publicações institucionais devem ser inseridas no sistema no MVP? → A: Administradores cadastram manualmente as publicações a partir das fontes oficiais.

## User Scenarios & Testing

### User Story 1 - Consultar editais e avisos oficiais (Priority: P1)

Como estudante da UnB, quero encontrar editais, avisos e comunicados oficiais organizados em um só lugar, para consultar oportunidades e acessar a fonte oficial da informação.

**Why this priority**: É uma das finalidades centrais do produto e atende diretamente à necessidade de reduzir a dispersão dos comunicados institucionais.

**Independent Test**: Pode ser testada cadastrando publicações de exemplo, filtrando por categoria ou unidade e verificando se os detalhes e a fonte oficial são exibidos.

**Acceptance Scenarios**:

1. **Given** que existem publicações cadastradas, **When** o estudante acessa a Central de Editais e Avisos, **Then** ele visualiza uma lista organizada de publicações.
2. **Given** que uma publicação possui fonte oficial, **When** o estudante abre seus detalhes, **Then** ele visualiza o resumo, a unidade responsável, as datas, o estado e o link oficial.
3. **Given** que uma fonte oficial está indisponível ou não foi verificada, **When** o estudante consulta a publicação, **Then** essa limitação é informada claramente.

---

### User Story 2 - Consultar conteúdos de uma disciplina (Priority: P1)

Como estudante, quero consultar resumos, dicas, dificuldades, provas, implementações e links organizados por curso e disciplina, para apoiar meus estudos.

**Why this priority**: A Base de Conhecimento é o segundo pilar principal do produto e concentra o conhecimento colaborativo do grupo.

**Independent Test**: Pode ser testada selecionando um curso, uma disciplina e uma categoria, e verificando se os conteúdos publicados aparecem com autoria ou origem e data de atualização.

**Acceptance Scenarios**:

1. **Given** que existem conteúdos publicados, **When** o estudante seleciona um curso e uma disciplina, **Then** ele visualiza os conteúdos disponíveis para aquela disciplina.
2. **Given** que existem diferentes tipos de conteúdo, **When** o estudante escolhe uma categoria, **Then** a lista é filtrada pelo tipo selecionado.
3. **Given** que um conteúdo foi publicado, **When** o estudante abre seus detalhes, **Then** ele visualiza a disciplina, o tipo, a autoria ou origem e a data de atualização.
4. **Given** que não existem conteúdos para o filtro selecionado, **When** o estudante realiza a consulta, **Then** o sistema informa que não há resultados e apresenta a possibilidade de contribuir.

---

### User Story 3 - Enviar e acompanhar uma contribuição (Priority: P2)

Como usuário autenticado, quero enviar uma contribuição associada a um curso, disciplina e categoria, para compartilhar conhecimento com outros estudantes sem publicação imediata.

**Why this priority**: A colaboração amplia o valor da plataforma, mas depende da existência de uma base consultável e de um processo de revisão.

**Independent Test**: Pode ser testada preenchendo uma contribuição válida, enviando-a e verificando que ela fica pendente e pode ser acompanhada pelo autor.

**Acceptance Scenarios**:

1. **Given** que o usuário está autenticado e possui as informações obrigatórias, **When** ele envia uma contribuição, **Then** a contribuição é registrada como pendente.
2. **Given** que a contribuição está pendente, **When** o colaborador consulta seu envio, **Then** ele visualiza o estado atual da contribuição.
3. **Given** que a contribuição precisa de ajustes, **When** um moderador devolve o envio com uma justificativa, **Then** o colaborador visualiza a orientação para correção.
4. **Given** que faltam informações obrigatórias, **When** o colaborador tenta enviar o formulário, **Then** o sistema informa os campos que precisam ser preenchidos.
5. **Given** que o usuário não está autenticado, **When** ele tenta enviar uma contribuição, **Then** o sistema impede o envio e informa que é necessário entrar em uma conta.
6. **Given** que o estudante ainda não possui uma conta, **When** ele realiza o cadastro, **Then** sua conta é criada e ele pode acessar as funções permitidas a usuários autenticados.

---

### User Story 4 - Moderar conteúdos e administrar informações (Priority: P2)

Como moderador ou administrador, quero revisar contribuições, gerenciar publicações e tratar relatos de problemas, para preservar a qualidade e a confiabilidade das informações.

**Why this priority**: A moderação é necessária para que os conteúdos compartilhados não sejam publicados sem revisão e para manter a transparência das publicações institucionais.

**Independent Test**: Pode ser testada com perfis autorizados e não autorizados, verificando decisões de moderação, justificativas e bloqueio de operações indevidas.

**Acceptance Scenarios**:

1. **Given** que existe uma contribuição pendente, **When** um moderador aprova, rejeita, arquiva ou solicita ajustes, **Then** o estado da contribuição é atualizado conforme a decisão.
2. **Given** que uma decisão exige explicação, **When** o moderador registra a decisão, **Then** a justificativa fica vinculada à contribuição.
3. **Given** que um usuário comum tenta acessar uma operação de moderação, **When** ele realiza a tentativa, **Then** o acesso é negado.
4. **Given** que existe um relato de duplicidade, link quebrado ou desatualização, **When** um administrador consulta os relatos, **Then** ele consegue encaminhar o problema para análise.
5. **Given** que um usuário não é administrador, **When** ele tenta cadastrar ou alterar uma publicação institucional, **Then** o acesso é negado.
6. **Given** que um administrador consulta uma fonte oficial, **When** ele cadastra uma publicação, **Then** a publicação é registrada com a origem e os dados disponíveis da fonte.
7. **Given** que um moderador consulta uma contribuição ou denúncia, **When** ele realiza uma decisão permitida, **Then** somente o registro correspondente é alterado.

### Edge Cases

- Uma fonte oficial pode ficar temporariamente indisponível.
- Uma publicação pode aparecer em mais de uma fonte.
- Um edital pode não informar prazo.
- Um documento oficial pode não permitir pesquisa direta em seu conteúdo.
- Uma contribuição pode não possuir fonte, conter material ofensivo ou utilizar material potencialmente protegido.
- Uma busca pode não retornar resultados.
- Um usuário pode tentar acessar uma função sem a permissão necessária.

## Requirements

### Functional Requirements

- **FR-001**: O sistema MUST apresentar acesso separado para a Base de Conhecimento e para a Central de Editais e Avisos.
- **FR-002**: O sistema MUST permitir navegar por curso, disciplina e tipo de conteúdo.
- **FR-003**: O sistema MUST permitir consultar publicações institucionais por categoria, unidade, curso relacionado e datas relevantes.
- **FR-004**: O sistema MUST permitir pesquisar na Base de Conhecimento e na Central de Editais e Avisos, diferenciando os resultados.
- **FR-005**: O sistema MUST exibir a origem, a unidade responsável, o estado e a data de verificação das publicações quando essas informações estiverem disponíveis.
- **FR-006**: O sistema MUST exigir autenticação para registrar relatos de erro, duplicidade, link quebrado ou desatualização, vinculando cada denúncia ao usuário que a criou.
- **FR-007**: O sistema MUST permitir que somente usuários autenticados, considerados colaboradores, enviem contribuições associadas a curso, disciplina e tipo de conteúdo.
- **FR-008**: O sistema MUST manter novas contribuições pendentes até a revisão de um moderador autorizado.
- **FR-009**: O sistema MUST permitir que moderadores aprovem, rejeitem, arquivem ou devolvam contribuições para ajustes.
- **FR-010**: O sistema MUST preservar a justificativa das decisões de moderação quando ela for registrada.
- **FR-011**: O sistema MUST disponibilizar orientações sobre qualidade, escopo permitido, autoria e fontes para a primeira contribuição.
- **FR-012**: A consulta básica de conteúdos e publicações MUST estar disponível sem autenticação.
- **FR-013**: O sistema MUST impedir que usuários sem autorização publiquem ou alterem diretamente conteúdos moderados.
- **FR-014**: O sistema MUST apresentar mensagens compreensíveis para estados vazios, falhas de fonte, erros de acesso e envios incompletos.
- **FR-015**: O sistema MUST preservar o vínculo de cada informação com sua fonte oficial ou com o colaborador responsável.
- **FR-016**: O sistema MUST permitir que somente administradores cadastrem ou alterem publicações institucionais.
- **FR-017**: O sistema MUST permitir que estudantes criem a própria conta para acessar as funções autenticadas.
- **FR-018**: O sistema MUST permitir que administradores cadastrem manualmente publicações consultadas em fontes oficiais no MVP.
- **FR-019**: O sistema MUST exigir título, resumo, categoria, unidade responsável e fonte oficial para cadastrar uma publicação institucional.
- **FR-020**: O sistema MUST exigir curso, disciplina, tipo e conteúdo ou URL para enviar uma contribuição; `conteudo_id` será informado somente quando a contribuição alterar conteúdo existente.
- **FR-021**: O sistema MUST interpretar o filtro `termo` como busca em título e resumo; `categoria`, `unidade`, `curso_id`, `estado` e `prazo` devem filtrar pelos campos correspondentes.
- **FR-022**: O sistema MUST representar publicações sem prazo como `sem_prazo` e informar essa condição ao usuário.
- **FR-023**: O sistema MUST informar quando um documento oficial não puder ser pesquisado diretamente, mantendo o link para consulta externa.
- **FR-024**: O sistema MUST permitir que moderadores analisem contribuições e denúncias, enquanto administradores podem executar essas ações e também gerenciar publicações institucionais, fontes, categorias e disciplinas.
- **FR-025**: O sistema MUST rejeitar o cadastro de publicação ou contribuição incompleto antes de criar um registro parcial, informando os campos ausentes.
- **FR-026**: O sistema MUST oferecer nomes acessíveis, foco visível e navegação por teclado nos fluxos principais de consulta, busca, contribuição e moderação.
- **FR-027**: O MVP deve considerar os principais navegadores desktop atuais e as versões móveis atuais de Chrome e Safari, sem exigir suporte a versões antigas específicas.
- **FR-028**: O sistema MUST exigir nome, e-mail e senha para criar uma conta, e-mail único para cada conta.
- **FR-029**: O sistema MUST exigir tipo e descrição para registrar uma denúncia.
- **FR-030**: O sistema MUST impedir que senhas apareçam em respostas da API, mensagens de erro ou registros de operação.
- **FR-031**: O sistema MUST apresentar nas mensagens de erro a causa do problema e, quando aplicável, a orientação para corrigi-lo ou tentar novamente.

### Key Entities

- **Usuário**: pessoa que consulta informações ou, quando autenticada, pode salvar preferências e enviar contribuições; funções de moderação e administração dependem de autorização específica.
- **Curso**: agrupamento de disciplinas e referência para organização dos interesses acadêmicos.
- **Disciplina**: unidade curricular pertencente a um curso.
- **Conteúdo acadêmico**: material publicado na Base de Conhecimento, como resumo, dica, dificuldade, prova, implementação ou link.
- **Contribuição**: proposta de criação ou alteração de conteúdo acadêmico que passa por estados de revisão.
- **Fonte institucional**: canal oficial relacionado a publicações da UnB.
- **Publicação institucional**: edital, aviso ou comunicado com origem, unidade, categoria, datas, estado e link oficial. Fontes iniciais incluem Reitoria, decanatos, institutos, faculdades, coordenações e canais oficiais relacionados ao SEI.
- **Denúncia**: relato de problema em uma publicação ou conteúdo, encaminhado para análise.

## Success Criteria

### Measurable Outcomes

- **SC-001**: Em uma demonstração, um estudante consegue encontrar uma publicação institucional usando busca ou filtros e acessar sua fonte oficial.
- **SC-002**: Em uma demonstração, um estudante consegue localizar conteúdos de uma disciplina selecionando curso, disciplina e categoria.
- **SC-003**: 100% das contribuições enviadas durante os testes permanecem pendentes até uma decisão de moderação.
- **SC-004**: 100% das decisões de moderação realizadas durante os testes resultam no estado correspondente e preservam a justificativa quando informada.
- **SC-005**: Usuários sem permissão não conseguem executar operações de moderação ou administração durante os testes.
- **SC-006**: Publicações sem verificação são identificadas claramente nos testes de consulta.
- **SC-007**: Os fluxos principais de consulta, busca e envio de contribuição podem ser realizados por teclado.

## Assumptions

- O foco inicial da Base de Conhecimento será Engenharia de Software.
- A consulta pública não exige autenticação.
- A publicação de contribuições depende de revisão humana.
- A Central de Editais e Avisos manterá um link para a fonte oficial sempre que ele estiver disponível.
- Denúncias exigem autenticação no MVP; cadastro de conta, verificação de e-mail e recuperação de senha ficam fora do escopo inicial.
- O sistema será desenvolvido como projeto acadêmico de escopo reduzido, sem metas de desempenho, capacidade ou infraestrutura avançada.
- Autenticação, fontes institucionais prioritárias e hospedagem serão detalhadas durante o planejamento técnico, sem alterar os fluxos principais desta especificação.
- Qualquer usuário autenticado será considerado colaborador e poderá enviar contribuições para revisão.
- Somente administradores poderão cadastrar ou alterar publicações institucionais.
- Estudantes poderão criar a própria conta sem aprovação prévia de um administrador.
- No MVP, as publicações institucionais serão cadastradas manualmente por administradores a partir das fontes oficiais.
