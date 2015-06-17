$(document).ready( function() {
  
  
  $("#searchButton").click(function(event) {
      var term = $("#search").val()
                
      $.ajax({
        url: "query_title",
        data: { title: term },
        dataType: "json",
		
        beforeSend: function() {
          

        },
        complete: function() {
		

		
        },
        success: function( data ) {
		data: { title: term }		
			
			var series_names = []
    series = []
    series.push( { name: "derece", data: [] } )
	series.push( { isim: "name", data: [] } )
    
    data.forEach(function(fac) {
        series_names.push(fac.name);
        series[0].data.push(fac["derece"]);
                
    });
	series[0].dataLabels = {
       'style': { 'fontSize': "12px"}
    }
	console.log(data);
    console.log(series_names);
    console.log(series);
			
			  $(function () {
		  
    $('#chart3').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'AVERAGE OF SEASONS '
        },
        subtitle: {
            text: 'MADE IN BY tv.com'
        },
        xAxis: {
            categories:series_names,
            
        },
       
        tooltip: {
            
        },
        plotOptions: {
            column: {
                dataLabels: {
                    enabled: true,
                    allowOverlap: true,
                    style: { 'fontSize': "8px" }
                }
            }
        },
		legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            // x: 40,
            // y: 100,
            // floating: true,
            borderWidth: 1,
            backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
            shadow: true
        },
        credits: {
            enabled: false
        },
        series: series
        
        
    });
});
         
        },
      })   
          
  })  
	
}) // document.ready

















