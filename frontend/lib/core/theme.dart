import 'package:flutter/material.dart';

class AppColors {
  static const Color backgroundPrimary = Color(0xFF0F172A);
  static const Color backgroundSecondary = Color(0xFF111827);
  static const Color cardBackground = Color(0xFF1E293B);
  static const Color surface = Color(0xFF1A2234);

  static const Color medicalBlue = Color(0xFF3B82F6);
  static const Color medicalGreen = Color(0xFF10B981);
  static const Color warningAmber = Color(0xFFF59E0B);
  static const Color emergencyRed = Color(0xFFEF4444);
  static const Color aiPurple = Color(0xFF8B5CF6);

  static const Color textPrimary = Colors.white;
  static const Color textSecondary = Colors.white70;
}

class AppTheme {
  static ThemeData get darkTheme {
    return ThemeData(
      brightness: Brightness.dark,
      primaryColor: AppColors.medicalBlue,
      scaffoldBackgroundColor: AppColors.backgroundPrimary,
      cardColor: AppColors.cardBackground,
      colorScheme: ColorScheme.dark(
        primary: AppColors.medicalBlue,
        secondary: AppColors.aiPurple,
        surface: AppColors.surface,
        error: AppColors.emergencyRed,
      ),
      textTheme: TextTheme(
        headlineLarge: TextStyle(color: AppColors.textPrimary, fontWeight: FontWeight.bold),
        bodyLarge: TextStyle(color: AppColors.textPrimary),
        bodyMedium: TextStyle(color: AppColors.textSecondary),
      ),
    );
  }
}
