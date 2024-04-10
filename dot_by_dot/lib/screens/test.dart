import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class TestPage extends StatefulWidget {
  const TestPage({super.key});

  @override
  _TestPageState createState() => _TestPageState();
}

class _TestPageState extends State<TestPage> {
  List<Map<String, dynamic>> _apiData = [];
  String _apiWelcomeMessage = '';

  Future<void> fetchData() async {
    final response =
        //     await http.get(Uri.parse('http://127.0.0.1:5000/api/data'));
        await http.get(Uri.parse('http://localhost:5000/api/data'));

    if (response.statusCode == 200) {
      print('flask je vratio kod 200');
      final Map<String, dynamic> data = json.decode(response.body);
      setState(() {
        _apiData = List.from(data['data']);
        _apiWelcomeMessage = data['message'];
      });
    } else {
      throw Exception('Failed to load data');
    }
  }

  @override
  void initState() {
    super.initState();
    fetchData();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('Test FLASK API Page'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(_apiWelcomeMessage),
            const SizedBox(height: 20),
            DataTable(
              headingRowColor: MaterialStateColor.resolveWith(
                (states) => Colors.green,
              ),
              columns: const [
                DataColumn(label: Text('Akcija')),
                DataColumn(label: Text('Ime')),
                DataColumn(label: Text('Prezime')),
                DataColumn(
                  label: Text('Datum rođenja'),
                  numeric:
                      true, // Postavite numeric na true za centralno orijentisanu kolonu
                ),
              ],
              rows: [
                for (var item in _apiData)
                  DataRow(cells: [
                    DataCell(
                      ElevatedButton(
                        onPressed: () {
                          // Dodajte svoju logiku za uređivanje ovdje
                          _showModalDialog(context);
                          // Možete, na primjer, otvoriti dijalog za uređivanje podataka
                          print('Edit: ${item['name']}');
                        },
                        child: const Text('Edit'),
                      ),
                    ),
                    DataCell(Text(item['name'])),
                    DataCell(Text(item['surname'])),
                    DataCell(Text(item['date_of_birth'])),
                  ])
              ],
              //   DataRow(cells: [
              //     DataCell(Text('Marko')),
              //     DataCell(Text('Perić')),
              //     DataCell(Text('25')),
              //   ]),
              //   DataRow(cells: [
              //     DataCell(Text('Ana')),
              //     DataCell(Text('Ivić')),
              //     DataCell(Text('20')),
              //   ]),
              //   DataRow(cells: [
              //     DataCell(Text('Ivan')),
              //     DataCell(Text('Marković')),
              //     DataCell(Text('30')),
              //   ]),
              // ],
            ),
          ],
        ),
      ),
    );
  }
}

void _showModalDialog(BuildContext context) {
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: const Text('Modalni Dijalog'),
        content: const Text('Ovo je sadržaj modala.'),
        actions: <Widget>[
          TextButton(
            onPressed: () {
              Navigator.of(context).pop();
            },
            child: const Text('Zatvori'),
          ),
        ],
      );
    },
  );
}
