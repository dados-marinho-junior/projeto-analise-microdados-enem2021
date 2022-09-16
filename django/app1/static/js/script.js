// Json para os gráficos highcharts

Highcharts.chart('container', {
    title: {
      text: 'Frequencia de alunos de 2017 a 2021',
      align: 'left'
    },
    xAxis: {
      categories: [2017, 2018, 2019, 2020, 2021]
    },
    yAxis: {
      title: {
        text: 'Inscritos'
      }
    },
    series: [{
      type: 'column',
      name: 'Inscritos',
      data: [6731278, 5513373, 5095171, 5783109, 3389832],
    }, {
      type: 'column',
      name: 'Partcipantes',
      data: [4426692, 3893729, 3701910, 2588681, 2238107]
    },  {
      type: 'spline',
      name: 'Faltas',
      data: [2304586, 1620004, 1393261, 3194428, 1151725],
      marker: {
        lineWidth: 2,
        lineColor: Highcharts.getOptions().colors[2],
        fillColor: 'white'
      }
    }]
  });
  
  Highcharts.chart('container2', {
    title: {
      text: 'Média Inscritos x Média Participantes de 2017 a 2021',
      align: 'left'
    },
    xAxis: {
      categories: [2017, 2018, 2019, 2020, 2021]
    },
    yAxis: {
      title: {
        text: 'Médias'
      }
    },
    series: [{
      type: 'column',
      name: 'Média Inscritos',
      data: [346.18, 380.12, 384.37, 237.21, 354.83],
    }, {
      type: 'column',
      name: 'Média Participantes',
      data: [511.01, 520.25, 514.81, 517.99, 527.04]
    },]
  });