function led_handler() {

  var button_one = document.getElementById("led-1");
  var button_two = document.getElementById("led-2");
  var button_three = document.getElementById("led-3");

// Check if button is pressed
  if (button_one.checked == true){
     $.post('/led/17/on');
  } else {
     $.post('/led/17/off');
  }
 

// Check if button is pressed
  if (button_two.checked == true){
     $.post('/led/18/on');
  } else {
     $.post('/led/18/off');
  }


// Check if button is pressed
  if (button_three.checked == true){
     $.post('/led/27/on');
  } else {
     $.post('/led/27/off');
  }


}
