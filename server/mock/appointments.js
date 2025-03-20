const express = require('express');
const router = express.Router();

// Dados mockados
let appointments = [
  {
    id: 1,
    student_id: 123,
    status: 'Ativo',
    professional_id: 1,
    start_date: '2025-03-20',
    end_date: null,
    description: 'Atendimento inicial',
  },
];

// Endpoint para inativar o atendimento
router.patch('/:id', (req, res) => {
  const appointmentId = parseInt(req.params.id);
  const appointment = appointments.find((app) => app.id === appointmentId);

  if (!appointment) {
    return res.status(404).json({ error: 'Atendimento não encontrado' });
  }

  // Simulando o inativamento do atendimento (alterando o status para 'Finalizado')
  appointment.status = 'Finalizado';

  // Simulando a criação de um log (mock)
  const log = {
    action: 'Inativação de Atendimento',
    action_time: new Date(),
    user_id: 1,  // Usuário administrativo mockado
    details: `Atendimento ${appointmentId} inativado.`,
    appointment_id: appointmentId,
  };

  console.log('Log criado:', log);  // Simulando a criação do log no console

  // Retornar o atendimento atualizado
  res.status(200).json(appointment);
});

module.exports = router;
