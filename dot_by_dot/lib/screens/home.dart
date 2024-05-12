import 'package:dot_by_dot/localization/locales.dart';
import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:flutter_localization/flutter_localization.dart';

// import 'tour_info_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});
  final CameraPosition _initialCameraPosition = const CameraPosition(
    target: LatLng(44.79717, 20.47694),
  );

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
            LocaleData.home_title.getString(context)), //! prepravi na početna
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            children: [
              // Logo ili ikona
              const Icon(Icons.location_city), // Zamenite sa svojim logom

              const SizedBox(height: 20), // Dodaje razmak

              // Slika grada
              Image.asset(
                  'assets/images/city.jpg'), // Zamenite sa putanjom do vaše slike

              const SizedBox(height: 20), // Dodaje razmak

              // Naslov grada
              const Text(
                'Vučje',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),

              const SizedBox(height: 10), // Dodaje razmak

              // Kratak opis
              Text(
                LocaleData.home_vucje_about.getString(context),
                maxLines: 7, // Ograničava broj linija za kratki opis
                overflow: TextOverflow.ellipsis, // Dodaje elipsu (...)
              ),

              const SizedBox(height: 20), // Dodaje razmak

              // Dugme za proširen tekst (floating action button)
              FloatingActionButton.extended(
                onPressed: () => _showExpandedText(context),
                label: Text(LocaleData.main_more.getString(context)),
                icon: const Icon(Icons.info_rounded),
              ),

              const SizedBox(height: 20), // Dodaje razmak

              // Dugmad za ture
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _navigateToWalkingTourInfo(context),
                    icon: const Icon(Icons.directions_walk),
                    label:
                        Text(LocaleData.main_walking_tour.getString(context)),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _navigateToCyclingTourInfo(context),
                    icon: const Icon(Icons.directions_bike),
                    label:
                        Text(LocaleData.main_cycling_tour.getString(context)),
                  ),
                ],
              ),
              const SizedBox(height: 20), // Dodaje razmak

              // GoogleMap(
              //     onMapCreated: _onMapCreated,
              //     initialCameraPosition: _initialCameraPosition
              //     ),
            ],
          ),
        ),
      ),
    );
  }

  // Funkcija za prikazivanje proširenog teksta (implementirajte po potrebi)
  void _showExpandedText(BuildContext context) {
    // Modal, dno sheet ili neki drugi vidžet za prikazivanje proširenog teksta
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(LocaleData.home_vucje_about_title.getString(context)),
        content: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                LocaleData.home_vucje_about_extended.getString(context),
                textAlign: TextAlign.justify,
              ),
            ],
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: Text(LocaleData.home_vucje_about_close.getString(context)),
          ),
        ],
      ),
    );
  }

  // Funkcija za prelazak na stranicu sa informacijama o turi (implementirajte po potrebi)
  void _navigateToWalkingTourInfo(BuildContext context) {
    // Navigacija ka novoj stranici za prikaz informacija o turi
    // Predajte 'tourType' ('walking' ili 'cycling') na sledeću stranicu
    Navigator.pushNamed(context, '/walkingTourInfo');
  }

  void _navigateToCyclingTourInfo(BuildContext context) {
    // Navigacija ka novoj stranici za prikaz informacija o turi
    // Predajte 'tourType' ('walking' ili 'cycling') na sledeću stranicu
    Navigator.pushNamed(context, '/cyclingTourInfo');
  }
}
