
$("#view").on("submit", function(event){
		if(event.isDefaultPrevented()){
				console.log("something went wrong");
		}else {
				event.preventDefault();
				changeGraph();
		}
});
 
function changeGraph() {
		var product = $("#product").val();
		console.log(product)
		$.get({
				url: "../php/data.php",
				data: {
						product: product
				}
		}).done(function(output, status){
				var obj = JSON.parse(output);
				console.log(obj[0]);
				console.log(obj[1]);
				dates = obj[1].split(" ");
				results = obj[0].split(" ");
				data = []
				for(i=0; i< dates.length; i++){
						data.push({date: dates[i], result: Number(results[i])})
				}
				console.log(data[0]);
				graph.setData(data);
				$("#title").text(product.split(".")[0])
				
		}).fail(function(err){
				console.log("Hi");
				console.log(err);
		});
}
var graph;
	  var product = $("#product").val();
		console.log(product)
		$.get({
				url: "../php/data.php",
				data: {
						product: product
				}
		}).done(function(output, status){
				var obj = JSON.parse(output);
				console.log(obj[0]);
				console.log(obj[1]);
				dates = obj[1].split(" ");
				results = obj[0].split(" ");
				data = []
				for(i=0; i< dates.length; i++){
						data.push({date: dates[i], result: Number(results[i])})
				}
				console.log(data[0]);
						graph = new Morris.Line({
							element: 'graph',
							data: data,
							xkey: 'date',
							ykeys: ['result'],
							labels:['Sentiment Levels']
						});
                
                var title = product.split(".")[0].split("_")
                var fixed_title = ""
                for (i = 0; i < length(title); i++) {
                    var first_letter = ttitle[i].charAt(0)
                    first_letter = first_letter.concat()
                    fixed_title = first_letter.toUpperCase().concat(title[i][1:].concat(" ")) 
                }
				$("#title").text(fixed_title)
				
		}).fail(function(err){
				console.log("Hi");
				console.log(err); 
		});







/*
new Morris.Line({
  // ID of the element in which to draw the chart.
  element: 'graph',
  // Chart data records -- each entry in this array corresponds to a point on
  // the chart.
  data: [
    { year: '2008', value: 20 },
    { year: '2009', value: 10 },
    { year: '2010', value: 5 },
    { year: '2011', value: 5 },
    { year: '2012', value: 20 }
  ],
  // The name of the data record attribute that contains x-values.
  xkey: 'year',
  // A list of names of data record attributes that contain y-values.
  ykeys: ['value'],
  // Labels for the ykeys -- will be displayed when you hover over the
  // chart.
  labels: ['Value']
});
*/
