import 'package:flutter/material.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'chat_screen.dart';

class MotherDashboard extends StatefulWidget {
  const MotherDashboard({super.key});

  @override
  State<MotherDashboard> createState() => _MotherDashboardState();
}

class _MotherDashboardState extends State<MotherDashboard> {
  int _currentIndex = 0;

  final List<Widget> _screens = [
    const HomeTab(),
    const Center(child: Text('Appointments')),
    const ChatScreen(),
    const Center(child: Text('Profile')),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) => setState(() => _currentIndex = index),
        type: BottomNavigationBarType.fixed,
        selectedItemColor: const Color(0xFF009688),
        unselectedItemColor: Colors.grey,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.dashboard), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.event), label: 'Events'),
          BottomNavigationBarItem(icon: Icon(Icons.chat), label: 'AI'),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Profile'),
        ],
      ),
    );
  }
}

class HomeTab extends StatelessWidget {
  const HomeTab({super.key});

  @override
  Widget build(BuildContext context) {
    return CustomScrollView(
      slivers: [
        SliverAppBar(
          expandedHeight: 120,
          floating: false,
          pinned: true,
          flexibleSpace: FlexibleSpaceBar(
            title: const Text('Hello, Marie!', style: TextStyle(color: Colors.white)),
            background: Container(color: const Color(0xFF009688)),
          ),
        ),
        SliverToBoxAdapter(
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                _buildPregnancyProgress(context),
                const SizedBox(height: 24),
                const Text('Quick Actions', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                const SizedBox(height: 16),
                _buildQuickActions(),
                const SizedBox(height: 24),
                const Text('Upcoming Visits', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                const SizedBox(height: 16),
                _buildUpcomingVisits(),
              ],
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildPregnancyProgress(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                const Text('Pregnancy Progress', style: TextStyle(fontWeight: FontWeight.bold)),
                Text('Week 24', style: TextStyle(color: Theme.of(context).primaryColor)),
              ],
            ),
            const SizedBox(height: 16),
            LinearProgressIndicator(
              value: 24 / 40,
              minHeight: 10,
              borderRadius: BorderRadius.circular(5),
              backgroundColor: Colors.teal.shade50,
              color: const Color(0xFF009688),
            ),
            const SizedBox(height: 12),
            const Text('16 weeks to go!', style: TextStyle(color: Colors.grey)),
          ],
        ),
      ),
    ).animate().fadeIn().slideY(begin: 0.1);
  }

  Widget _buildQuickActions() {
    return GridView.count(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      crossAxisCount: 3,
      mainAxisSpacing: 12,
      crossAxisSpacing: 12,
      children: [
        _actionItem(Icons.emergency, 'SOS', Colors.red),
        _actionItem(Icons.vaccines, 'Vaccines', Colors.orange),
        _actionItem(Icons.monitor_weight, 'Growth', Colors.blue),
      ],
    );
  }

  Widget _actionItem(IconData icon, String label, Color color) {
    return InkWell(
      onTap: () {},
      child: Container(
        decoration: BoxDecoration(
          color: color.withOpacity(0.1),
          borderRadius: BorderRadius.circular(16),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, color: color, size: 32),
            const SizedBox(height: 8),
            Text(label, style: TextStyle(color: color, fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }

  Widget _buildUpcomingVisits() {
    return Column(
      children: [
        ListTile(
          leading: const CircleAvatar(backgroundColor: Color(0xFF009688), child: Icon(Icons.medical_services, color: Colors.white)),
          title: const Text('Prenatal Checkup'),
          subtitle: const Text('Nov 25, 2024 - District Hospital'),
          trailing: const Icon(Icons.chevron_right),
          tileColor: Colors.white,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        ),
      ],
    );
  }
}
