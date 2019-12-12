// Se crea un grafico para calcular la cantidad de bolsos vendidos
var ctx = document.getElementById('cantidadPromedio').getContext('2d');
var cantidad = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Grande', 'Pequeño', 'Escolar', 'Coleccion'],
        datasets: [{
            label: 'Reporte de Venta por Cantidad',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Reporte del Mes'
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
//Se crea un grafico sobre las ganancia dadas
var ctx = document.getElementById('ventas').getContext('2d');
var ventas = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Grande', 'Pequeño', 'Escolar', 'Coleccion'],
        datasets: [{
            label: 'Reporte de Venta por Cantidad',
            data: [50000, 75000, 32000, 12000],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Reporte del Mes'
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
//Se graficos sobre los ingresos totales
var ctx = document.getElementById('total').getContext('2d');
var total = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Enero', 'Febrero', 'Marzon', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        datasets: [{
            label: 'Reportes de ventas Total',
            data: [1000000, 232323232, 322334, 454545678, 666543, 232324, 2232434, 1223234, 5667, 4343434, 23049, 43943949],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(253, 99, 132, 0.2)',
                'rgba(52, 162, 235, 0.2)',
                'rgba(25, 206, 86, 0.2)',
                'rgba(79, 192, 192, 0.2)',
                'rgba(55, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(215, 206, 86, 0.2)',
                'rgba(5, 192, 192, 0.2)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Reporte de los Meses'
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});