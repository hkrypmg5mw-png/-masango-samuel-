import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';

class GrowthChart extends StatelessWidget {
  final List<FlSpot> weightData;
  final String title;

  GrowthChart({required this.weightData, required this.title});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 300,
      padding: EdgeInsets.all(16),
      child: LineChart(
        LineChartData(
          titlesData: FlTitlesData(show: true),
          borderData: FlBorderData(show: true),
          lineBarsData: [
            LineChartBarData(
              spots: weightData,
              isCurved: true,
              color: Colors.blue,
              barWidth: 4,
              dotData: FlDotData(show: true),
            ),
          ],
        ),
      ),
    );
  }
}
