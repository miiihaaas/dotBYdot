import 'package:dot_by_dot/consts.dart';
import 'package:dot_by_dot/localization/locales.dart';
import 'package:dot_by_dot/tour_info.dart';
import 'package:dot_by_dot/sidebar_menu.dart';
import 'package:flutter/material.dart';
import 'package:flutter_localization/flutter_localization.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:geolocator/geolocator.dart';
import 'package:location/location.dart' as location_package;
import 'dart:async';
import 'package:flutter_polyline_points/flutter_polyline_points.dart';

class MapScreen extends StatefulWidget {
  final TourInfo tourInfo;
  const MapScreen({super.key, required this.tourInfo});

  @override
  _MapScreenState createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen> {
  double _distanceInMeters = 0;
  bool _showFullBottomNavBar = false;
  String _description = 'Nema lokacije';
  int? _selectedMarkerIndex;
  final location_package.Location _locationController =
      location_package.Location();
  bool _followUserLocation = true; // Flag to control camera updates

  final Completer<GoogleMapController> _mapController =
      Completer<GoogleMapController>();

  static const _pKratovo = LatLng(42.077990, 22.179178);
  LatLng? _currentP;

  Map<PolylineId, Polyline> polylines = {};

  @override
  void initState() {
    super.initState();
    getLocationUpdates();
    // getLocationUpdates().then((_) => {
    //       getPolylinePoints().then((coordinates) => {
    //             generatePolylinesFromPoints(coordinates),
    //           })
    //     });
  }

  List<int> _selectedMarkers = [];

  void _updateMarkersList() {
    List<int> newSelectedMarkers = [];
    for (int i = 0; i < widget.tourInfo.locations.length; i++) {
      double distanceInMeters = Geolocator.distanceBetween(
        _currentP!.latitude,
        _currentP!.longitude,
        widget.tourInfo.locations[i].latlng[0],
        widget.tourInfo.locations[i].latlng[1],
      );
      if (distanceInMeters < widget.tourInfo.locations[i].distance_radius) {
        print(
            'Bravo! Odabrani marker: $i je dovoljno blizu: $distanceInMeters / ${widget.tourInfo.locations[i].distance_radius}');
        newSelectedMarkers.add(i);
      } else {
        print(
            'Odabrani marker: $i nije dovoljno blizu: $distanceInMeters / ${widget.tourInfo.locations[i].distance_radius}');
      }
    }
    setState(() {
      _selectedMarkers = newSelectedMarkers;
      print('ovo je _selectedMarkers: $_selectedMarkers');
    });
  }

  Future<void> _updateDistance(LatLng point, desiredLocation) async {
    if (_currentP != null) {
      double distanceInMeters = await Geolocator.distanceBetween(
        _currentP!.latitude,
        _currentP!.longitude,
        point.latitude,
        point.longitude,
      );
      setState(() {
        _distanceInMeters = distanceInMeters;
        _showFullBottomNavBar =
            distanceInMeters < widget.tourInfo.locations[0].distance_radius;
        if (_showFullBottomNavBar) {
          _description = desiredLocation.description;
          print('Dugačak Opis: $_description');
        } else {
          _description = desiredLocation.short_description +
              '... Opširnije kada se približite mestu ...';
          print('Kratak Opis: $_description');
        }
        print('Razdaljina u metrima: $_distanceInMeters m');
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    print(widget.tourInfo);
    return Scaffold(
        appBar: AppBar(
          title: Text(widget.tourInfo.name),
        ),
        endDrawer: const SidebarMenu(),
        body: Stack(children: [
          _currentP == null
              ? const Center(child: Text('Loading...'))
              : GoogleMap(
                  onMapCreated: ((GoogleMapController controller) =>
                      _mapController.complete(controller)),
                  initialCameraPosition: const CameraPosition(
                    target: _pKratovo,
                    zoom: 18,
                  ),
                  markers: {
                    ...List.generate(
                      widget.tourInfo.locations.length,
                      (index) => Marker(
                        markerId: MarkerId('location$index'),
                        icon: BitmapDescriptor.defaultMarkerWithHue(
                          BitmapDescriptor.hueAzure,
                        ),
                        infoWindow: InfoWindow(
                          title: widget.tourInfo.locations[index].name,
                          snippet: widget
                              .tourInfo.locations[index].short_description,
                        ),
                        position: LatLng(
                          widget.tourInfo.locations[index].latlng[0],
                          widget.tourInfo.locations[index].latlng[1],
                        ),
                        onTap: () => _onMarkerTapped(LatLng(
                            widget.tourInfo.locations[index].latlng[0],
                            widget.tourInfo.locations[index].latlng[1])),
                      ),
                    ).toSet(),
                    ...List.generate(
                      widget.tourInfo.restStops.length,
                      (index) => Marker(
                        markerId: MarkerId('restStop$index'),
                        icon: BitmapDescriptor.defaultMarkerWithHue(
                          BitmapDescriptor.hueMagenta,
                        ),
                        infoWindow: InfoWindow(
                          title: widget.tourInfo.restStops[index].name,
                          snippet: widget.tourInfo.restStops[index].description,
                        ),
                        position: LatLng(
                          widget.tourInfo.restStops[index].latlng[0],
                          widget.tourInfo.restStops[index].latlng[1],
                        ),
                        onTap: () => _onMarkerTapped(LatLng(
                            widget.tourInfo.restStops[index].latlng[0],
                            widget.tourInfo.restStops[index].latlng[1])),
                      ),
                    ).toSet(),
                    Marker(
                      markerId: const MarkerId('currentPosition'),
                      icon: BitmapDescriptor.defaultMarkerWithHue(
                        BitmapDescriptor.hueViolet,
                      ),
                      position: _currentP!,
                    ),
                  },
                  polylines: Set<Polyline>.of(polylines.values),
                  onCameraMove: (position) {
                    _followUserLocation = false; // Disable camera follow
                  },
                ),
          IgnorePointer(
            ignoring: true,
            child: GestureDetector(
              onTap: () {
                if (_selectedMarkerIndex != null) {
                  setState(() {
                    _selectedMarkerIndex = null;
                    print(
                        'ovo bi trebalo da potvrdi da je deselektovan marker!!');
                  });
                } else {
                  print(
                      'nema selektovanog markera ili ti ne radi kod kako treba!');
                }
              },
              child: Container(
                color: Colors.transparent,
                width: double.infinity,
                height: double.infinity,
              ),
            ),
          ),
        ]),
        bottomNavigationBar: Visibility(
          visible: _selectedMarkers.isNotEmpty,
          child: BottomAppBar(
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: _selectedMarkers.map((index) {
                  return Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 8.0),
                    child: FloatingActionButton.extended(
                      onPressed: () => _showExpandedText(context, index),
                      label: Text(widget.tourInfo.locations[index].name),
                      icon: const Icon(Icons.location_on),
                    ),
                  );
                }).toList(),
              ),
            ),
          ),
        ));

    // bottomNavigationBar: Visibility(
    //   visible: _selectedMarkers.isNotEmpty,
    //   child: BottomAppBar(
    //     child: Row(
    //       mainAxisAlignment: MainAxisAlignment.spaceEvenly,
    //       children: _selectedMarkers.map((index) {
    //         return FloatingActionButton.extended(
    //           onPressed: () => _showExpandedText(context, index),
    //           label: Text(widget.tourInfo.locations[index].name),
    //           icon: const Icon(Icons.location_on),
    //         );
    //       }).toList(),
    //     ),
    //   ),
    // ));
  }

