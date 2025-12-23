# 🌡️SMT-IoT - Sistema de Monitoramento de Temperatura IoT

Projeto de **monitoramento de temperatura em tempo real** utilizando **Raspberry Pi Pico W**, **Django** e **Chart.js**, desenvolvido com foco em aplicações **IoT**, aprendizado acadêmico e uso como **portfólio profissional**.

---

## 📌 Visão Geral

O sistema coleta dados de temperatura a partir do **sensor interno do Pico W**, envia essas informações via **Wi‑Fi** para um servidor **Django**, armazena em banco de dados e exibe os valores em um **gráfico dinâmico no navegador**, atualizado automaticamente sem necessidade de recarregar a página.

---

## 🛠️ Tecnologias Utilizadas

### 🔌 Hardware

* Raspberry Pi Pico W
* Sensor de temperatura interno

### 💻 Backend

* Python 3.12
* Django
* SQLite (pode ser substituído por PostgreSQL/MySQL)

### 🌐 Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

### 📡 Comunicação

* HTTP (POST/GET)
* API REST

---

## ⚙️ Funcionalidades

* 📤 Recebimento de dados de temperatura via API
* 💾 Armazenamento das leituras no banco de dados
* 📈 Gráfico de temperatura atualizado automaticamente
* ⏱️ Registro de data e hora de cada leitura
* 🔄 Atualização contínua sem uso de F5

---

## 📁 Estrutura do Projeto

```
SISTEMA-DE-MONITORAMENTO-DE-TEMPERATURA/
│
├── picoiot/
│   ├── sensores/
│   │   ├── migrations/
│   │   ├── static/
│   │   │   ├── sensores/css/style.css
│   │   │   └── sensores/js/grafico.js
│   │   ├── templates/
│   │   │   └── sensores/grafico.html
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   └── settings.py
│
├── manage.py
└── README.md
```

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone <url-do-repositorio>
cd SISTEMA-DE-MONITORAMENTO-DE-TEMPERATURA
```

### 2️⃣ Criar e ativar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependências

```bash
pip install django
```

### 4️⃣ Aplicar migrações

```bash
python manage.py migrate
```

### 5️⃣ Iniciar o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/grafico/
```

---

## 📡 API Endpoints

### 🔹 Enviar temperatura (Pico W)

```
POST /api/temperatura/
```

**JSON esperado:**

```json
{
  "temperatura": 25.6
}
```

---

### 🔹 Obter dados para o gráfico

```
GET /api/dados/
```

**Resposta:**

```json
[
  { "valor": 25.6, "hora": "15:23:50" },
  { "valor": 25.7, "hora": "15:24:00" }
]
```

---

## 📈 Melhorias Futuras

* 🔐 Autenticação por token para o Pico W
* 📊 Estatísticas (mínima, máxima, média)
* ⚡ WebSocket (tempo real sem polling)
* 📡 MQTT para comunicação IoT
* ☁️ Deploy em servidor cloud
* 📥 Exportação CSV/PDF

---

## 🎓 Aplicações do Projeto

* Projeto acadêmico (PIBITI / TCC)
* Portfólio profissional
* Monitoramento industrial
* Estufas inteligentes
* Automação residencial

---

## 👨‍💻 Autor

**Everton Santos**
Licenciatura em Computação
Projeto com foco em IoT, Web e Sistemas Distribuídos

---

## 📜 Licença

Este projeto é de uso educacional. Sinta-se livre para estudar, modificar e evoluir 🚀
