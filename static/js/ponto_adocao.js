const map = L.map('map').setView([-10.505872, -39.018019], 14);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

let marker;

map.on('click', function(e) {
    const latlng = e.latlng.lat.toFixed(6) + ',' + e.latlng.lng.toFixed(6);
    document.getElementById('cordenada').value = latlng;

    if (marker) {
        map.removeLayer(marker);
    }

    marker = L.marker(e.latlng).addTo(map);
});
denuncias.forEach((denuncia) => {
    const [lat, lng] = denuncia.cordenada.split(',').map(Number);
    const circle = L.circle([lat, lng], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: 30
    }).addTo(map);

    circle.bindPopup(`
        <b>Denúncia</b><br>
        Tipo: ${denuncia.tipo_animal}<br>
        Quantidade: ${denuncia.quantidade}
    `);
});

// Adicionar pontos de adoção
pontos.forEach((ponto) => {
    const [lat, lng] = ponto.cordenada.split(',').map(Number);
    const marker = L.marker([lat, lng], {
        icon: L.icon({
            iconUrl: 'https://cdn-icons-png.flaticon.com/512/1796/1796995.png',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        })
    }).addTo(map);

    marker.bindPopup(`
        <b>Ponto de Adoção</b><br>
        Local: ${ponto.nome_local}<br>
        Tipo: ${ponto.tipo_animal}<br>
        Disponíveis: ${ponto.quantidade_disponivel}
    `);
});