import 'package:flutter/material.dart';
import 'login_screen.dart';
import 'test.dart';
import 'Table_screen.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;
  bool _isSwitched = false;
  double _sliderValue = 50.0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  void _navigateToLoginPage() {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => const LoginPage(),
      ),
    );
  }

  void _navigateToTestPage() {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => const TestPage(),
      ),
    );
  }

  void _navigateToTablePage() {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => const TablePage(),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text('Rajkula ima ovoliko godina:'),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // print('pritisnuto je dugme "login".');
                _navigateToLoginPage();
              },
              child: const Text('Login'),
            ),
            // Dodajte novo dugme za navigaciju ka TablePage
            ElevatedButton(
              onPressed: () {
                // print('pritisnuto je dugme za tabelu.');
                _navigateToTablePage();
              },
              child: const Text('Prikaži tabelu'),
            ),
            ElevatedButton(
              onPressed: () {
                // print('Pritisnuto je dugme za test.');
                _navigateToTestPage();
              },
              child: const Text('Test Page'),
            ),

            const SizedBox(height: 40),
            const Column(
              children: [
                Text("Text 1"),
                SizedBox(height: 10),
                Text("Text 2"),
                SizedBox(height: 10),
                Text("Text 3"),
                SizedBox(height: 10),
                Icon(
                  Icons.home,
                  color: Colors.green,
                  size: 128,
                ),
                SizedBox(height: 10),
              ],
            ),
            Switch(
              value: _isSwitched,
              activeColor: Colors.green,
              inactiveThumbColor: Colors.red,
              inactiveTrackColor: const Color.fromARGB(255, 218, 155, 150),
              onChanged: (bool value) {
                // print('promenjena vrednost je: $value.');
                setState(() {
                  _isSwitched = value;
                });
              },
            ),
            const SizedBox(height: 20),
            Text(
              'Switch je uključen: ${_isSwitched ? "Da" : "Ne"}',
            ),
            Slider(
              min: 0,
              max: 100,
              value: _sliderValue,
              onChanged: (double value) {
                // print('slider je sada na $value.');
                setState(() {
                  _sliderValue = value;
                });
              },
            )
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
