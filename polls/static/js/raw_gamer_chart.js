var app = {
    init: function() {
        console.log("init");
        app.getData();
    },
    getData: function() {
      const url = document.getElementById('myChart').dataset.url;
      axios.get(url, {
      })
      .then(function (response) {
        app.drawChart(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    },
    drawChart: function(response) {
        const chartData = [];
        response.data.forEach(element => {
          chartData.push({x:element.playtime, y:element.money_spent});
        });
        const chartContainer = document.getElementById('myChart').getContext('2d');
        var scatterChart = new Chart(chartContainer, {
          type: 'scatter',
          data: {
              datasets: [{
                  label: 'Gamers',
                  data: chartData
              }]
          },
          options: {
              scales: {
                  xAxes: [{
                      type: 'linear',
                      position: 'bottom',
                      scaleLabel: {
                        display: true,
                        labelString: 'Play time in hours'
                      }
                  }],
                  yAxes: [{
                    scaleLabel: {
                      display: true,
                      labelString: 'Money spent in euros'
                    }
                  }]
              }
          }
      });
  },
};

document.addEventListener('DOMContentLoaded', app.init);
