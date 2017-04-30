
$("#view").on("submit", function(event){
		if(event.isDefaultPrevented()){
				console.log("something went wrong");
		}else {
				event.preventDefault();
				changeGraph();
		}
});

function changeGraph() {
		var product = $("#product").value;
		$.get([{
				url: "../php/data.php",
				data: {
						product: product
				}
		}]).done(function(data, status){
				console.log(output)
		}).fail(function(err){
				console.log(err);
		});
}








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
