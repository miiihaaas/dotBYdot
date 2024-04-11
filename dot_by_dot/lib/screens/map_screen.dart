import 'package:dot_by_dot/tour_info.dart';
import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:dot_by_dot/sidebar_menu.dart';
import 'dart:async';

class MapScreen extends StatefulWidget {
  final TourInfo tourInfo;
  const MapScreen({super.key, required this.tourInfo});

  @override
  _MapScreenState createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen> {
  late GoogleMapController _controller;
  final Completer<GoogleMapController> _controllerCompleter = Completer();
  final CameraPosition _initialCameraPosition =
      const CameraPosition(target: LatLng(42.077990, 22.179178));
  final CameraPosition _currentPosition =
      const CameraPosition(target: LatLng(42.077995, 22.179188));

  @override
  Widget build(BuildContext context) {
    print(widget.tourInfo);
    return Scaffold(
        appBar: AppBar(
          title: Text(widget.tourInfo.name),
        ),
        endDrawer: const SidebarMenu(),
        body: GoogleMap(
          onMapCreated: _onMapCreated,
          initialCameraPosition: CameraPosition(
            target: _initialCameraPosition.target,
            zoom: 18,
          ),
          markers: Set<Marker>.from(
            List.generate(
              widget.tourInfo.locations.length,
              (index) => Marker(
                markerId: MarkerId('location$index'),
                icon: BitmapDescriptor.defaultMarker,
                infoWindow: InfoWindow(
                  title: widget.tourInfo.locations[index].name,
                  snippet: widget.tourInfo.locations[index].short_description,
                ),
                position: LatLng(
                  widget.tourInfo.locations[index].latlng[0],
                  widget.tourInfo.locations[index].latlng[1],
                ),
              ),
            ),
          )..add(Marker(
              markerId: const MarkerId('currentPosition'),
              icon: BitmapDescriptor.defaultMarkerWithHue(
                  BitmapDescriptor.hueBlue),
              position: _currentPosition.target)),
        ),
        // footer na dnu stranice
        bottomNavigationBar: const BottomAppBar(
            child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [Icon(Icons.play_arrow), Icon(Icons.text_snippet)])));
  }

  /// Callback function that is called when the Google Map is created.
  ///
  /// This function completes the `_controllerCompleter` with the
  /// `GoogleMapController`.
  ///
  /// Parameters:
  /// - controller: The `GoogleMapController` that is created.
  void _onMapCreated(GoogleMapController controller) {
    // Completes the `_controllerCompleter` with the `GoogleMapController`.
    _controller = controller;
    _controllerCompleter.complete(controller);
  }
}
