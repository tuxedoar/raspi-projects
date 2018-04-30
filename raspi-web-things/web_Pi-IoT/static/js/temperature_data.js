// Get temperature graph, fill table with latest values and get a summary with minimum, maximum and average values.
  
     $(function () {

                    $.ajax({
                        type: "GET",
                        url: "static/temperatures.xml",
                        dataType: "xml",
                        success: function(xml) {

			/* 
			Create an array to be filled with time, date and temperature values. This array is then used to generate a table with these data. 
			*/
			var values = []

		  function graph_temp_values() {

                            Highcharts.setOptions({global:{useUTC:false}});
                            options={chart:{renderTo:"containerxxx",type:"spline"},title:{text:""},subtitle:{text:""},xAxis:{type:"datetime",dateTimeLabelFormats:{hour:"%H. %M"}},yAxis:{title:{text:"T (°C)"}},tooltip:{formatter:function(){return"<b>"+this.series.name+"</b><br/>"+Highcharts.dateFormat("%H:%M",this.x)+": "+this.y.toFixed(1)+"°C"}},plotOptions:{series:{marker:{radius:2}}},lineWidth:1,series:[]}
 
                            var series = []
                            //alert('start');

                            //define series
                            $(xml).find("entry").each(function() {
                                var seriesOptions = {
                                    name: $(this).text(),
                                    data: []
                                };
                                options.series.push(seriesOptions);
                            });
			
                            //alert('finish part 1');

                            //populate with data
                            $(xml).find("row").each(function() {
                                var t = parseInt($(this).find("t").text()) * 1000

                                $(this).find("v").each(function(index) {
                                    var v = parseFloat($(this).text())
                                    v = v || null
                                    if (v != null) {
                                        //alert('index = ' + index + 'time=' + t + 'v=' + v);
                                        options.series[index].data.push([t, v])
                                    };
                                });
                            });
                            //alert('finish part 2');

                            options.title.text = "Evolución de la temperatura en las últimas 24hs"
                            $.each(series, function(index) {
                                options.series.push(series[index]);
                            });
                            //alert('finish part 3');

                            chart = new Highcharts.Chart(options);
                        }


                        function fill_array_with_values() {
                            //populate with data
                            $(xml).find("row").each(function() {
                                var t = parseInt($(this).find("t").text()) * 1000
				// Set friendly format to the timestamp.	
				var t = new Date(t),
				t = t.toLocaleTimeString()
				
			
                                $(this).find("v").each(function(index) {
                                    var v = parseFloat($(this).text())
                                    v = v || null

				    if (v != null) {
			   			    
				    // Store time, date and temperature values on the created array!. 
				    values.push([t, v.toFixed(2)]); 


                                  };
				
                                });
                            });

			}
               

                       // Get minimum, maximum and average temperature values!. 
                        window.get_summary = function(){
                          var temperatures = [];
                          var total = values.length;
                          var sum = 0;

                          for(i=0; i < total; i++) {
                            var temp = values[i][1];
                            temperatures.push(temp);
                            sum += parseInt( temperatures[i], 10 );
                          }

                          minTemp = Math.min.apply(Math, temperatures);
                          maxTemp = Math.max.apply(Math, temperatures);
                          var avg = sum/temperatures.length;
                          var avg = avg.toFixed(2);

                          document.getElementById("summary_item1").innerHTML = "<label>" + "Temperatura m&iacute;nima: " + "</label>";
                          document.getElementById("min_temp").innerHTML = minTemp;

                          document.getElementById("summary_item2").innerHTML = "<label>" + "Temperatura m&aacute;xima: " + "</label>";
                          document.getElementById("max_temp").innerHTML = maxTemp;
 
                          document.getElementById("summary_item3").innerHTML = "<label>" + "Promedio: " + "</label>";
                          document.getElementById("avg_temp").innerHTML = avg;
                          
                        }


                      // This function takes an argument (n_values) which defines how many values to show on the table. 
                      window.show_table =  function(n_values){

                          var total = values.length;
                          var cont = 0;

        		var target = total - n_values;

                            for(i=0; i < total; i++) {
                                cont += 1

                                var date = values[i][0];
                                var temperature = values[i][1];

                                while(cont > target) {
                                        // console.log(valores[i]);
                                        $('#temp_table tbody').append('<tr class="child"><td>' + date + '</td>' + '<td>' + temperature + '</td>' + '</td>');
                                        break;
		                }
			   }
	              }     
            
		    // Allow the user to select how many values to show on the table. 
                    window.select_cant_registros_tabla =  $('.dropdown-menu li a').click(function(){

                       $('#selected').text($(this).text());
                       var selValue = $(this).text();

                       if (selValue != n_values) {
                             //var myvalue = tempValuesSelector.value;
                         var n_values = selValue;
                         $('#temp_table tbody').empty();  // Empty the table before updating it!.
                         show_table(n_values)
                       }  else {
 			  $('#temp_table tbody').empty(); // Empty the table before updating it!.
		          show_table(n_vaules)
			 }
                 });

		 // Set the number of values to show on the table on 5, by default!. 
                 n_values = 5

	         graph_temp_values()
                 // Call the functions to fill the array to be used to show temperature values on the table!. 
	         fill_array_with_values()
	         show_table(n_values)
                 get_summary()

	      }

      });

});
