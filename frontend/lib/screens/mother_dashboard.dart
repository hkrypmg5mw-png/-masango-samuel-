import 'package:flutter/material.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import 'sos_screen.dart';

class MotherDashboard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;
    return Scaffold(
      appBar: AppBar(title: Text(l10n.dashboard)),
      body: GridView.count(
        crossAxisCount: 2,
        padding: EdgeInsets.all(16),
        children: [
          _buildCard(context, l10n.pregnancyTracker, Icons.pregnant_woman, Colors.pink, () {}),
          _buildCard(context, l10n.vaccinations, Icons.medical_services, Colors.blue, () {}),
          _buildCard(context, l10n.appointments, Icons.calendar_today, Colors.teal, () {}),
          _buildCard(context, "Health Tips", Icons.lightbulb, Colors.orange, () {}),
          _buildCard(context, "Growth Charts", Icons.show_chart, Colors.green, () {}),
          _buildCard(context, l10n.emergencySos, Icons.emergency, Colors.red, () {
            Navigator.of(context).push(MaterialPageRoute(builder: (_) => SOSScreen()));
          }),
        ],
      ),
    );
  }

  Widget _buildCard(BuildContext context, String title, IconData icon, Color color, VoidCallback onTap) {
    return Card(
      elevation: 4,
      child: InkWell(
        onTap: onTap,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, size: 48, color: color),
            SizedBox(height: 8),
            Text(title, textAlign: TextAlign.center, style: TextStyle(fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}
