const ctx = document.getElementById('graficoTemperatura');

const MAX_PONTOS = 30;

let grafico = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperatura (°C)',
            data: [],
            borderWidth: 2,
            tension: 0.3
        }]
    },
    options: {
        responsive: true,
        animation: false,
        scales: {
            y: {
                beginAtZero: false
            }
        }
    }
});

async function atualizarDados() {
    try {
        const response = await fetch('/api/dados/');
        const dados = await response.json();

        if (dados.length === 0) return;

        const temperaturas = dados.map(item => Number(item.valor));
        const horarios = dados.map(item => item.hora);

        grafico.data.labels = horarios.slice(-MAX_PONTOS);
        grafico.data.datasets[0].data = temperaturas.slice(-MAX_PONTOS);
        grafico.update('none');

        document.getElementById('tempAtual').innerText =
            temperaturas.at(-1).toFixed(1) + ' °C';

        document.getElementById('tempMax').innerText =
            Math.max(...temperaturas).toFixed(1) + ' °C';

        document.getElementById('tempMin').innerText =
            Math.min(...temperaturas).toFixed(1) + ' °C';

    } catch (erro) {
        console.error('Erro ao atualizar dados:', erro);
    }
}

setInterval(atualizarDados, 2000);
atualizarDados();
