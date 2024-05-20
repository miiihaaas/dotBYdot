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
      //appBar: AppBar(
       // title: Text(
            // LocaleData.home_title.getString(context)), //! prepravi na početna
      //),
      
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(0.0),
          child: Column(
            children: [
              // Logo ili ikona
          //    const Icon(Icons.location_city), // Zamenite sa svojim logom
              
              Container(
                padding: const EdgeInsets.all(0.0),
                child: Image.asset('assets/images/prelaz-top-3.png'),
              ),
              Container(
                color: Color(0xFF0094C9), // Postavlja plavu pozadinsku boju
                padding: const EdgeInsets.all(20.0),
                child: SizedBox(
                  height: 200,
                  child: PageView(
                    children: [
                      Image.asset('assets/images/vucje-logobeo-cir.png'),
                    ],
                  ),
                ),
              ),

              Container(
                padding: const EdgeInsets.all(0.0),
                child: Image.asset('assets/images/prelaz.png'),
              ),

              // const SizedBox(height: 20), // Dodaje razmak

              // Slika grada
              Container(
                decoration: BoxDecoration(
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
                  top: 40.0,  // Padding za vrh
                  left: 20.0, // Padding za levo
                  right: 20.0, // Padding za desno
                  bottom: 20.0, // Padding za dno
                ),
                child:SizedBox(
                  height: 200, // Postavite odgovarajuću visinu za slike
                  child: PageView(
                    children: [
                      ClipRRect(
                        borderRadius: BorderRadius.circular(16.0), // Postavite stepen zaobljenosti ivica
                        child: Image.asset('assets/images/city.jpg', fit: BoxFit.cover),
                      ),
                      ClipRRect(
                        borderRadius: BorderRadius.circular(16.0), // Postavite stepen zaobljenosti ivica
                        child: Image.asset('assets/images/city_2.jpg', fit: BoxFit.cover),
                      ),
                    ],
                  ),
                ),
              ), 


              const SizedBox(height: 20), // Dodaje razmak

              // Naslov grada
              const Text(
                'Vučje',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, fontFamily: "RussoOne"),
              ),

              const SizedBox(height: 10), // Dodaje razmak

              // Kratak opis
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20.0),
                child: Text(
                  LocaleData.home_vucje_about.getString(context),
                  maxLines: 7, // Ograničava broj linija za kratki opis
                  overflow: TextOverflow.ellipsis, // Dodaje elipsu (...)
                ),
              ),

              const SizedBox(height: 20), // Dodaje razmak

              // Dugme za proširen tekst (floating action button)
              Container(
                width: double.infinity,
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [
                      Color(0xFFFFFFFF),
                      Color(0xFFCCEAF4),
                    ],
                  ),
                ),
                padding: const EdgeInsets.all(20.0),
                child: ElevatedButton.icon(
                  onPressed: () => _showExpandedText(context),
                  icon: const Icon(Icons.info_rounded),
                  label: Text(LocaleData.main_more.getString(context)),
                  style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.resolveWith<Color>(
                      (states) {
                        return const Color(0xFFEBF2F5); // Promenite boju dugmeta
                      },
                    ),
                    foregroundColor: MaterialStateProperty.resolveWith<Color>(
                      (states) {
                        return const Color(0xFF0094C9); // Promenite boju teksta
                      },
                    ),
                  ),
                ),
              ),

              // const SizedBox(height: 20), // Dodaje razmak

              Container(
                padding: const EdgeInsets.all(0.0),
                child: Image.asset('assets/images/prelaz-bottom-1.png'),
              ),
              // Dugmad za ture
              Container(
                color: Color(0xFF0094C9),
                padding: const EdgeInsets.all(20.0),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    ElevatedButton.icon(
                      onPressed: () => _navigateToWalkingTourInfo(context),
                      icon: Icon(Icons.directions_walk, color: Color(0xFF0094C9)),
                      label: Text(
                        LocaleData.main_walking_tour.getString(context),
                        style: const TextStyle(color: Color(0xFF0094C9)),
                      ),
                    ),
                    ElevatedButton.icon(
                      onPressed: () => _navigateToCyclingTourInfo(context),
                      icon: const Icon(Icons.directions_bike, color: Color(0xFF0094C9)),
                      label: Text(
                        LocaleData.main_cycling_tour.getString(context),
                        style: const TextStyle(color: Color(0xFF0094C9)),
                      ),
                    ),
                  ],
                ),
              ),
              // const SizedBox(height: 20), // Dodaje razmak

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
