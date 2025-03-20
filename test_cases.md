# Caso de Teste: Inativamento de Atendimento com Geração de Log

## Objetivo
Verificar se o atendimento pode ser inativado corretamente e se um log de uso é gerado para essa ação.

## Pré-condição
- A API deve estar rodando localmente.
- Deve existir um atendimento ativo no banco de dados para ser inativado.
- O usuário que realiza a ação precisa ter permissões adequadas (por exemplo, um Gerente Administrativo).
- A tabela de logs deve estar configurada corretamente no banco de dados.

## Procedimento de Teste
1. Verificar se existe pelo menos um atendimento ativo no banco de dados.
2. Enviar uma requisição `PATCH` para o endpoint `http://localhost:3000/atendimentos/{id}` para inativar o atendimento, mudando o campo `status` para `Finalizado` (ou outro status de inativação apropriado).
3. Verificar se a resposta da API retorna o status `200 OK` e se o atendimento foi atualizado corretamente (status alterado para `Finalizado`).
4. Consultar a tabela de logs `log_usage` e verificar se há um novo log com a ação de "Inativação de Atendimento", associada ao usuário responsável, incluindo o `appointment_id` correto e outros detalhes da ação.

## Resultado Esperado
1. A API deve retornar um status `200 OK` e a resposta deve conter o atendimento com o status alterado para `Finalizado`.
2. Um novo log deve ser registrado na tabela `log_usage` com:
    - Ação: "Inativação de Atendimento"
    - O ID do usuário que realizou a ação
    - O `appointment_id` correto
    - Detalhes sobre a inativação (por exemplo, a data e a razão)
  
## Resultado Obtido
(Preencher após o teste)

## Pós-condição
- O atendimento estará inativado.
- O log será registrado na tabela `log_usage`.
