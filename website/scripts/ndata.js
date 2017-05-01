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


 
function changeGraph() {
		var product = $("#newterm").val();
		console.log(product)
		$.get({
				url: "../php/data.php",
				data: {
						product: product
				}
		}).done(function(output, status){
				var obj = JSON.parse(output);
				dates = obj[1].split(" ");
				results = obj[0].split(" ");
				results2 = obj[2].split(" ");
				data = []
				data2 = []
				for(i=0; i< dates.length; i++){
						data.push({date: dates[i], result: Number(results[i])});
						data2.push({date: dates[i], result: Number(results2[i])});
				}
				graph.setData(data);
				graph2.setData(data2);
				                var title = product.split(".")[0].split("_")
                for (i = 0; i < title.length; i++) {
										title[i] = title[i].charAt(0).toUpperCase() + title[i].substring(1);
                }
				var fixed_title = title.join(" ");
				$("#title").text(fixed_title);
				var image = "../../images/" + product.split(".")[0] + ".png"
				$("#word_cloud").attr("src",image); 

				
		}).fail(function(err){
				console.log(err);
		});
}
