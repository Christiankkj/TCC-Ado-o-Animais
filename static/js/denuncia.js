document.addEventListener("DOMContentLoaded", function () {
    const map = L.map('map').setView([-10.505872, -39.018019], 14);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    let marcador = null; 

    function onMapClick(e) {
        const latlng = e.latlng;

   
        if (marcador !== null) {
            map.removeLayer(marcador);
        }

    
        marcador = L.circle(latlng, {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5,
            radius: 30
        }).addTo(map);

        marcador.bindPopup("Foram avistados x animais aqui.").openPopup();


        const campoCoord = document.getElementById('cordenada');
        if (campoCoord) {
            campoCoord.value = latlng.lat.toFixed(6) + ", " + latlng.lng.toFixed(6);
        }

        console.log("Coordenada clicada:", latlng.lat, latlng.lng);
    }

    map.on('click', onMapClick);
});
