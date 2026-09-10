# Documento de Requisitos do Produto

## UNB CORE

**Projeto:** Métodos de Desenvolvimento de Software 2026/2  
**Curso:** Engenharia de Software - 2026.2  
**Equipe:** G1

## 1. Visão geral

O UNB CORE é uma plataforma de informações acadêmicas e institucionais da Universidade de Brasília (UnB). O sistema reúne dois espaços principais:

1. **Base de Conhecimento:** materiais, resumos, dicas e experiências organizadas por curso e disciplina.
2. **Central de Editais e Avisos:** publicações oficiais da UnB reunidas e organizadas em um único local.

O objetivo é reduzir a dispersão do conhecimento acadêmico e facilitar o acesso a comunicados e oportunidades institucionais. O foco inicial da Base de Conhecimento será o curso de Engenharia de Software, com possibilidade de expansão para outros cursos.

A plataforma será um agregador de informações e não substituirá os canais oficiais da UnB. Em caso de divergência, a fonte oficial deverá prevalecer.

## 2. Público-alvo

- Estudantes de graduação e pós-graduação da UnB.
- Veteranos interessados em compartilhar conhecimento.
- Coordenações de curso, centros acadêmicos e entidades estudantis como usuários indiretos.

## 3. Escopo do produto

### 3.1 Incluído no escopo

- Consulta pública de conteúdos acadêmicos.
- Consulta pública de editais, avisos e comunicados.
- Organização por curso, disciplina, categoria e unidade responsável.
- Busca e filtros para localizar informações.
- Envio de contribuições acadêmicas.
- Revisão e moderação das contribuições antes da publicação.
- Registro da fonte e da data de verificação de publicações institucionais.
- Relato de problemas em publicações, como duplicidade, link quebrado ou desatualização.
- Cadastro opcional para salvar preferências de cursos e categorias.

### 3.2 Fora do escopo inicial

- Substituir os sistemas oficiais da UnB.
- Receber inscrições, documentos ou recursos de processos institucionais.
- Garantir cobertura de todos os canais da Universidade.
- Oferecer tutoria individual, chat ou correção automática de exercícios.
- Publicar contribuições sem revisão quando houver risco de erro, dados pessoais ou ausência de fonte.
- Criar uma rede social geral entre estudantes.

## 4. Requisitos funcionais

### RF-001 - Navegação principal

O sistema deve apresentar acesso separado para a Base de Conhecimento e para a Central de Editais e Avisos.

### RF-002 - Organização acadêmica

O sistema deve permitir navegar por curso, disciplina e tipo de conteúdo.

### RF-003 - Consulta de conteúdo

O sistema deve exibir, para cada conteúdo acadêmico publicado, a disciplina, o tipo, a autoria ou origem e a data de atualização.

### RF-004 - Busca unificada

O sistema deve permitir pesquisar na Base de Conhecimento e na Central de Editais e Avisos, diferenciando claramente os resultados de cada espaço.

### RF-005 - Cadastro de publicações oficiais

O sistema deve registrar editais, avisos e comunicados com título, resumo, fonte original, unidade responsável e endereço oficial de acesso.

### RF-006 - Categorização institucional

O sistema deve permitir classificar publicações por categoria, unidade responsável, curso relacionado e datas relevantes.

### RF-007 - Data de verificação

O sistema deve exibir a data da última verificação ou atualização conhecida de cada publicação institucional.

### RF-008 - Estados da publicação

O sistema deve diferenciar publicações ativas, encerradas, canceladas, desatualizadas, não verificadas e sem prazo informado.

Publicações encerradas, canceladas ou desatualizadas não devem ser apresentadas como oportunidades ativas.

### RF-009 - Relato de problemas

O sistema deve permitir relatar erro, duplicidade, link quebrado ou desatualização em uma publicação.

### RF-010 - Contribuições acadêmicas

O sistema deve permitir enviar contribuições associadas a um curso, disciplina e tipo de conteúdo.

### RF-011 - Revisão de contribuições

Novas contribuições ou alterações devem permanecer pendentes até a revisão de um moderador autorizado.

### RF-012 - Moderação

Moderadores devem poder aprovar, rejeitar, arquivar ou devolver contribuições para ajustes. Quando necessário, a decisão deve conter uma justificativa.

### RF-013 - Guia de contribuição

O sistema deve disponibilizar orientações sobre qualidade, escopo permitido, autoria e referência das fontes.

### RF-014 - Conta e preferências

O sistema deve permitir autenticação opcional para salvar curso, unidade, categorias e preferências do usuário.

### RF-015 - Acesso público

A consulta básica de conteúdos e publicações deve estar disponível sem autenticação.

### RF-016 - Administração

Administradores devem possuir recursos para gerenciar fontes, publicações, categorias, disciplinas, contribuições, denúncias e estados de atualização.

### RF-017 - Rastreabilidade

O sistema deve preservar a origem de cada informação e o vínculo com a fonte oficial ou com o colaborador responsável.

### RF-018 - Tratamento de falhas

Falhas de coleta ou verificação devem ser identificadas explicitamente, sem remover silenciosamente informações relevantes.

### RF-019 - Permissões

O sistema deve impedir que usuários sem autorização publiquem ou alterem diretamente conteúdos moderados.

### RF-020 - Mensagens de estado

O sistema deve apresentar mensagens compreensíveis para estados vazios, erros de acesso, falhas de fonte e envios incompletos.

