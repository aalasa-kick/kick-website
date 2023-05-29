// Initialize and add the map
let map;

async function initMap() {
  // The location of Kick Dublin
  const position = { lat: 53.3287, lng: -6.2129 };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Kick Dublin
  map = new Map(document.getElementById("map"), {
    zoom: 14,
    center: position,
    mapId: "fd93d6ae1877fd2b",
  });

  // The marker, positioned at Kick Dublin
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "KICK Dublin",
  });
}

initMap();