
function random_integer(min, max) {
  return Math.floor(Math.random() * (max - min) ) + min;
}

function fetch(){
	var jqxhr = $.getJSON(random_module_url, function() {
		console.log( "success" );
	})
	.done(async function(json) {
		await new Promise(resolve => setTimeout(resolve, 500));
		$("#django-class").html(json.classpath);
		$('#running-program').prop('title', json.size + ' bytes');

		for (char of json.data){
			if (char == ' '){
				var duration = random_integer(40, 120);
			}
			await new Promise(resolve => setTimeout(resolve, duration));
		    $('#code-runner').append(char);
		    if (char == '\n' || true){
		      var code_so_far = $('#code-runner').text();
		      code_so_far = hljs.highlight('python', code_so_far).value
		      $('#code-runner').html(code_so_far);
		    }
		}
	})
}

$(document).ready(function() {
    fetch();
});
