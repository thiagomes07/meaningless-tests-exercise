# Projeto de Testes Automatizados - Inativamento de Atendimento com Geração de Log

Este repositório contém o código e os testes automatizados para verificar o comportamento de uma API que realiza o inativamento de atendimentos e gera logs de uso. A API foi mockada para garantir que o ambiente de testes seja isolado e não afete o sistema real.

## Descrição do Projeto

O objetivo principal deste projeto é testar o funcionamento de um endpoint de inativamento de atendimentos e verificar se, ao inativar um atendimento, um log de uso é gerado corretamente. A implementação simula a lógica de atendimento e logs, utilizando mocks para garantir que o sistema esteja isolado durante os testes.

### Funcionalidade Principal

- A API possui um endpoint que permite **inativar um atendimento ativo**, alterando seu status para "Finalizado".
- Quando um atendimento é inativado, **um log é gerado** contendo informações sobre a ação realizada, o usuário que a executou e o atendimento afetado.

## Contextualização do Inativamento de Atendimentos, Assistências e Logs

Dentro do contexto da Assessoria de Inclusão, **atendimentos** são registros que vinculam um aluno a um profissional da área de inclusão, seja para **acompanhamento** psicológico, social ou o fornecimento de **tecnologias assistivas** (como leitores de tela, cadeiras de rodas, etc.). Cada atendimento tem um **status** que pode ser `Ativo`, `Finalizado`, `Cancelado` ou `Pausado`.

O **inativamento** de um atendimento ocorre quando este deixa de ser necessário, seja porque o aluno não precisa mais do acompanhamento ou tecnologia assistiva, ou porque a situação foi resolvida. O objetivo do endpoint de **inativamento de atendimentos** é alterar o status de um atendimento de "Ativo" para "Finalizado". Durante esse processo, um **log** de uso é gerado para rastrear a ação realizada, permitindo que se tenha um histórico das operações no sistema, como quem fez a alteração e qual atendimento foi afetado.

### **Fluxo de Inativamento:**
1. Um **atendimento** ativo é registrado no sistema.
2. Quando o atendimento não é mais necessário, ele é **inativado**, alterando seu status para "Finalizado".
3. Ao inativar o atendimento, um **log de uso** é criado, registrando quem realizou a ação, o atendimento que foi alterado, e outros detalhes relevantes.

Esses logs são vitais para **auditoria** e **controle**, garantindo que todas as modificações no sistema possam ser rastreadas e verificadas.

## Estrutura do Repositório

```
C:.
│   README.md
│
├───server
│   │   .gitignore
│   │   app.js
│   │   package-lock.json
│   │   package.json
│   │
│   └───mock
│           appointments.js
│
└───tests
        appointment_inactivation_test.py
        test_case.md
```

- **server/**: Contém o servidor e as rotas mockadas da API.
  - **app.js**: Arquivo de configuração da API mockada.
  - **mock/appointments.js**: Mock da lógica de inativamento de atendimentos.
  
- **tests/**: Contém os testes automatizados para a funcionalidade de inativamento de atendimentos.
  - **appointment_inactivation_test.py**: Arquivo Python que realiza os testes automatizados usando a biblioteca `requests` para simular requisições HTTP e `unittest.mock` para mockar a resposta de logs.
  - **test_case.md**: Documento que descreve o caso de teste, incluindo objetivo, pré-condições, procedimento, resultado esperado e pós-condições.

## Requisitos

Antes de rodar os testes, certifique-se de ter os seguintes requisitos instalados:

- **Python 3.x**: Para rodar os testes automatizados.
- **Bibliotecas Python**: As bibliotecas necessárias podem ser instaladas com o seguinte comando:
  ```bash
  pip install requests
  ```

- **Node.js e NPM**: Para rodar o servidor de mock da API.
- **Bibliotecas Node.js**: Instalar as dependências necessárias do servidor com:
  ```bash
  npm install
  ```

## Como Rodar o Projeto

### 1. Subir o Servidor Mockado

Antes de executar os testes, é necessário garantir que o servidor de mock da API esteja rodando localmente. Para isso, execute o seguinte comando dentro da pasta `server`:

```bash
node app.js
```

Isso irá iniciar o servidor mockado na porta 3000.

### 2. Rodar os Testes

Com o servidor de mock em funcionamento, você pode rodar os testes automatizados usando o Python. Na pasta `tests`, execute:

```bash
python appointment_inactivation_test.py
```

Os testes verificarão se o endpoint de inativamento de atendimento funciona corretamente e se um log é gerado conforme esperado.

## Detalhes do Caso de Teste

O caso de teste automatizado verifica os seguintes pontos:
1. **Inativamento de Atendimento**: Verifica se a requisição `PATCH` para o endpoint `http://localhost:3000/mock/atendimentos/{id}` inativa corretamente um atendimento ativo.
2. **Geração de Log**: Verifica se, ao inativar o atendimento, um log é gerado corretamente com os detalhes da ação realizada, incluindo o ID do usuário e do atendimento.

### Caso de Teste: Inativamento de Atendimento com Geração de Log

- **Objetivo**: Verificar se o atendimento é inativado corretamente e se um log é gerado com a ação.
- **Pré-condições**:
  - O servidor de mock da API deve estar rodando.
  - O atendimento a ser inativado deve estar ativo.
  - O usuário que realiza a ação deve ter permissões adequadas.
- **Procedimento**:
  - Verificar se o atendimento está ativo.
  - Enviar uma requisição `PATCH` para inativar o atendimento.
  - Verificar se a resposta da API foi `200 OK` e se o status foi alterado para "Finalizado".
  - Verificar se o log foi registrado corretamente.
  
- **Resultado Esperado**:
  - A resposta da API deve indicar que o atendimento foi inativado.
  - O log de inativação deve ser gerado com as informações corretas.