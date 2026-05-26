import 'package:flutter/material.dart';

class HealthWorkerDashboard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Health Worker Dashboard")),
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
            onTap: () {},
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