  Future<void> _cameraToPosition(LatLng pos) async {
    if (!_followUserLocation) return; // Prevent camera from following
    final GoogleMapController controller = await _mapController.future;
    CameraPosition newCameraPosition = CameraPosition(target: pos, zoom: 18);
    await controller
        .animateCamera(CameraUpdate.newCameraPosition(newCameraPosition));
  }

  Future<void> getLocationUpdates() async {
    bool serviceEnabled;
    location_package.PermissionStatus permissionGranted;

    serviceEnabled = await _locationController.serviceEnabled();
    if (!serviceEnabled) {
      serviceEnabled = await _locationController.requestService();
      if (!serviceEnabled) return;
    }

    permissionGranted = await _locationController.hasPermission();
    if (permissionGranted == location_package.PermissionStatus.denied) {
      permissionGranted = await _locationController.requestPermission();
      if (permissionGranted != location_package.PermissionStatus.granted) {
        return;
      }
    }
    _locationController.onLocationChanged
        .listen((location_package.LocationData currentLocation) {
      if (currentLocation.latitude != null &&
          currentLocation.longitude != null) {
        setState(() {
          _currentP =
              LatLng(currentLocation.latitude!, currentLocation.longitude!);
          if (_followUserLocation) {
            _cameraToPosition(_currentP!);
          }
        });
        _updateMarkersList();
        print('izvršio se _updateMarkersList');
      }
    });
  }

