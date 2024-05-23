import 'package:dot_by_dot/localization/locales.dart';
import 'package:dot_by_dot/tour_info.dart';
import 'package:dot_by_dot/sidebar_menu.dart';
import 'package:flutter/material.dart';
import 'package:flutter_localization/flutter_localization.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:geolocator/geolocator.dart'; // novo za tetiranje razdaljine između trenutne lokacije i lokacije na mapi
import 'package:location/location.dart' as location_package;
import 'dart:async';

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
  int? _selectedMarkerIdex;
  final location_package.Location _locationController =
      location_package.Location();

  final Completer<GoogleMapController> _mapController =
      Completer<GoogleMapController>();

  static const _pKratovo = LatLng(42.077990, 22.179178);
  LatLng? _currentP;

  @override
  void initState() {
    super.initState();
    getLocationUpdates();
  }

  List<int> _selectedMarkers = [];
  // Funkcija za ažuriranje liste odabranih markera
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
                  markers: Set<Marker>.from(
                    List.generate(
                      widget.tourInfo.locations.length,
                      (index) => Marker(
                        markerId: MarkerId('location$index'),
                        icon: BitmapDescriptor.defaultMarker,
                        infoWindow: InfoWindow(
                          title: widget.tourInfo.locations[index].name,
                          snippet: widget
                              .tourInfo.locations[index].short_description,
                        ),
                        position: LatLng(
                          widget.tourInfo.locations[index].latlng[0],
                          widget.tourInfo.locations[index].latlng[1],
                        ),
                        //? onTap: () {
                        //?   setState(() {
                        //?     _selectedMarkerIdex = index;
                        //?   });
                        //?   _updateDistance(
                        //?       LatLng(
                        //?           widget.tourInfo.locations[index].latlng[0],
                        //?           widget.tourInfo.locations[index].latlng[1]),
                        //?       widget.tourInfo.locations[index]);
                        //? }
                        // proslediti vrednost widget.tourInfo.locations[index].description u bottomNavigationBar
                      ),
                    ),
                  )..add(Marker(
                      markerId: const MarkerId('currentPosition'),
                      icon: BitmapDescriptor.defaultMarkerWithHue(
                          BitmapDescriptor.hueBlue),
                      position: _currentP!)),
                ),
          IgnorePointer(
            ignoring: true,
            child: GestureDetector(
              onTap: () {
                if (_selectedMarkerIdex != null) {
                  setState(() {
                    _selectedMarkerIdex = null;
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
        // footer na dnu stranice
        // bottomNavigationBar: BottomAppBar(
        //     color: Colors.red,
        //     child: _selectedMarkers.isNotEmpty
        //         ? Row(
        //             mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        //             children: _selectedMarkers.map((index) {
        //               return FloatingActionButton.extended(
        //                 onPressed: () => _showExpandedText(context, index),
        //                 label: Text(widget.tourInfo.locations[index].name),
        //                 icon: const Icon(Icons.location_on),
        //               );
        //             }).toList(),
        //           )
        //         : null));
        bottomNavigationBar: Visibility(
          visible: _selectedMarkers.isNotEmpty,
          child: BottomAppBar(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: _selectedMarkers.map((index) {
                return FloatingActionButton.extended(
                  onPressed: () => _showExpandedText(context, index),
                  label: Text(widget.tourInfo.locations[index].name),
                  icon: const Icon(Icons.location_on),
                );
              }).toList(),
            ),
          ),
        ));
  }

  //!

  //!
  Future<void> _cameraToPosition(LatLng pos) async {
    final GoogleMapController controller = await _mapController.future;
    CameraPosition newCameraPosition = CameraPosition(target: pos, zoom: 18);
    await controller
        .animateCamera(CameraUpdate.newCameraPosition(newCameraPosition));
  }

  Future<void> getLocationUpdates() async {
    bool serviceEnabled;
    location_package.PermissionStatus permissionGranted;

    serviceEnabled = await _locationController.serviceEnabled();
    if (serviceEnabled) {
      serviceEnabled = await _locationController.requestService();
    } else {
      return;
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
          _cameraToPosition(_currentP!);
        });
      }
      //! ovde dodati _updateDistance
      _updateMarkersList(); //!
      print('izvršio se _updateMarkersList');
    });
  }

  // Funkcija za prikazivanje proširenog teksta (implementirajte po potrebi)
  // void _showExpandedText(BuildContext context, int index) {
  //   var location = widget.tourInfo.locations[index];
  //   // Modal, dno sheet ili neki drugi vidžet za prikazivanje proširenog teksta
  //   showDialog(
  //     context: context,
  //     builder: (context) => AlertDialog(
  //       title: Text(location.name),
  //       content: SingleChildScrollView(
  //         child: Column(
  //           crossAxisAlignment: CrossAxisAlignment.start,
  //           children: [
  //             Text(
  //               location.description,
  //               textAlign: TextAlign.justify,
  //             ),
  //           ],
  //         ),
  //       ),
  //       actions: [
  //         TextButton(
  //           onPressed: () => Navigator.pop(context),
  //           child: const Text('Zatvori'),
  //         ),
  //       ],
  //     ),
  //   );
  // }
  void _showExpandedText(BuildContext context, int index) {
    var location = widget.tourInfo.locations[index];
    showDialog(
      context: context,
      builder: (context) => Dialog(
        backgroundColor: Colors.transparent, // Transparent background
        child: Container(
          width: MediaQuery.of(context).size.width * 0.9, // 90% screen width
          height: MediaQuery.of(context).size.height, // 100% screen height
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              Container(
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.85), // 30% transparency
                  borderRadius: BorderRadius.circular(5),
                ),
                padding: EdgeInsets.all(12),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.start,
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
                          top: 40.0, // Padding za vrh
                          left: 0.0, // Padding za levo
                          right: 0.0, // Padding za desno
                          bottom: 20.0, // Padding za dno
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
                    // Naslov
                    Text(
                      location.name,
                      style: const TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 8),
                    // Opis
                    SingleChildScrollView(
                      child: Text(
                        location.description,
                        textAlign: TextAlign.justify,
                      ),
                    ),
                    Align(
                      alignment: Alignment.bottomRight,
                      child: TextButton(
                        onPressed: () => Navigator.pop(context),
                        child: Text(LocaleData.button_close.getString(context)),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
