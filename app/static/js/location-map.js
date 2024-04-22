/*!
 * stats.wwdt.me (https://github.com/questionlp/stats.wwdt.me_v5)
 * Copyright 2018-2024 Linh Pham, Elijah Conners
 * Apache License 2.0 (https://github.com/questionlp/stats.wwdt.me_v5/blob/main/LICENSE)
 */


if (document.getElementById("map")) {
    const lat = document.getElementById("map").getAttribute("lat");
    const lon = document.getElementById("map").getAttribute("lon");
    const venue = document.getElementById("map").getAttribute("venue");

    const mapOptions = {
        center: [lat, lon],
        zoom: 100
    }

    const map = new L.map("map", mapOptions);
    map.attributionControl.setPrefix('<a href="https://leafletjs.com">Leaflet</a>');
    map.attributionControl.addAttribution('&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>');
    const layer = new L.TileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);
    const marker = L.marker([lat, lon], {"alt": venue}).addTo(map);
}