## 5. Requisitos não funcionais

### RNF-001 - Segurança de acesso

O sistema deve diferenciar, no mínimo, os perfis de usuário, colaborador, moderador e administrador. Operações não autorizadas devem ser negadas.

### RNF-002 - Privacidade

O sistema deve coletar somente os dados necessários para conta, preferências, autoria e moderação. O usuário deve poder consultar e corrigir seus dados quando aplicável.

### RNF-003 - Acessibilidade

As funcionalidades principais de consulta, busca, contribuição e leitura de publicações devem ser utilizáveis por teclado e apresentar nomes compreensíveis para leitores de tela.

### RNF-004 - Compatibilidade

As páginas públicas devem funcionar nos principais navegadores desktop e mobile, com layout adaptado para telas pequenas.

### RNF-005 - Confiabilidade da informação

Toda publicação institucional deve manter a origem, o estado de verificação, a data da última verificação e o link para a fonte oficial quando disponível.

### RNF-006 - Manutenibilidade

O código deve ser organizado por responsabilidades e possuir testes automatizados para as regras mais importantes do sistema.

### RNF-007 - Documentação

O repositório deve conter instruções básicas de configuração, execução e contribuição do projeto.

## 6. Cenários de uso prioritários

### Cenário 1: Encontrar um edital

1. O estudante acessa a Central de Editais e Avisos.
2. Filtra por categoria, unidade, curso ou prazo.
3. Abre uma publicação relevante.
4. Consulta o resumo, o prazo, o estado de atualização e a fonte oficial.
5. Acessa o canal oficial para obter a informação definitiva.

### Cenário 2: Consultar uma disciplina

1. O estudante acessa a Base de Conhecimento.
2. Seleciona o curso e a disciplina.
3. Escolhe uma categoria de conteúdo.
4. Consulta materiais, dicas ou dificuldades comuns.
5. Encontra a opção de contribuir caso o conteúdo ainda não exista.

### Cenário 3: Enviar uma contribuição

1. O colaborador acessa o guia de primeira contribuição.
2. Preenche o formulário com disciplina, categoria, conteúdo e fonte.
3. Envia a contribuição.
4. A contribuição fica pendente de revisão.
5. O colaborador acompanha a aprovação ou recebe orientações para ajustes.

## 7. Casos de exceção

- Fonte oficial temporariamente indisponível.
- Publicação duplicada em fontes diferentes.
- Edital sem prazo informado.
- Documento oficial em formato não pesquisável.
- Contribuição com material sem fonte, ofensivo ou potencialmente protegido.
- Formulário enviado sem informações obrigatórias.
- Busca sem resultados.
- Usuário tentando acessar uma função sem permissão.

## 8. Entidades principais

### Usuário

Pessoa autenticada que pode salvar preferências, enviar contribuições ou moderar conteúdo. Possui nome, e-mail, perfil e estado.

### Curso

Agrupa disciplinas e permite organizar os interesses dos usuários.

### Disciplina

Unidade curricular que pertence a um curso e organiza os conteúdos acadêmicos.

### Conteúdo acadêmico

Material publicado na Base de Conhecimento, como resumo, dica, dificuldade, prova, implementação ou link.

### Contribuição

Proposta de criação ou alteração de conteúdo acadêmico, mantida pendente até a decisão da moderação.

### Fonte institucional

Canal oficial monitorado pela equipe responsável pelo cadastro das publicações.

### Publicação institucional

Edital, aviso ou comunicado que possui fonte, unidade responsável, categoria, datas, estado e link oficial.

### Denúncia

Relato de problema em uma publicação ou conteúdo, encaminhado para análise.

## 9. Arquitetura e tecnologias definidas

A solução será desenvolvida como uma aplicação web simples, adequada ao escopo do projeto da disciplina.

- **Front-end:** HTML, CSS e JavaScript, utilizando React para os componentes e páginas da interface.
- **Back-end:** Python utilizando FastAPI para disponibilizar as funcionalidades do sistema.
- **Banco de dados inicial:** SQLite, por ser adequado ao desenvolvimento local e à fase inicial do projeto.
- **Banco de dados posterior:** PostgreSQL, caso o projeto avance para uma etapa que exija essa migração.
- **Organização:** separação entre interface, regras do sistema, persistência de dados e testes.

As decisões sobre autenticação, fontes institucionais prioritárias, hospedagem e armazenamento de arquivos ainda serão definidas pela equipe conforme a necessidade do projeto.

## 10. Critérios de validação

- Usuários conseguem consultar a Base de Conhecimento e a Central de Editais sem autenticação.
- A busca diferencia resultados acadêmicos e institucionais.
- Publicações exibem fonte oficial, unidade responsável e data de verificação quando essas informações estiverem disponíveis.
- Contribuições novas permanecem pendentes até uma decisão de moderação.
- Cada decisão de moderação altera o estado esperado da contribuição.
- Usuários comuns não acessam operações de moderação ou administração.
- Publicações encerradas, canceladas ou desatualizadas são identificadas corretamente.
- Relatos de problemas são registrados para análise.
- O sistema apresenta mensagens compreensíveis quando não há resultados ou quando ocorre uma falha.
- A navegação principal pode ser realizada por teclado.

## 11. Observação final

O UNB CORE deve priorizar clareza, precisão e transparência. Quando uma informação não puder ser confirmada, o sistema deve mostrar essa limitação claramente em vez de presumir que o conteúdo continua vigente.