import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

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
        title: const Text('Početna'),
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
                  '/images/city.jpg'), // Zamenite sa putanjom do vaše slike

              const SizedBox(height: 20), // Dodaje razmak

              // Naslov grada
              const Text(
                'Vučje',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),

              const SizedBox(height: 10), // Dodaje razmak

              // Kratak opis
              const Text(
                'Vučje je gradsko naselje u okrugu Leskovca sa oko 2.865 stanovnika prema popisu iz 2011. Do 1965. bilo je sedište opštine Vučje koju su činila mnoga naseljena mesta. Nalazi se oko 17 km jugozapadno od Leskovca i geografski je centar područja Porečje, kroz koje protiče reka Vučjanka. Ima dom zdravlja, policijsku stanicu, fudbalski klub FK Vučje, osnovnu i srednju školu. Stanovništvo je pretežno srpsko.',
                maxLines: 7, // Ograničava broj linija za kratki opis
                overflow: TextOverflow.ellipsis, // Dodaje elipsu (...)
              ),

              const SizedBox(height: 20), // Dodaje razmak

              // Dugme za proširen tekst (floating action button)
              FloatingActionButton.extended(
                onPressed: () => _showExpandedText(context),
                label: const Text('Opširnije'),
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
                    label: const Text('Pešačka tura'),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _navigateToCyclingTourInfo(context),
                    icon: const Icon(Icons.directions_bike),
                    label: const Text('Biciklistička tura'),
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
        title: const Text('Opširnije o mestu Vučje'),
        content: const SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                '''Vučje je gradsko naseljeno mesto grada Leskovca u Jablaničkom okrugu. Prema popisu iz 2011. bilo je 2.865 stanovnika.

Do 1965. godine je ovo naselje bilo sedište opštine Vučje, koju su činila naseljena mesta: Barje, Beli Potok, Brza, Bukova Glava, Bunuša (od koje su nastala današnja samostalna naseljena mesta Bunuški Čifluk, Gornja Bunuša i Donja Bunuša), Crcavac, Čukljenik, Drvodelja, Gagince, Gorina, Gornja Jajina, Igrište, Kaluđerce, Kukulovce, Melovo, Miroševce, Nakrivanj, Oruglica, Palikuća, Presečina, Radonjica (tada pod zvaničnim nazivom Radonjice), Ravni Del, Slavujevce, Strojkovce, Šainovac, Todorovce, Veliko Trnjane, Vina, Vučje i Žabljane. Posle ukidanja opštine područje bivše opštine je u celini ušlo u sastav opštine Leskovac.

Geografija
Nalazi se približno 17 km jugozapadno od grada Leskovca i geografski je centar područja Porečje. Kroz Vučje protiče reka Vučjanka po kojoj je mesto dobilo ime. Na reci Vučjanki, nekoliko kilometara iznad Vučja, nalazi se hidrocentrala iz 1903. godine koja još uvek radi. U blizini Vučja nalazio se srednjovekovni Zelen-grad. Nedaleko od Vučja nalaze se i ostaci Skobaljić grada.

Vučje ima dom zdravlja, policijsku stanicu, fudbalski klub FK Vučje itd. Ima osnovnu školu „Bora Stanković“ i srednju školu „Svetozar Krstić Toza“. Ovo mesto je i kulturno središte kraja, a u njega dolaze mladi iz okolnih sela da se zabavljaju i druže.

Demografija
U naselju Vučje živi 2649 punoletnih stanovnika, a prosečna starost stanovništva iznosi 41,3 godina (40,2 kod muškaraca i 42,3 kod žena). U naselju ima 1049 domaćinstava, a prosečan broj članova po domaćinstvu je 3,11.

Ovo naselje je velikim delom naseljeno Srbima (prema popisu iz 2002. godine).''',
                textAlign: TextAlign.justify,
              ),
            ],
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Zatvori'),
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
