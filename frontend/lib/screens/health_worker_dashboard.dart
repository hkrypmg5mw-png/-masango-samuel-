import 'package:flutter/material.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import 'record_entry_screen.dart';

class HealthWorkerDashboard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;
    return Scaffold(
      appBar: AppBar(title: Text(l10n.dashboard)),
      body: ListView(
        children: [
          ListTile(
            leading: Icon(Icons.people),
            title: Text("Patient Records"),
            onTap: () {},
          ),
          ListTile(
            leading: Icon(Icons.add_task),
            title: Text("Record ANC Visit"),
            onTap: () {
              Navigator.of(context).push(MaterialPageRoute(builder: (_) => RecordEntryScreen(recordType: "ANC")));
            },
          ),
          ListTile(
            leading: Icon(Icons.vaccines),
            title: Text("Record Vaccination"),
            onTap: () {
              Navigator.of(context).push(MaterialPageRoute(builder: (_) => RecordEntryScreen(recordType: "Vaccination")));
            },
          ),
          ListTile(
            leading: Icon(Icons.warning, color: Colors.red),
            title: Text("High-Risk Alerts"),
            onTap: () {},
          ),
          ListTile(
            leading: Icon(Icons.sync),
            title: Text("Sync Data"),
            onTap: () {},
          ),
        ],
      ),
    );
  }
}
