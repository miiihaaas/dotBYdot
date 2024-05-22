import 'package:flutter/material.dart';

final GlobalKey<ScaffoldState> scaffoldKey = GlobalKey<ScaffoldState>();

// List<String> languages = ['Srpski', 'Engleski'];
// String selectedLanguage = 'Srpski'; // Inicijalno izabrani jezik

class SidebarMenu extends StatelessWidget {
  final String selectedLanguage;
  final Function(String?)?
      onLanguageSelected; // Define the onLanguageSelected parameter

  const SidebarMenu(
      {super.key, this.selectedLanguage = 'en', this.onLanguageSelected});

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: Container(
        padding: EdgeInsets.all(0.0),
        //margin: EdgeInsets.all(10.0),
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [
              Color(0xFFFFFFFF),
              Color(0xFFCCEAF4),
            ],
          ),
        ),
        child: ListView(
          padding: EdgeInsets.zero,
          children: <Widget>[
            const DrawerHeader(
              decoration: BoxDecoration(
                color: Color(0xFF0094C9),
                image: DecorationImage(
                  image: AssetImage('assets/images/talasi.png'),
                  fit: BoxFit.scaleDown,
                ),
              ),
              child: Text(
                '',
                style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            // ListTile(
            //   title: Text('NAZAD'),
            //   leading: Icon(Icons.arrow_back),
            //   onTap: () {
            //     Navigator.pop(context);
            //   },
            // ),
            ListTile(
              leading: const Icon(Icons.home),
              title: const Text('POČETNA'),
              onTap: () {
                Navigator.popUntil(context, ModalRoute.withName('/'));
              },
            ),
            ListTile(
              leading: const Icon(Icons.location_on),
              title: const Text('LISTA LOKALITETA'),
              onTap: () {
                Navigator.popAndPushNamed(context, '/listaLokaliteta');
              },
            ),
            ListTile(
              leading: const Icon(Icons.language),
              title: const Text('IZBOR JEZIKA: '),
              trailing: DropdownButton(
                value: selectedLanguage,
                items: const [
                  DropdownMenuItem(
                    value: 'sr',
                    child: Text('Srpski'),
                  ),
                  DropdownMenuItem(
                    value: 'en',
                    child: Text('English'),
                  )
                ],
                onChanged: onLanguageSelected, // Promenjeno ovde
              ),
            ),
          ],
        ),
      ),
    );
  }
}
