if (document.getElementById("map")) {
	let x = document.getElementById("map").getAttribute("x");
	let y = document.getElementById("map").getAttribute("y");

	let mapOptions = {
		center: [x, y],
		zoom: 100
	}

	let map = new L.map('map' , mapOptions);

	let layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
	map.addLayer(layer);

	let marker = new L.Marker([x, y]);
	marker.addTo(map);
}