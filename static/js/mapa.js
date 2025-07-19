const map = L.map('map').setView([-10.505872, -39.018019], 14);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


function onMapClick(e) {
    const latlng = e.latlng; 
    
  
    const circle = L.circle(latlng, {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: 30
    }).addTo(map);
    

    circle.bindPopup("Foram avistados x animais aqui.").openPopup();

    console.log("Coordenadas clicadas:", latlng.lat, latlng.lng);
}

map.on('click', onMapClick);



