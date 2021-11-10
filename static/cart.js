function plus() {
  var value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 0 : value;
  value++;
  document.getElementById('number').value = value;
}

function minus() {
  var value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 0 : value;
  value < 1 ? value = 1 : '';
  value--;
  document.getElementById('number').value = value;
}

/*$(document).ready(function () {

        $('.increment-btn').click(function (e) {
            e.preventDefault();
            var incre_value = $(this).parents('.quantity').find('.qty-input').val();
            var value = parseInt(incre_value, 10);
            value = isNaN(value) ? 0 : value;
            if(value<10){
                value++;
                $(this).parents('.quantity').find('.qty-input').val(value);
            }

        });

        $('.decrement-btn').click(function (e) {
            e.preventDefault();
            var decre_value = $(this).parents('.quantity').find('.qty-input').val();
            var value = parseInt(decre_value, 10);
            value = isNaN(value) ? 0 : value;
            if(value>1){
                value--;
                $(this).parents('.quantity').find('.qty-input').val(value);
            }
        });

    });
*/

/*function showp() {
    // body...
    var rs = document.getElementById('price').value;
    var qt = document.getElementById('qty').value;
    var val = rs
    var total = rs*qt+val;
    document.getElementById('total').value = total;

  }
 function showm() {
    // body...
    var rs = document.getElementById('price').value;
    var qt = document.getElementById('qty').value;
    var val = rs
    var total = rs*qt-val
    if(total===0)
    {
      document.getElementById('total').value= rs;
      console.log(rs)
    }
    else{
      document.getElementById('total').value= total;
      console.log(total)
    }
    

  }
 