  Future<void> _onMarkerTapped(LatLng? destination) async {
    if (_currentP == null || destination == null) return;
    List<LatLng> polylineCoordinates = await getPolylinePoints(destination);
    generatePolylinesFromPoints(polylineCoordinates);
  }

  Future<List<LatLng>> getPolylinePoints(LatLng destination) async {
    List<LatLng> polylineCoordinates = [];
    PolylinePoints polylinePoints = PolylinePoints();
    PolylineResult result = await polylinePoints.getRouteBetweenCoordinates(
      GOOGLE_MAPS_API_KEY,
      PointLatLng(_currentP!.latitude, _currentP!.longitude),
      PointLatLng(destination.latitude, destination.longitude),
      travelMode: TravelMode.walking,
    );
    if (result.points.isNotEmpty) {
      result.points.forEach((PointLatLng point) {
        polylineCoordinates.add(LatLng(point.latitude, point.longitude));
      });
    } else {
      print(result.errorMessage);
    }
    return polylineCoordinates;
  }

  void generatePolylinesFromPoints(List<LatLng> poilylineCoordinates) async {
    PolylineId id = PolylineId('poly');
    Polyline polyline = Polyline(
        polylineId: id,
        color: Colors.blue,
        points: poilylineCoordinates,
        width: 8);
    setState(() {
      polylines[id] = polyline;
    });
  }

  void _showExpandedText(BuildContext context, int index) {
    var location = widget.tourInfo.locations[index];
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return Dialog(
          backgroundColor: Colors.transparent,
          child: Container(
            height: MediaQuery.of(context).size.height * 0.85,
            padding: EdgeInsets.all(16.0),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.85),
              borderRadius: BorderRadius.circular(10.0),
            ),
            child: Column(
              children: [
                // Header (Slajder slika i Naslov)
                Column(
                  children: [
                    // Slajder slika
                    Container(
                        decoration: const BoxDecoration(
                          gradient: LinearGradient(
                            begin: Alignment.topCenter,
                            end: Alignment.bottomCenter,
                            colors: [
                              Color(0xFFCCEAF4),
                              Color(0xFFFFFFFF),
                            ],
                          ),
                        ),
                        padding: const EdgeInsets.only(
                          top: 0.0, // Padding za vrh
                          left: 0.0, // Padding za levo
                          right: 0.0, // Padding za desno
                          bottom: 0.0, // Padding za dno
                        ),
                        child: SizedBox(
                          height: 200, // Postavite odgovarajuću visinu za slike
                          child: PageView.builder(
                            itemCount: location.pictures.length,
                            itemBuilder: (context, index) {
                              return ClipRRect(
                                borderRadius: BorderRadius.circular(
                                    0.0), // Postavite stepen zaobljenosti ivica
                                child: Image.network(
                                  location.pictures[index],
                                  fit: BoxFit.cover,
                                ),
                              );
                            },
                          ),
                        )),
                    SizedBox(height: 16.0),
                    // Naslov
                    Text(
                      location.name,
                      style: TextStyle(
                        fontSize: 24.0,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
                SizedBox(height: 8.0),
                // Skrolabilan opis
                Expanded(
                  child: SingleChildScrollView(
                    child: Text(
                      location.description,
                      style: TextStyle(
                        fontSize: 16.0,
                      ),
                    ),
                  ),
                ),
                SizedBox(height: 16.0),
                // Footer (Audio kontrolni dugmići i dugme za zatvaranje)
                Align(
                  alignment: Alignment.bottomCenter,
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      IconButton(
                        icon: Icon(Icons.play_arrow),
                        onPressed: () {
                          // Logika za puštanje audio zapisa
                        },
                      ),
                      IconButton(
                        icon: Icon(Icons.pause),
                        onPressed: () {
                          // Logika za pauziranje audio zapisa
                        },
                      ),
                      IconButton(
                        icon: Icon(Icons.stop),
                        onPressed: () {
                          // Logika za zaustavljanje audio zapisa
                        },
                      ),
                      ElevatedButton(
                        onPressed: () {
                          Navigator.of(context).pop();
                        },
                        child: Text(LocaleData.button_close.getString(context)),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }
}
