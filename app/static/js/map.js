if (document.getElementById("map")) {
	let lat = document.getElementById("map").getAttribute("lat");
	let lon = document.getElementById("map").getAttribute("lon");

	let mapOptions = {
		center: [lat, lon],
		zoom: 100
	}

	let map = new L.map('map' , mapOptions);

	let layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
	map.addLayer(layer);

	let marker = new L.Marker([x, y]);
	marker.addTo(map);
}