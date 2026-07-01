import 'package:flutter/material.dart';

class HealthWorkerDashboard extends StatelessWidget {
  const HealthWorkerDashboard({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Facility Dashboard')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('Patient Overview', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            const SizedBox(height: 16),
            _buildStatCards(),
            const SizedBox(height: 24),
            const Text('Recent Patient Registrations', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            const SizedBox(height: 16),
            Expanded(
              child: ListView.builder(
                itemCount: 5,
                itemBuilder: (context, index) {
                  return Card(
                    margin: const EdgeInsets.only(bottom: 12),
                    child: ListTile(
                      leading: const CircleAvatar(child: Icon(Icons.person)),
                      title: Text('Patient ${index + 1}'),
                      subtitle: const Text('Last Visit: 2 days ago'),
                      trailing: const Badge(label: Text('Low Risk'), backgroundColor: Colors.green),
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {},
        label: const Text('Register Patient'),
        icon: const Icon(Icons.add),
        backgroundColor: const Color(0xFF009688),
      ),
    );
  }

  Widget _buildStatCards() {
    return Row(
      children: [
        Expanded(child: _statCard('Total Mothers', '124', Colors.teal)),
        const SizedBox(width: 12),
        Expanded(child: _statCard('High Risk', '8', Colors.red)),
        const SizedBox(width: 12),
        Expanded(child: _statCard('Scheduled', '15', Colors.blue)),
      ],
    );
  }

  Widget _statCard(String label, String count, Color color) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: color.withOpacity(0.1),
        borderRadius: BorderRadius.circular(16),
      ),
      child: Column(
        children: [
          Text(count, style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: color)),
          const SizedBox(height: 4),
          Text(label, style: TextStyle(fontSize: 12, color: color)),
        ],
      ),
    );
  }
}
