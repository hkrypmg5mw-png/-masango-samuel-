import 'package:flutter/material.dart';

class HealthWorkerDashboard extends StatelessWidget {
  const HealthWorkerDashboard({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Health Worker Dashboard')),
      body: ListView(
        padding: const EdgeInsets.all(16.0),
        children: [
          const Text('Active Patients', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          const SizedBox(height: 10),
          _buildPatientTile('Marie Claire', 'High Risk', Colors.red),
          _buildPatientTile('Florence N.', 'Medium Risk', Colors.orange),
          _buildPatientTile('Sita Diallo', 'Low Risk', Colors.green),
          const SizedBox(height: 20),
          ElevatedButton.icon(
            onPressed: () {},
            icon: const Icon(Icons.person_add),
            label: const Text('Register New Mother'),
          ),
          ElevatedButton.icon(
            onPressed: () {},
            icon: const Icon(Icons.event),
            label: const Text('Schedule Field Visit'),
          ),
        ],
      ),
    );
  }

  Widget _buildPatientTile(String name, String risk, Color color) {
    return Card(
      child: ListTile(
        title: Text(name),
        subtitle: Text('Risk Level: $risk'),
        trailing: Container(
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
          decoration: BoxDecoration(color: color, borderRadius: BorderRadius.circular(10)),
          child: const Text('View Details', style: TextStyle(color: Colors.white, fontSize: 12)),
        ),
      ),
    );
  }
}
