// table_screen.dart
import 'package:flutter/material.dart';

class TablePage extends StatelessWidget {
  const TablePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('Prva Flutter aplikacija > Tabela'),
      ),
      body: SizedBox(
        width: double.infinity,
        child: DataTable(
          headingRowColor: MaterialStateColor.resolveWith(
            (states) => Colors.green,
          ),
          columns: const [
            DataColumn(label: Text('Ime')),
            DataColumn(label: Text('Prezime')),
            DataColumn(
              label: Text('Dob'),
              numeric: true, // Postavite numeric na true za centralno orijentisanu kolonu
            ),
          ],
          rows: const [
            DataRow(cells: [
              DataCell(Text('Marko')),
              DataCell(Text('Perić')),
              DataCell(Text('25')),
            ]),
            DataRow(cells: [
              DataCell(Text('Ana')),
              DataCell(Text('Ivić')),
              DataCell(Text('20')),
            ]),
            DataRow(cells: [
              DataCell(Text('Ivan')),
              DataCell(Text('Marković')),
              DataCell(Text('30')),
            ]),
          ],
        ),
      ),
    );
  }
}
