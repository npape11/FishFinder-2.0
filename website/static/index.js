// Function to initialize the map
function initMap() {
    // Create the map with a default center location
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 40.0583, lng: -74.4057 }, // Default: New Jersey
        zoom: 8
    });

    // Create a marker at the initial map center position
    const marker = new google.maps.Marker({
        map: map,
        position: { lat: 40.0583, lng: -74.4057 },
        title: "Fish",
        draggable: true  // Allow the user to drag the marker
    });

    // Add a listener for clicks on the map to update the marker and store coordinates
    map.addListener("click", function (event) {
        const lat = event.latLng.lat();
        const lng = event.latLng.lng();

        // Update the marker position
        marker.setPosition(event.latLng);

        // Store the latitude and longitude in the hidden input fields
        document.getElementById("latitude").value = lat;
        document.getElementById("longitude").value = lng;

        console.log(`Latitude: ${lat}, Longitude: ${lng}`); // Debugging
    });
}

// Make sure to initialize the map once the script is loaded
window.initMap = initMap;

window.onload = function() {
    initMap();
};
