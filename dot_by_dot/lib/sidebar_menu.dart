import 'package:flutter/material.dart';

final GlobalKey<ScaffoldState> scaffoldKey = GlobalKey<ScaffoldState>();

// List<String> languages = ['Srpski', 'Engleski'];
// String selectedLanguage = 'Srpski'; // Inicijalno izabrani jezik

class SidebarMenu extends StatelessWidget {
  final String selectedLanguage;
  final Function(String?)?
      onLanguageSelected; // Define the onLanguageSelected parameter

  const SidebarMenu(
      {Key? key, this.selectedLanguage = 'en', this.onLanguageSelected})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: <Widget>[
          const DrawerHeader(
            decoration: BoxDecoration(
              // color: Colors.blue,
              image: DecorationImage(
                image: AssetImage('assets/images/city.jpg'),
                fit: BoxFit.cover,
              ),
            ),
            child: Text(
              'MENI',
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
    );
  }
}
