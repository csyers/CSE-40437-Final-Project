
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
				dates = obj[1].split(" ");
				results = obj[0].split(" ");
				results2 = obj[2].split(" ");
				count = obj[3].split(" ");
				data = []
				data2 = []
				data3 = []
				for(i=0; i< dates.length; i++){
						data.push({date: dates[i], result: Number(results[i])});
						data2.push({date: dates[i], result: Number(results2[i])});
						data3.push({date: dates[i], result: Number(count[i])});
				}
				graph.setData(data);
				graph2.setData(data2);
				graph3.setData(data3);
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
var graph;
var graph2;
var graph3;
	  var product = $("#product").val();
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
				count = obj[3].split(" ");
				data = []
				data2 = []
				data3 = []
				for(i=0; i< dates.length; i++){
						data.push({date: dates[i], result: Number(results[i])})
						data2.push({date: dates[i], result: Number(results2[i])})
						data3.push({date: dates[i], result: Number(count[i])})
				}
				console.log(data[0]);
						graph = new Morris.Line({
							element: 'graph',
							data: data,
							xkey: 'date',
							ykeys: ['result'],
								labels:['Sentiment Levels'],
								ymin: 0,
								ymax: 5
						});
				graph2 = new Morris.Line({
							element: 'graph2',
							data: data2,
							xkey: 'date',
							ykeys: ['result'],
						labels:['Sentiment Levels']
						});

				graph3 = new Morris.Line({
							element: 'graph3',
							data: data3,
							xkey: 'date',
							ykeys: ['result'],
						labels:['Tweets Collected']
						});

                var title = product.split(".")[0].split("_")
                for (i = 0; i < title.length; i++) {
										title[i] = title[i].charAt(0).toUpperCase() + title[i].substring(1);
                }
				var fixed_title = title.join(" ");
				$("#title").text(fixed_title)
				var image = "../../images/" + product.split(".")[0] + ".png"
				$("#word_cloud").attr("src",image);
				
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
