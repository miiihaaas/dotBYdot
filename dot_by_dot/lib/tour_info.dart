class TourInfo {
  final String name;
  final String type; // 'walking' or 'cycling'
  final double duration; // Time in hours
  final double elevationGain; // Difference in meters
  final String startingLocation;
  final String difficultyLevel;
  final int numberOfLocations;

  // Information for each tab
  final List<Location> locations;
  final List<String> preTourInformation;
  final List<RestStop> restStops;

  TourInfo({
    required this.name,
    required this.type,
    required this.duration,
    required this.elevationGain,
    required this.startingLocation,
    required this.difficultyLevel,
    required this.numberOfLocations,
    required this.locations,
    required this.preTourInformation,
    required this.restStops,
  });
  factory TourInfo.fromJson(Map<String, dynamic> json) {
    return TourInfo(
      name: json['name'],
      type: json['type'],
      duration: json['duration'],
      elevationGain: json['elevationGain'],
      startingLocation: json['startingLocation'],
      difficultyLevel: json['difficultyLevel'],
      numberOfLocations: json['numberOfLocations'],
      locations: (json['locations'] as List<dynamic>)
          .map((location) => Location.fromJson(location))
          .toList(),
      preTourInformation: List<String>.from(json['preTourInformation']),
      restStops: (json['restStops'] as List<dynamic>)
          .map((restStop) => RestStop.fromJson(restStop))
          .toList(),
    );
  }
}

class Location {
  final String name;
  final String description;
  final String short_description;
  final List<dynamic> latlng;
  bool visited; // Track if user visited this location

  Location({
    required this.name,
    required this.description,
    required this.short_description,
    required this.latlng,
    this.visited = false,
  });

  factory Location.fromJson(Map<String, dynamic> json) {
    return Location(
      name: json['name'],
      description: json['description'],
      short_description: json['short_description'],
      latlng: json['latlng'],
      visited: json['visited'] ?? false,
    );
  }
}

class RestStop {
  final String name;
  final String description;

  RestStop({
    required this.name,
    required this.description,
  });

  factory RestStop.fromJson(Map<String, dynamic> json) {
    return RestStop(
      name: json['name'],
      description: json['description'],
    );
  }
}
