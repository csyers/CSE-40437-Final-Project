// When "add" button is hit, add the new word to our list of tracked words
$("#view").on("submit", function(event){
		if(event.isDefaultPrevented()){
				console.log("something is wrong with the button");
		} else {
				event.preventDefault();
				//loadscreen();
				createNewSearch();
				//changeGraph();
		}
});


function createNewSearch() {
		var new_term = $("#newterm").val()
		$.get({
				url: "../php/ndata.php",
				data: {
						new_term: new_term
				}
		}).done(function(output,status){
		    console.log(output);
		}).fail(function(err){
		    console.log(err);
		});
}
