<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1"> 

  <title>Pi-IoT panel web</title>

  <!-- Bootstrap core CSS -->
  <link href="static/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="static/css/jumbotron.css" rel="stylesheet">

  <!-- Toggle switch  --> 
  <link href="static/css/toggle_switch.css" rel="stylesheet">


</head>

<body>


<div class="container">

<header class="jumbotron hero-spacer">
       <h1>Pi-IoT panel web</h1>
        <p>Bienvenido al panel web de la Internet de las Cosas, basado en la Raspberry Pi!.</p>
        <p><a class="btn btn-primary btn-lg" href="#" role="button">Acerca de... &raquo;</a></p>
      </header>

    <div class="container">
      <!-- Example row of columns -->
      <div class="row">
        <div class="col-md-4">

          <h2>Gestor de LEDs</h2>

         <!-- <p><a class="btn btn-default" href="/led" role="button">Acceder &raquo;</a></p> -->
        <div class="sliderWrapper">
        <div><h5>LED 1:</h5></div> 
         <!-- Rounded switch -->
         <label class="switch">
         <input type="checkbox" id="led-1" onclick="led_handler()">
         <span class="slider round"></span>
        </label>
        </div>


        <div class="sliderWrapper">
        <div><h5>LED 2:</h5></div>
       <label class="switch">
       <input type="checkbox" id="led-2" onclick="led_handler()">
       <span class="slider round"></span>
       </label>
       </div>


       <div class="sliderWrapper">
       <div><h5>LED 3:</h5></div>
       <label class="switch">
       <input type="checkbox" id="led-3" onclick="led_handler()">
       <span class="slider round"></span>
       </label>
       </div>

        </div>

        <div class="col-md-4">
          <h2>Sensor de temperatura</h2>
          <p>Visualiz&aacute; los datos obtenidos por el sensor de temperatura DS18B20!. </p>
          <p><a class="btn btn-default" href="/sensor" role="button">Acceder &raquo;</a></p>
       </div>

      </div>

	<br>
      <hr>

      <footer>
	<div class="row">
         <div class="col-lg-12">
            <p align="center">&copy; 2018 Pi-IoT Panel Web</p>  
         </div>
        </div>
      </footer>



    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="js/vendor/jquery.min.js"><\/script>')</script>
    <script src="static/js/bootstrap.min.js"></script>
    <script src="static/js/led_handler.js"></script>
 

</body>
</html>
