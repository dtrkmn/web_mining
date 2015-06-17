$.ajax({
        url: "chart4_query",
        dataType: "json",
        /* beforeSend: function() {
          loader_gif.show();
          console.log("beforeSend");
        }, 
        complete: function() {
          loader_gif.hide();
        }, */
        success: function( datam ) {
           createChart(datam);
        }
})
function createChart(datam) {
	        
			var json_data = JSON.stringify(datam);
			var result = JSON.parse(json_data);
			
			console.log(json_data)

			console.log(result)
	        $('#chart4').highcharts({
            chart: {
                type: 'pie',
            options3d: {
                enabled: true,
                alpha: 45,
                beta: 0
            }},
            title: {
                text: 'Social Analysis'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false
                    },
                    showInLegend: true
                }
            },
			
            series: [{
                type: 'pie',
                name: 'Rate',
                data: result
				}]
        });
	
	
	
}
