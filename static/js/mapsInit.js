"use-strict";


let map;
// let service;
// let infowindow;

function initMap() {
    const stPaulCoords = {
        lat: 44.9544,
        lng: -93.0913
    };
  
    const basicMap = new google.maps.Map(
      document.querySelector('#map'),
      {
        center: stPaulCoords,
        zoom: 15
      }
    );

    const stPaulMarker = new.google.maps.Marker({
        position: stPaulCoords,
        title: 'Saint Paul'
        map: basicMap
    });

    const stpInfo = new google.maps.InfoWindow({
        content: '<h1>Saint Paul!</h1>'
    });

    stpInfo.open(basicMap, stPaulMarker);
};
