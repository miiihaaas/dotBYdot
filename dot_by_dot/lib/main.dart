import 'package:dot_by_dot/localization/locales.dart';
import 'package:flutter/material.dart';
import 'package:flutter_localization/flutter_localization.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'screens/home.dart';
import 'screens/tour_info_screen.dart';
import 'tour_info.dart';
import 'sidebar_menu.dart';

void main() {
  runApp(const MyApp());
}

Future<Map<String, dynamic>> fetchTourData(String tourType) async {
  final response = await http
      .get(Uri.parse('https://popis.online/dotBYdot/api/tours/$tourType'));
  if (response.statusCode == 200) {
    return json.decode(response.body);
  } else {
    throw Exception('Failed to load tour data');
  }
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final FlutterLocalization localization = FlutterLocalization.instance;
  String selectedLanguage = 'en'; // Initial language selection

  @override
  void initState() {
    configureLocalization();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF0094C9)),
        useMaterial3: true,
      ),
      supportedLocales: localization.supportedLocales,
      localizationsDelegates: localization.localizationsDelegates,
      home: Builder(
        builder: (context) => Scaffold(
          appBar: PreferredSize(
            preferredSize: Size.fromHeight(kToolbarHeight),
            child: AppBar(
              flexibleSpace: Container(
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [Color(0xFFffffff), Color(0xFFcceaf4)], // Promenite boje po potrebi
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                  ),
                ),
              ),
              title: Text(
                LocaleData.main_title.getString(context),
              ),
              //backgroundColor: Colors.transparent, // Set to transparent to show gradient
            ),
          ),
          endDrawer: SidebarMenu(
            selectedLanguage: selectedLanguage,
            onLanguageSelected: _updateLanguage,
          ),
          body: const HomeScreen(),
        ),
      ),
      routes: {
        '/walkingTourInfo': (context) =>
            buildTourInfoScreen(context, 'walking'),
        '/cyclingTourInfo': (context) =>
            buildTourInfoScreen(context, 'cycling'),
      },
    );
  }

  void configureLocalization() {
    localization.init(
      mapLocales: LOCALES,
      initLanguageCode: selectedLanguage,
    );
    localization.onTranslatedLanguage = onTranslatedLanguage;
  }

  void onTranslatedLanguage(Locale? locale) {
    setState(() {});
  }

  void _updateLanguage(String? newLanguage) {
    setState(() {
      selectedLanguage =
          newLanguage ?? 'en'; // Set to 'en' if newLanguage is null
      localization.init(
          mapLocales: LOCALES, initLanguageCode: selectedLanguage);
    });
  }
}

Widget buildTourInfoScreen(BuildContext context, String tourType) {
  return FutureBuilder(
    future: fetchTourData(tourType),
    builder: (context, AsyncSnapshot<Map<String, dynamic>> snapshot) {
      if (snapshot.connectionState == ConnectionState.waiting) {
        return const Center(
          child: SizedBox(
            height: 50.0,
            width: 50.0,
            child: CircularProgressIndicator(),
          ),
        );
      } else if (snapshot.hasError) {
        return Text('Error: ${snapshot.error}');
      } else {
        try {
          final tourInfo = TourInfo.fromJson(snapshot.data!);
          return TourInfoScreen(tourInfo: tourInfo);
        } catch (e) {
          print('Error parsing data: $e');
          print('Raw data: ${snapshot.data}');
          return const Text('Error parsing data');
        }
      }
    },
  );
}
