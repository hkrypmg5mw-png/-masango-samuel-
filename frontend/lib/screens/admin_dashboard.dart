import 'package:flutter/material.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

class AdminDashboard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;
    return Scaffold(
      appBar: AppBar(title: Text("Admin Dashboard")),
      body: ListView(
        children: [
          ListTile(
            leading: Icon(Icons.manage_accounts),
            title: Text("User Management"),
            onTap: () {},
          ),
          ListTile(
            leading: Icon(Icons.business),
            title: Text("Facility Management"),
            onTap: () {},
          ),
          ListTile(
            leading: Icon(Icons.analytics),
            title: Text("Health Statistics"),
            onTap: () {},
          ),
          ListTile(
            leading: Icon(Icons.monitor_heart),
            title: Text("System Monitoring"),
            onTap: () {},
          ),
        ],
      ),
    );
  }
}
