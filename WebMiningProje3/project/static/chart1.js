$.ajax({
        url: "chart1_query",
        dataType: "json",
        /* beforeSend: function() {
          loader_gif.show();
          console.log("beforeSend");
        },
        complete: function() {
          loader_gif.hide();
        }, */
        success: function( data ) {
           createChart(data);
        }
})
function createChart(data) {
    
    var series_names = []
    series = []
    series.push( { name: "oylama", data: [] } )
	series.push( { isim: "isim", data: [] } )
    
    data.forEach(function(fac) {
        series_names.push(fac.isim);
        series[0].data.push(fac["oylama"]);
		
                
    });

    series[0].dataLabels = {
       'style': { 'fontSize': "12px"}
    }

    console.log(data);
    console.log(series_names);
    console.log(series);
    $('#chart1').highcharts({
        chart: {
            type: 'column',
            margin: 75,
            options3d: {
                enabled: true,
                alpha: 15,
                beta:15,
                depth: 100
            }
        },
        title: {
            text: 'Top Ten Series'
        },
        subtitle: {
            text: 'Made in by tv.com'
        },
        plotOptions: {
            column: {
                depth: 45
            }
        },
        xAxis: {
            categories: series_names
        },
        yAxis: {
            title: {
                text: null
            }
        },
        series: series
    });
}
