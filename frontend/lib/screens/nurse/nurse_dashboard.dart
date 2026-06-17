import 'package:flutter/material.dart';
import 'package:flutter_neumorphic_plus/flutter_neumorphic.dart';
import '../../core/theme.dart';
import '../../widgets/dashboard_card.dart';

class NurseDashboard extends StatelessWidget {
  const NurseDashboard({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: NeumorphicAppBar(
        title: const Text("Nurse Dashboard"),
        backgroundColor: AppColors.backgroundPrimary,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Row(
              children: const [
                Expanded(
                  child: DashboardCard(
                    title: "Total Mothers",
                    content: "124",
                    color: AppColors.medicalBlue,
                  ),
                ),
                SizedBox(width: 16),
                Expanded(
                  child: DashboardCard(
                    title: "Visits Today",
                    content: "12",
                    color: AppColors.medicalGreen,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),
            const DashboardCard(
              title: "High Risk Alerts",
              content: "3 Patients require immediate follow-up",
              color: AppColors.emergencyRed,
            ),
            const SizedBox(height: 16),
            Neumorphic(
              style: NeumorphicStyle(
                depth: 8,
                boxShape: NeumorphicBoxShape.roundRect(BorderRadius.circular(24)),
                color: AppColors.cardBackground,
              ),
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text("Patient Monitoring Panel", style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18)),
                  const SizedBox(height: 12),
                  _buildPatientRow("Marie Ngo", "Week 32", "High Risk"),
                  _buildPatientRow("Claire Abena", "Week 14", "Normal"),
                  _buildPatientRow("Fatima Moussa", "Week 24", "Normal"),
                ],
              ),
            )
          ],
        ),
      ),
    );
  }

  Widget _buildPatientRow(String name, String stage, String status) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(name),
          Text(stage),
          Text(status, style: TextStyle(color: status == "High Risk" ? AppColors.emergencyRed : AppColors.medicalGreen)),
        ],
      ),
    );
  }
}
