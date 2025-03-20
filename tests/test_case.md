# Caso de Teste: Inativamento de Atendimento com Geração de Log

## Objetivo
Verificar se o atendimento pode ser inativado corretamente e se um log de uso é gerado para essa ação.

## Pré-condição
- A API mockada deve estar rodando localmente.
- Um atendimento ativo deve estar presente no sistema mockado para ser inativado.
- O usuário que realiza a ação (mockado como um administrador) deve ter permissões adequadas.
- Não será necessário um banco de dados real. O banco de dados de logs é simulado durante o teste.

## Procedimento de Teste
1. **Verificar se existe um atendimento ativo no sistema mockado**: O sistema deve ter um atendimento com o status "Ativo" para ser inativado.
2. **Enviar uma requisição `PATCH` para o endpoint `http://localhost:3000/mock/atendimentos/{id}`**: A requisição deve tentar inativar o atendimento, alterando o campo `status` para "Finalizado".
3. **Verificar se a resposta da API retorna o status `200 OK` e se o atendimento foi atualizado corretamente**: A resposta da API deve conter o atendimento com o status alterado para `Finalizado`.
4. **Simular a consulta à tabela de logs**: Consultar a criação de um log simulado para verificar se a ação de inativação foi registrada corretamente, incluindo o `appointment_id` correto e os detalhes da ação.

## Resultado Esperado
1. A API deve retornar um status `200 OK` e a resposta deve conter o atendimento com o status alterado para "Finalizado".
2. Um novo log deve ser registrado no sistema simulado com:
   - Ação: "Inativação de Atendimento"
   - O ID do usuário que realizou a ação (usuário mockado)
   - O `appointment_id` correto
   - Detalhes sobre a inativação (por exemplo, a data e a razão).

## Resultado Obtido
- **Resultado da API**: O teste executado retornou o status `200 OK`, indicando que a requisição foi processada com sucesso e o atendimento foi inativado com sucesso. O status do atendimento foi alterado de "Ativo" para "Finalizado" conforme esperado.
  
- **Resultado do Log**: O log gerado durante o teste foi simulado corretamente e contém as seguintes informações:
  - Ação: "Inativação de Atendimento"
  - ID do usuário: 1 (usuário mockado, administrador)
  - Detalhes: "Atendimento 1 inativado."
  - Appointment ID: 1 (atendimento correto)

Além disso, o teste foi executado com sucesso sem erros, e as validações realizadas dentro do código também passaram sem falhas. O log foi criado conforme esperado e a funcionalidade de inativação foi validada com sucesso.

## Pós-condição
- O atendimento estará inativado.
- O log será registrado corretamente na simulação de logs.