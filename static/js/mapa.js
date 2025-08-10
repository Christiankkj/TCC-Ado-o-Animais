// Função para inicializar o mapa dado um centro
function initMap(lat, lng) {
    window.map = L.map('map').setView([lat, lng], 14);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap'
    }).addTo(map);


    // Depois adicione os demais marcadores (denuncias e pontos)
    addMarkers();
}

// Função para adicionar os marcadores de denúncias e pontos
function addMarkers() {
    const markerRefs = {};

    denuncias.forEach((denuncia) => {
        const [lat, lng] = denuncia.cordenada.split(',').map(Number);
        const coordKey = `${lat},${lng}`;

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

        markerRefs[coordKey] = circle;
    });

    pontos.forEach((ponto) => {
        const [lat, lng] = ponto.cordenada.split(',').map(Number);
        const coordKey = `${lat},${lng}`;

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

        markerRefs[coordKey] = marker;
    });

    // Evento para links das coordenadas
    document.querySelectorAll('.coord-link').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();

            const lat = parseFloat(this.dataset.lat);
            const lng = parseFloat(this.dataset.lng);

            focusOnCoord(lat, lng, markerRefs);
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });
}

// Função para focar no marcador e abrir popup
function focusOnCoord(lat, lng, markerRefs) {
    const coordKey = `${lat},${lng}`;
    const item = markerRefs[coordKey];
    if (item) {
        map.flyTo([lat, lng], 18, { duration: 1.0 });
        setTimeout(() => item.openPopup(), 800);
    }
}

// Tentar pegar localização do usuário primeiro
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
        (position) => {
            initMap(position.coords.latitude, position.coords.longitude);
        },
        (error) => {
            console.warn("Geolocalização não disponível, usando padrão.");
            // Usar localização padrão se falhar
            initMap(-10.505872, -39.018019);
        }
    );
} else {
    // Se navegador não suportar geolocalização
    initMap(-10.505872, -39.018019);
}