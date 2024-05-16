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
      appBar: AppBar(
        title: Text(tourInfo.name),
      ),
      endDrawer: const SidebarMenu(),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Tour details
              Text(
                '${tourInfo.type} tura',
                style:
                    const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 10),
              Text(context.formatString(
                      LocaleData.tour_info_screen_description_1,
                      [tourInfo.duration.toStringAsFixed(1)])
                  // 'Trajanje: ${tourInfo.duration.toStringAsFixed(1)} sati',
                  ),
              Text(
                context.formatString(LocaleData.tour_info_screen_description_2,
                    [tourInfo.elevationGain.toStringAsFixed(0)]),
                // 'Ukupna visinska razlika: ${tourInfo.elevationGain.toStringAsFixed(0)} m',
              ),
              Text(
                'Preporučeni početni lokalitet: ${tourInfo.startingLocation}',
              ),
              Text(
                'Nivo težine: ${tourInfo.difficultyLevel}',
              ),
              Text(
                'Broj lokacija: ${tourInfo.numberOfLocations}',
              ),
              const SizedBox(height: 20),

              // Tabs
              DefaultTabController(
                length: 3,
                child: Column(
                  children: [
                    const TabBar(
                      tabs: [
                        Tab(text: 'Lista lokacija'),
                        Tab(text: 'Pre nego što krenete'),
                        Tab(text: 'Mesta za predah'),
                      ],
                    ),
                    const SizedBox(height: 15),
                    SizedBox(
                      height: 450, // Adjust height as needed
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
                                  location.visited ? Icons.check : Icons.place,
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
                              return Text(tourInfo.preTourInformation[index]);
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

              const SizedBox(height: 20),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(
                builder: (context) => MapScreen(tourInfo: tourInfo)),
          );
        },
        label: const Text('POKRENI TURU'),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
    );
  }
}
