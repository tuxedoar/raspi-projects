<!DOCTYPE html>

<!-- Copyright Tuxedoar 2018 -->

<html>
    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1"> 
        <title>WebSocket demo</title>

 <!-- Bootstrap core CSS -->
   <link href="static/css/bootstrap.min.css" rel="stylesheet">

<!-- Custom styles for this template -->
   <link href="static/css/jumbotron.css" rel="stylesheet">

   <style media="screen" type="text/css">
     .img-responsive {
        margin: 0 auto;
        }
   </style>



  </head>
    <body>

<div class="container">
  <div class="jumbotron">
   <h1 align="center">Temperature sensor with the Raspberry Pi</h1>
   <p class="lead" align="center">Real time graph with websockets</p>
  </div>
</div>


<div class="row">
  <div class="col-md-4"></div>
  <div class="col-md-4"> <canvas id='tempChart' width='400' height='400'></canvas> </div>
  <div class="col-md-4"></div>
</div>

<br>
<br>

<hr>

<footer>
  <p align="center">&copy; 2018 Tuxedoar</p>
</footer>


    <script src="https://code.jquery.com/jquery-1.12.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.js" ></script>
    <script>

    $(document).ready(function() {

     // Setup the temperature chart!.
     var ctx = document.getElementById("tempChart").getContext("2d");
     var tempChart = new Chart(ctx, {
 
     type: 'line',
     data: {
         labels: [],
         datasets: [
                {
                  label: "Temperature (Celsius)",
                  backgroundColor: "#e0e0e0",
                  strokeColor: "rgba(220,220,220,1)",
                  pointColor: "rgba(220,220,220,1)",
                  borderColor: "#9bb9e5",
                  pointStrokeColor: "#fff",
                  pointHighlightFill: "#fff",
                  pointHighlightStroke: "rgba(220,220,220,1)",
                  data: [],
                  fill: true
                }]
           },

     // Set options for the temp chart!.
           options: {
             scales: {
               yAxes: [{
                 ticks: {
                    beginAtZero: true,
                    // min: -5,
                    max: 50,
                    stepSize: 5
                }
            }]
        }
    }	
      // END of the temp chart options!.

         });


    
            // Setup the connection to the websocket server!. 

            // Replace with your IP address on this line!!.
            var ws = new WebSocket("ws://192.168.0.20:5678/");
            var mensajes = document.createElement('p');

            ws.onmessage = function (event) {
              tempValue = event.data;
              tempValue = parseFloat(tempValue);
              t = new Date();
              t = t.toLocaleTimeString()
              <!-- console.log(tempValue); -->
             
            // Fill chart with temperature values.

            setTimeout(function() {

            tempChart.data.labels.push(t);
            tempChart.data.datasets[0].data.push(tempValue);
            

            // Keep 20 values in the tempChart and remove the oldest data point.
            if (tempChart.data.datasets[0].data.length > 20) {
              tempChart.data.datasets[0].data.splice(0, 1);   // remove first data point
              tempChart.data.labels.splice(0, 1);             // remove first label. The pop() method, removes last element last element from array!.
             }

            tempChart.update();
            }, 2000);

      };

       // End of the jQuery function!.
        });
        </script>


    </body>
</html>
