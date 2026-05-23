import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/auth_provider.dart';

class MotherDashboard extends StatelessWidget {
  const MotherDashboard({super.key});

  @override
  Widget build(BuildContext context) {
    final user = Provider.of<AuthProvider>(context).user;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Mother Dashboard'),
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () => Provider.of<AuthProvider>(context, listen: false).logout(),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Welcome, ${user?.username}!', style: Theme.of(context).textTheme.headlineSmall),
            const SizedBox(height: 20),
            _buildStatCard(context, 'Pregnancy Progress', '24 Weeks', Icons.pregnant_woman, Colors.pink),
            const SizedBox(height: 10),
            _buildStatCard(context, 'Next Appointment', 'Oct 25, 2023', Icons.calendar_today, Colors.blue),
            const SizedBox(height: 20),
            const Text('Quick Actions', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            const SizedBox(height: 10),
            GridView.count(
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              crossAxisCount: 2,
              crossAxisSpacing: 10,
              mainAxisSpacing: 10,
              children: [
                _buildActionCard(context, 'Vaccinations', Icons.medical_services, Colors.green),
                _buildActionCard(context, 'Growth Chart', Icons.show_chart, Colors.orange),
                _buildActionCard(context, 'Health Tips', Icons.lightbulb, Colors.amber),
                _buildActionCard(context, 'SOS/Emergency', Icons.emergency, Colors.red),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildStatCard(BuildContext context, String title, String value, IconData icon, Color color) {
    return Card(
      child: ListTile(
        leading: Icon(icon, color: color, size: 40),
        title: Text(title),
        trailing: Text(value, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
      ),
    );
  }

  Widget _buildActionCard(BuildContext context, String title, IconData icon, Color color) {
    return InkWell(
      onTap: () {},
      child: Card(
        color: color.withValues(alpha: 0.1),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, color: color, size: 40),
            const SizedBox(height: 10),
            Text(title, style: TextStyle(color: color, fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}
