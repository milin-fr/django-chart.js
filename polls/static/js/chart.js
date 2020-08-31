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
        const chartLabels = [];
        const chartData = [];
        response.data.forEach(element => {
          chartLabels.push(element.choice_text);
          chartData.push(element.votes);
        });
        const chartContainer = document.getElementById('myChart').getContext('2d');
        var myChart = new Chart(chartContainer, {
          type: 'bar',
          data: {
              labels: chartLabels,
              datasets: [{
                  label: '# of Votes',
                  data: chartData,
              }]
          },
          options: {
              scales: {
                  yAxes: [{
                      ticks: {
                          beginAtZero: true
                      }
                  }]
              }
          }
    })
  },
};

document.addEventListener('DOMContentLoaded', app.init);
