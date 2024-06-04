import 'package:dot_by_dot/localization/locales.dart';
import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:flutter_localization/flutter_localization.dart';

class ExpandableTextWidget extends StatefulWidget {
  final String initialText;
  final String expandedText;

  ExpandableTextWidget({required this.initialText, required this.expandedText});

  @override
  _ExpandableTextWidgetState createState() => _ExpandableTextWidgetState();
}

class _ExpandableTextWidgetState extends State<ExpandableTextWidget> {
  bool _isExpanded = false;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          _isExpanded ? widget.expandedText : widget.initialText,
          maxLines: _isExpanded ? null : 5,
          overflow: TextOverflow.visible,
        ),
        SizedBox(height: 10),
        if (widget.expandedText.isNotEmpty)
          TextButton(
            onPressed: () {
              setState(() {
                _isExpanded = !_isExpanded;
              });
            },
            child: Text(
              _isExpanded
                  ? LocaleData.home_show_less.getString(context)
                  : LocaleData.home_show_more.getString(context),
              style: TextStyle(color: Colors.blue),
            ),
          ),
      ],
    );
  }
}

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

              //Container(
              //  padding: const EdgeInsets.all(0.0),
              //  child: Image.asset('assets/images/prelaz-top-3.png'),
              //),
              //Container(
              //color: Color(0xFF0094C9), // Postavlja plavu pozadinsku boju
              //decoration: const BoxDecoration(
              //  gradient: LinearGradient(
              //    begin: Alignment.topCenter,
              //    end: Alignment.bottomCenter,
              //    colors: [
              //      Color(0xFF00ace9),
              //      Color(0xFF0094c9),
              //    ],
              //  ),
              //),
              //padding: const EdgeInsets.all(20.0),
              FittedBox(
                child: Image.asset('assets/images/kratovo-header.png'),
                fit: BoxFit.fill,
              ),
              //),

              Container(
                padding: const EdgeInsets.only(
                  top: 0.0, // Padding za vrh
                  left: 20.0, // Padding za levo
                  right: 80.0, // Padding za desno
                  bottom: 20.0, // Padding za dno
                ),
                decoration: BoxDecoration(
                  color: Color(0xFFfdc70c), // dodaj pozadinsku boju #fdc70c
                ),
                child: Image.asset('assets/images/kratovo-slogan-en.png'),
              ),

              // const SizedBox(height: 20), // Dodaje razmak

              // Slika grada
              Container(
                color: Color(0xFFfdc70c),
                padding: const EdgeInsets.only(
                  top: 40.0, // Padding za vrh
                  left: 0.0, // Padding za levo
                  right: 0.0, // Padding za desno
                  bottom: 20.0, // Padding za dno
                ),
                child: AspectRatio(
                  aspectRatio: 1 / 1,
                  child: PageView(
                    children: [
                      Image.asset(
                        'assets/images/kratovo-mozaik.jpg',
                        fit: BoxFit.cover,
                      ),
                      Image.asset(
                        'assets/images/kratovo-city.jpg',
                        fit: BoxFit.cover,
                      ),
                    ],
                  ),
                ),
              ),

              Container(
                padding: const EdgeInsets.all(0.0),
                child: Image.asset('assets/images/kratovo-zut-prelaz.png'),
              ),

              const SizedBox(height: 20), // Dodaje razmak

              // Naslov grada
              const Text(
                'Kratovo',
                //style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, fontFamily: "RussoOne"),
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),

              //const SizedBox(height: 10), // Dodaje razmak

              Container(
                decoration: BoxDecoration(
                  image: DecorationImage(
                    image: AssetImage(
                        'assets/images/prelaz-siv-gradient-half.jpg'),
                    fit: BoxFit.none,
                    alignment: Alignment.center,
                  ),
                ),
                padding: const EdgeInsets.only(
                    top: 40, bottom: 80, left: 20, right: 20),
                child: Container(
                  decoration: BoxDecoration(
                    color: Colors
                        .white, // Dodajte bilo koju dekoraciju ili stil koji želite za novi Container
                    borderRadius: BorderRadius.circular(
                        20.0), // Primer sa zaobljenim uglovima
                    boxShadow: [
                      BoxShadow(
                        color: Colors.grey
                            .withOpacity(0.2), // Boja senke sa prozirnošću
                        spreadRadius: 5, // Širina senke
                        blurRadius: 10, // Zamućenje senke
                        offset: Offset(0, 0), // Pomeranje senke (x, y)
                      ),
                    ],
                  ),
                  padding: const EdgeInsets.all(20.0),
                  child: ExpandableTextWidget(
                    initialText: LocaleData.home_kratovo_about_extended
                        .getString(context),
                    expandedText: LocaleData.home_kratovo_about_extended
                        .getString(context),
                  ),
                ),
              ),

              Container(
                padding: const EdgeInsets.all(0.0),
                child: Image.asset('assets/images/kratovo-zut-prelaz-flip.png'),
              ),

              // Dugmad za ture
              /*  Container(
                color: Color(0xFFfdc70d),
                padding: const EdgeInsets.only(
                    top: 20, bottom: 60, left: 20, right: 20),
                width:
                    double.infinity, // Da Container zauzme celu širinu ekrana
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    Stack(
                      alignment: Alignment.center,
                      children: [
                        ElevatedButton(
                          onPressed: () => _navigateToWalking1(context),
                          style: ElevatedButton.styleFrom(
                            backgroundColor: Color(0xFFFFFFFF),
                            shadowColor: Colors.black,
                            elevation: 5,
                            shape: CircleBorder(side: BorderSide(width: 100)),
                          ),
                          child: Image.asset(
                            'assets/images/walk-tour.png',
                          ),
                        ),
                        Positioned(
                          top: 50, // prilagodite potrebnu visinu
                          child: Text(
                            LocaleData.home_walking_1.getString(context),
                            style: TextStyle(color: Color(0xFF333333)),
                          ),
                        ),
                      ],
                    ),
                    Stack(
                      alignment: Alignment.center,
                      children: [
                        ElevatedButton(
                          onPressed: () => _navigateToWalking2(context),
                          style: ElevatedButton.styleFrom(
                            backgroundColor: Color(0xFFFFFFFF),
                            shadowColor: Colors.black,
                            elevation: 5,
                            shape: CircleBorder(side: BorderSide(width: 100)),
                          ),
                          child: Image.asset(
                            'assets/images/walk-cardio-tour.png',
                          ),
                        ),
                        Positioned(
                          top: 50, // prilagodite potrebnu visinu
                          child: Text(
                            LocaleData.home_walking_2.getString(context),
                            style: TextStyle(color: Color(0xFF333333)),
                          ),
                        ),
                      ],
                    ),
                    Stack(
                      alignment: Alignment.center,
                      children: [
                        ElevatedButton(
                          onPressed: () => _navigateToCycling1(context),
                          style: ElevatedButton.styleFrom(
                            backgroundColor: Color(0xFFFFFFFF),
                            shadowColor: Colors.black,
                            elevation: 5,
                            shape: CircleBorder(side: BorderSide(width: 100)),
                          ),
                          child: Image.asset(
                            'assets/images/bike-tour.png',
                          ),
                        ),
                        Positioned(
                          top: 50, // prilagodite potrebnu visinu
                          child: Text(
                            LocaleData.home_cycling_1.getString(context),
                            style: TextStyle(color: Color(0xFF333333)),
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ), */

              Container(
                color: Color(0xFFfdc70d),
                padding: const EdgeInsets.only(
                    top: 20, bottom: 60, left: 20, right: 20),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          ElevatedButton(
                            onPressed: () => _navigateToWalking1(context),
                            style: ElevatedButton.styleFrom(
                              backgroundColor: Color(0xFFFFFFFF),
                              padding: EdgeInsets.all(0.0),
                              shadowColor: Colors.black,
                              elevation: 5,
                              shape: CircleBorder(side: BorderSide(width: 100)),
                            ),
                            child: Image.asset(
                              'assets/images/walk-tour.png',
                            ),
                          ),
                          SizedBox(
                              height: 10), // Razmak između dugmeta i teksta
                          Text(
                            LocaleData.home_walking_1.getString(context),
                            style: TextStyle(
                              color: Color(0xFF056839),
                              fontSize: 16.0,
                              fontWeight: FontWeight.bold,
                            ),
                            textAlign: TextAlign.center,
                          ),
                        ],
                      ),
                    ),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          ElevatedButton(
                            onPressed: () => _navigateToWalking2(context),
                            style: ElevatedButton.styleFrom(
                              backgroundColor: Color(0xFFFFFFFF),
                              padding: EdgeInsets.all(0.0),
                              shadowColor: Colors.black,
                              elevation: 5,
                              shape: CircleBorder(side: BorderSide(width: 100)),
                            ),
                            child: Image.asset(
                              'assets/images/walk-cardio-tour.png',
                            ),
                          ),
                          SizedBox(
                              height: 10), // Razmak između dugmeta i teksta
                          Text(
                            LocaleData.home_walking_2.getString(context),
                            style: TextStyle(
                              color: Color(0xFF056839),
                              fontSize: 16.0,
                              fontWeight: FontWeight.bold,
                            ),
                            textAlign: TextAlign.center,
                          ),
                        ],
                      ),
                    ),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          ElevatedButton(
                            onPressed: () => _navigateToCycling1(context),
                            style: ElevatedButton.styleFrom(
                              backgroundColor: Color(0xFFFFFFFF),
                              padding: EdgeInsets.all(0.0),
                              shadowColor: Colors.black,
                              elevation: 5,
                              shape: CircleBorder(side: BorderSide(width: 100)),
                            ),
                            child: Image.asset(
                              'assets/images/bike-tour.png',
                            ),
                          ),
                          SizedBox(
                              height: 10), // Razmak između dugmeta i teksta
                          Text(
                            LocaleData.home_cycling_1.getString(context),
                            style: TextStyle(
                              color: Color(0xFF056839),
                              fontSize: 16.0,
                              fontWeight: FontWeight.bold,
                            ),
                            textAlign: TextAlign.center,
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),

              Container(
                width: double.infinity,
                color: const Color(0xFFfdb00b),
                padding: const EdgeInsets.all(20.0),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment
                      .spaceBetween, // Raspoređivanje elemenata između
                  children: [
                    Align(
                      alignment: Alignment.centerLeft,
                      child: SizedBox(
                        width: 60,
                        child: Image.asset('assets/images/eu-flag.png',
                            fit: BoxFit.contain),
                      ),
                    ),
                    Align(
                      alignment: Alignment.centerLeft,
                      child: SizedBox(
                        width: 280,
                        child: Text(
                          // 'Ovu aplikaciju finansira Evropska unija',
                          LocaleData.home_vucje_eu_text_1.getString(context),
                          style: const TextStyle(
                              fontSize: 14, color: Colors.black87),
                          textAlign: TextAlign.left,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              Container(
                width: double.infinity,
                color: const Color(0xFF056839),
                padding: const EdgeInsets.all(20.0),
                child: Text(
                  // 'Ova aplikacija je finansirana od strane Evropske unije. Sadržaj je isključiva odgovornost Srednje škole „Svetozar Krstić – Toza“ iz Vučja, SOU „Mitko Pendžukliski“ iz Kratova i Udruženja "Limitless" iz Beograda, i ne odražava nužno stavove Evropske unije',
                  LocaleData.home_vucje_eu_text_2.getString(context),
                  style: const TextStyle(fontSize: 12, color: Colors.white),
                  textAlign: TextAlign.center,
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
                LocaleData.home_kratovo_about_extended.getString(context),
                textAlign: TextAlign.justify,
              ),
            ],
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: Text(LocaleData.button_close.getString(context)),
          ),
        ],
      ),
    );
  }

  // Funkcija za prelazak na stranicu sa informacijama o turi (implementirajte po potrebi)
  void _navigateToWalking1(BuildContext context) {
    // Navigacija ka novoj stranici za prikaz informacija o turi
    // Predajte 'tourType' ('walking' ili 'cycling') na sledeću stranicu
    Navigator.pushNamed(context, '/walking_1');
  }

  void _navigateToWalking2(BuildContext context) {
    // Navigacija ka novoj stranici za prikaz informacija o turi
    // Predajte 'tourType' ('walking' ili 'cycling') na sledeću stranicu
    Navigator.pushNamed(context, '/walking_2');
  }

  void _navigateToCycling1(BuildContext context) {
    // Navigacija ka novoj stranici za prikaz informacija o turi
    // Predajte 'tourType' ('walking' ili 'cycling') na sledeću stranicu
    Navigator.pushNamed(context, '/cycling_1');
  }
}
