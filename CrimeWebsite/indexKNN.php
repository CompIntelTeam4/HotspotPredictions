
<?php 
    $string = file_get_contents("KNN_GEO_12M.json");
?>

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8' />
<title>KNN</title>
<meta name='viewport' content='initial-scale=1,maximum-scale=1,user-scalable=no' />
<script src='https://api.tiles.mapbox.com/mapbox-gl-js/v1.5.0/mapbox-gl.js'></script>
<link href='https://api.tiles.mapbox.com/mapbox-gl-js/v1.5.0/mapbox-gl.css' rel='stylesheet' />
<style>
body { margin:0; padding:0; }
#map { position:absolute; top:0; bottom:0; width:100%; }
</style>
</head>
<body>
 
<div id="map"></div>
<script>
mapboxgl.accessToken = 'pk.eyJ1IjoibG11cmRvY2sxMiIsImEiOiJjazJ1d2NobHIwM3ZzM2J0ZjdicTRhN3hjIn0.M3xbhDRz12zcYBnCDZPBnA';
var map = new mapboxgl.Map({
container: "map",
style: "mapbox://styles/mapbox/streets-v11",
center: [-86.403732, 36.1627],
zoom: 10
});
 
map.on("load", function() {
    map.addSource("grid_cords", <?php echo $string ?>);
 
map.addLayer({
"id": "gridPredictedHotspots",
"type": "fill",//"fill",
"source": "grid_cords",
"paint": {
"fill-color": "#FF0000",
"fill-opacity": 0.25
},
"filter": ["==", "PredictHot",1]
});
map.addLayer({
"id": "gridActualHotspots",
"type": "fill",//"fill",
"source": "grid_cords",
"paint": {
"fill-color": "#0000FF",
"fill-opacity": 0.25
},
"filter": ["==", "ActualHot",1]
});

map.addLayer({
"id": "gridCombinedHotspots",
"type": "fill",//"fill",
"source": "grid_cords",
"paint": {
"fill-color": "#00FF00",
"fill-opacity": 0.50
},
"filter":['all', ["==", "ActualHot",1],['==','PredictHot',1]]
});
 
map.addLayer({
"id": "grid_unfilled",
"type": "line",//"fill",
"source": "grid_cords",
"paint": {
"line-color": "#FF0000",
"line-width":.5,
//"fill-opacity": 0.5
"line-opacity":.5
},
//"filter": ["<=", "id",1500]
});
//map.getSource("grid_cords")["_data"]['features'][0]['properties']['id'].toString()
//map.setFilter(map.getSource("grid_cords"),[">","id",1500])
console.log(map.getSource("grid"))




//on load end mark
});

//console.log(map.isSourceLoaded("grid"))
</script>


</body>
</html>