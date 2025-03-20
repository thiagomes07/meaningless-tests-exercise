const express = require('express');
const app = express();
const port = 3000;

// Importar as rotas mockadas
const mockAppointmentsRoute = require('./mock/appointments');

// Usar as rotas mockadas
app.use(express.json());
app.use('/mock/atendimentos', mockAppointmentsRoute);

// Inicializar o servidor
app.listen(port, () => {
  console.log(`Servidor de mock rodando na porta ${port}`);
});
