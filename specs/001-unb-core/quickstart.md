# Quickstart de Validação: UNB CORE

## Pré-requisitos

- Python 3.12 ou superior.
- Node.js e npm em versão compatível com React.
- Repositório clonado localmente.

## Preparar o backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install fastapi uvicorn sqlmodel pydantic[email] pytest httpx
```

Quando a aplicação estiver criada, iniciar o servidor com:

```powershell
uvicorn app.main:app --reload
```

A API deverá ficar disponível em `http://127.0.0.1:8000` e sua documentação interativa em `/docs`.

## Preparar o frontend

```powershell
cd frontend
npm install
npm run dev
```

A URL exibida pelo comando deverá abrir a interface pública.

## Cenários de validação

### 1. Consulta pública institucional

1. Cadastrar uma publicação de demonstração como administrador.
2. Abrir a Central de Editais e Avisos sem login.
3. Filtrar por categoria ou unidade.
4. Abrir os detalhes.
5. Confirmar título, resumo, fonte oficial, estado e data de verificação.

Resultado esperado: a publicação aparece com a origem oficial e informa quando não foi verificada.

### 2. Consulta acadêmica

1. Criar um curso, uma disciplina e um conteúdo publicado.
2. Abrir a Base de Conhecimento sem login.
3. Selecionar curso, disciplina e tipo.
4. Confirmar os dados de autoria ou origem e atualização.

Resultado esperado: somente conteúdos publicados e compatíveis com os filtros aparecem.

### 3. Contribuição autenticada

1. Criar uma conta de estudante.
2. Enviar uma contribuição válida.
3. Consultar as contribuições da conta.
4. Confirmar o estado `pendente`.
5. Tentar enviar sem preencher um campo obrigatório.
6. Tentar enviar sem autenticação.

Resultado esperado: a contribuição válida fica pendente; dados incompletos produzem mensagem compreensível; usuário não autenticado não consegue enviar.

### 4. Moderação e permissões

1. Criar uma contribuição pendente.
2. Acessar a moderação com um moderador.
3. Solicitar ajustes ou aprovar a contribuição.
4. Confirmar o novo estado e a justificativa.
5. Repetir a tentativa com usuário comum.
6. Tentar cadastrar uma publicação com usuário não administrador.

Resultado esperado: decisões autorizadas alteram o estado; operações não autorizadas são negadas.

## Testes automatizados

Executar a partir do diretório do backend:

```powershell
pytest
```

Os testes devem cobrir validações de estados, permissões, consulta pública, envio de contribuição, moderação e tratamento de erros.
