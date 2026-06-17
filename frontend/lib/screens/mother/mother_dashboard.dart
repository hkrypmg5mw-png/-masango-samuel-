import 'package:flutter/material.dart';
import 'package:flutter_neumorphic_plus/flutter_neumorphic.dart';
import '../../core/theme.dart';
import '../../widgets/dashboard_card.dart';

class MotherDashboard extends StatelessWidget {
  const MotherDashboard({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: NeumorphicAppBar(
        title: const Text("MCH-FUS Mother Dashboard"),
        backgroundColor: AppColors.backgroundPrimary,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            const DashboardCard(
              title: "Pregnancy Progress",
              content: "Week 28 of 40\nEDD: 15 Oct 2024",
              color: AppColors.medicalBlue,
            ),
            const SizedBox(height: 16),
            const DashboardCard(
              title: "Upcoming Appointment",
              content: "ANC Visit\nTomorrow at 09:00 AM",
              color: AppColors.warningAmber,
            ),
            const SizedBox(height: 16),
            const DashboardCard(
              title: "Child Vaccination",
              content: "BCG Vaccine\nDue in 5 days",
              color: AppColors.medicalGreen,
            ),
            const SizedBox(height: 24),
            Align(
              alignment: Alignment.bottomRight,
              child: NeumorphicFloatingActionButton(
                child: const Icon(Icons.smart_toy, color: Colors.white),
                style: const NeumorphicStyle(
                  color: AppColors.aiPurple,
                  boxShape: NeumorphicBoxShape.circle(),
                ),
                onPressed: () {
                  // Open AI Chat
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
