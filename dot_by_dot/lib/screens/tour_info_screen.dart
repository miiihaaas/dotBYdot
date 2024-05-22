import 'package:dot_by_dot/localization/locales.dart';
import 'package:dot_by_dot/screens/map_screen.dart';
import 'package:flutter/material.dart';
import 'package:flutter_localization/flutter_localization.dart'; // Replace with your project name
import 'package:dot_by_dot/sidebar_menu.dart';
import 'package:dot_by_dot/tour_info.dart';

class TourInfoScreen extends StatelessWidget {
  final TourInfo tourInfo;

  const TourInfoScreen({super.key, required this.tourInfo});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: PreferredSize(
        preferredSize: Size.fromHeight(kToolbarHeight),
        child: AppBar(
          flexibleSpace: Container(
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                colors: [
                  Color(0xFFffffff),
                  Color(0xFFcceaf4)
                ], // Promenite boje po potrebi
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
              ),
            ),
          ),
          title: Text(tourInfo.name),
        ),
      ),
      endDrawer: const SidebarMenu(),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.only(
              top: 0.0, bottom: 80.0, left: 0.0, right: 00),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Image.asset('assets/images/prelaz-top-3.png'),
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(20.0),
                color: Color(0xFF0094C9),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      '${tourInfo.type}',
                      style: const TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                          color: Color(0xFFffffff)),
                    ),
                    const SizedBox(height: 10),
                    Text(
                      // 'Dužina rute:
                      context.formatString(
                          LocaleData.tour_info_screen_description_1,
                          [tourInfo.routeLenght]),
                      style: const TextStyle(color: Color(0xFFffffff)),
                    ),
                    Text(
                      // 'Trajanje:
                      context.formatString(
                          LocaleData.tour_info_screen_description_2,
                          [tourInfo.duration]),
                      style: const TextStyle(color: Color(0xFFffffff)),
                    ),
                    Text(
                      // 'Visinska razlika:
                      context.formatString(
                          LocaleData.tour_info_screen_description_3,
                          [tourInfo.elevationGain.toStringAsFixed(0)]),
                      style: const TextStyle(color: Color(0xFFffffff)),
                    ),
                    Text(
                      // 'Nivo težine: ${tourInfo.difficultyLevel}',
                      context.formatString(
                          LocaleData.tour_info_screen_description_4,
                          [tourInfo.difficultyLevel]),
                      style: const TextStyle(color: Color(0xFFffffff)),
                    ),
                    // Text(
                    //   'Broj lokacija: ${tourInfo.numberOfLocations}',
                    //   style: const TextStyle(color: Color(0xFFffffff)),
                    // ),
                  ],
                ),
              ),
              Container(
                padding: const EdgeInsets.all(0.0),
                child: Image.asset('assets/images/prelaz.png'),
              ),
              // Tabs
              DefaultTabController(
                length: 3,
                child: Container(
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
                  child: Column(
                    children: [
                      TabBar(
                        tabs: [
                          Tab(
                            child: Text(
                              // 'Lista lokacija',
                              LocaleData.tour_info_screen_tab_1
                                  .getString(context),
                              textAlign: TextAlign.center,
                            ),
                          ),
                          Tab(
                            child: Text(
                              // 'Pre nego što krenete',
                              LocaleData.tour_info_screen_tab_2
                                  .getString(context),
                              textAlign: TextAlign.center,
                            ),
                          ),
                          Tab(
                            child: Text(
                              // 'Mesta za predah',
                              LocaleData.tour_info_screen_tab_3
                                  .getString(context),
                              textAlign: TextAlign.center,
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 15),
                      SizedBox(
                        height:
                            MediaQuery.of(context).size.height * 0.42, // 100vh
                        child: TabBarView(
                          children: [
                            // List of locations
                            ListView.builder(
                              itemCount: tourInfo.locations.length,
                              itemBuilder: (context, index) {
                                final location = tourInfo.locations[index];
                                return ListTile(
                                  title: Text(location.name),
                                  subtitle: Text(location.short_description),
                                  trailing: Icon(
                                    location.visited
                                        ? Icons.check
                                        : Icons.place,
                                    color: location.visited
                                        ? Colors.green
                                        : Colors.grey,
                                  ),
                                );
                              },
                            ),

                            // Pre-tour information
                            ListView.builder(
                              itemCount: tourInfo.preTourInformation.length,
                              itemBuilder: (context, index) {
                                // return Text(tourInfo.preTourInformation[index]);
                                return ListTile(
                                  title:
                                      Text(tourInfo.preTourInformation[index]),
                                );
                              },
                            ),

                            // Rest stops
                            ListView.builder(
                              itemCount: tourInfo.restStops.length,
                              itemBuilder: (context, index) {
                                final restStop = tourInfo.restStops[index];
                                return ListTile(
                                  title: Text(restStop.name),
                                  subtitle: Text(restStop.description),
                                );
                              },
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              ),

              const SizedBox(height: 20),
            ],
          ),
        ),
      ),
      floatingActionButton: Padding(
        padding: const EdgeInsets.only(bottom: 10),
        child: FloatingActionButton.extended(
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) => MapScreen(tourInfo: tourInfo)),
            );
          },
          label: Text(
            // 'POKRENI TURU',
            LocaleData.tour_info_screen_start_tour.getString(context),
            style: TextStyle(color: Colors.white),
          ),
          backgroundColor: Color(0xFF0094C9),
        ),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
    );
  }
}
