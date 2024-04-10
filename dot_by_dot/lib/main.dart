import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
// import 'screens/home_screen.dart';
import 'screens/home.dart';
import 'screens/tour_info_screen.dart';
import 'tour_info.dart';
import 'sidebar_menu.dart';

void main() {
  runApp(const MyApp());
}

Future<Map<String, dynamic>> fetchTourData(String tourType) async {
  final response =
      await http.get(Uri.parse('http://localhost:5000/api/tours/$tourType'));
  if (response.statusCode == 200) {
    return json.decode(response.body);
  } else {
    throw Exception('Failed to load tour data');
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Flutter Demo',
        theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF07710A)),
          useMaterial3: true,
        ),
        home: Builder(
          builder: (context) => Scaffold(
            key: scaffoldKey,
            appBar: AppBar(
              title: const Text('Turistički vodič'),
            ),
            endDrawer: const SidebarMenu(),
            body: const HomeScreen(),
          ),
        ),
        routes: {
          '/walkingTourInfo': (context) =>
              buildTourInfoScreen(context, 'walking'),
          '/cyclingTourInfo': (context) =>
              buildTourInfoScreen(context, 'cycling'),
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
        ); // Prikaži loader dok se podaci učitavaju
      } else if (snapshot.hasError) {
        return Text('Error: ${snapshot.error}');
      } else {
        final tourInfo = TourInfo.fromJson(snapshot.data!);
        return TourInfoScreen(tourInfo: tourInfo);
      }
    },
  );
}
