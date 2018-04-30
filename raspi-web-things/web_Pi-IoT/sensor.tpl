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
</head>

<body>


<div class="container">
<header class="jumbotron hero-spacer">

        <h1>Sensor de temperatura</h1>
        <p>Datos del sensor DS18B20</p>
    </header>

<div id="containerxxx" style="min-width: 300px; height: 300px; margin: 0 auto"></div>


<!-- Tabla para insertar los ultimos valores de temperatura registrados. -->

<div class="container">
<div class="row">
<div class="col-md-6">
  <h2>Historial</h2>

<br>

<!-- Boton Dropdown para seleccionar la cant de registros a mostrar!. -->
<div class="panel-body">

<div class="row">
  <div class="col-md-6">Cantidad de registros a mostrar: </div>
  <div class="col-md-1"></div> 

<!--Default buttons with dropdown menu-->
<div class="btn-group">
<button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle">
<span id="selected">Seleccionar</span>
<span class="caret"></span>
</button>
 <ul class="dropdown-menu">
   <li><a href="#">5</a></li>
   <li><a href="#">10</a></li>
   <li><a href="#">15</a></li>
 </ul>
</div>

</div>

</div>

<br>

<!-- Tabla en donde se muestran los registros de temp!. -->
  <div class="table-responsive">          
  <table class="table table-striped" id="temp_table">
    <thead>
      <tr>
        <th>Fecha y hora</th>
	<th>Temperatura</th>	
     </tr>
    </thead>
    <tbody>
      <tr>
<!--    <td>Bla bla</td> -->
     </tr>
    </tbody>
  </table>
  </div>
</div>
</div>
</div>


<!-- Cuadro con resumen que muestra: temp maxima, temp minima y fecha y hora de actualizacion de los datos!. -->
<div class="row">
<div class="col-md-6">

 <div class="panel panel-primary">

<div class="panel-heading">
  <h3 class="panel-title">Resumen</h3>
  </div>

<div class="panel-body">

<div class="row">
  <div class="col-md-4" id="summary_item1"></div>
<!--  <div class="col-md-1"></div> -->
  <div class="col-md-4" id="min_temp"></div>
</div>
<br>
<div class="row">
  <div class="col-md-4" id="summary_item2"></div>
<!--  <div class="col-md-1"></div> -->
  <div class="col-md-4" id="max_temp"></div>
</div>
<br>
<div class="row">
  <div class="col-md-4" id="summary_item3"></div>
<!--  <div class="col-md-1"></div> -->
  <div class="col-md-4" id="avg_temp"></div>
</div>

</div>   

  </div>

</div>
</div>


  <div class="container">
   <div class="row">
     <div class="col-md-8 col-md-offset-8">
      <p><a class="btn btn-primary btn-lg" href="/" role="button">Volver &raquo;</a></p>
    </div>
 </div>
</div>
 
      <hr>

      <footer>
        <p align="center">&copy; 2018 Pi-IoT Panel Web</p>
      </footer>
    </div> <!-- /container -->


<!-- Bootstrap core JavaScript  -->
<script src="https://code.jquery.com/jquery-1.12.0.min.js"></script> 
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/highcharts/2.3.1/highcharts.js"></script>
<script type="text/javascript" src="static/js/temperature_data.js"></script>

<!-- Placed at the end of the document so the pages load faster -->
<script src="http://code.highcharts.com/modules/exporting.js"></script>
 <script src="static/js/bootstrap.min.js"></script>


</body>
</html>
