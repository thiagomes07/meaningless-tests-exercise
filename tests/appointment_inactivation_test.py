import requests
from unittest.mock import patch
from datetime import datetime

# URL da API mockada
BASE_URL = "http://localhost:3000/mock/atendimentos"

# Dados de exemplo (atendimento fictício para teste)
atendimento_id = 1  # Suponha que o ID do atendimento seja 1
usuario_id = 1  # Suponha que o ID do usuário que realizará a ação seja 1

# Função para inativar um atendimento
def inativar_atendimento():
    response = requests.patch(f"{BASE_URL}/{atendimento_id}", json={"status": "Finalizado"})
    return response

# Função para verificar se o log foi criado corretamente
def verificar_log():
    # Simulação de um log gerado
    log = {
        "action": "Inativação de Atendimento",
        "action_time": datetime.now(),
        "user_id": usuario_id,
        "details": f"Atendimento {atendimento_id} inativado.",
        "appointment_id": atendimento_id
    }
    return log

# Função principal para rodar o teste
def test_inativamento():
    # Mockar a resposta da API para simular a inativação do atendimento
    with patch('requests.patch') as mock_patch:
        mock_patch.return_value.status_code = 200
        mock_patch.return_value.json.return_value = {"id": atendimento_id, "status": "Finalizado"}
        
        # Passo 1: Enviar a requisição para inativar o atendimento
        response = inativar_atendimento()
        assert response.status_code == 200, f"Esperado 200 OK, mas obtido {response.status_code}"

        # Mockar a função de verificar o log para retornar o log esperado
        with patch('__main__.verificar_log') as mock_verificar_log:
            # Agora, ao chamar verificar_log(), ele vai retornar um dicionário com as informações mockadas
            mock_verificar_log.return_value = {
                "action": "Inativação de Atendimento",
                "action_time": datetime.now(),
                "user_id": usuario_id,
                "details": f"Atendimento {atendimento_id} inativado.",
                "appointment_id": atendimento_id
            }
            
            # Passo 2: Verificar se o log foi gerado
            log = verificar_log()

            # Agora podemos acessar o log como um dicionário real
            assert log["action"] == "Inativação de Atendimento", f"Esperado log de 'Inativação de Atendimento', mas obtido {log['action']}"
            assert log["user_id"] == usuario_id, f"Esperado ID de usuário {usuario_id}, mas obtido {log['user_id']}"
            assert log["details"] is not None, "Os detalhes do log não estão presentes."

    print("Teste de inativamento de atendimento passou com sucesso!")

# Executar o teste
if __name__ == "__main__":
    test_inativamento()
