import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'core/theme/app_theme.dart';
import 'providers/auth_provider.dart';
import 'screens/login_screen.dart';
import 'screens/mother_dashboard.dart';
import 'screens/health_worker_dashboard.dart';

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthProvider()),
      ],
      child: const MCHApp(),
    ),
  );
}

class MCHApp extends StatelessWidget {
  const MCHApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MCH Follow-Up',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.light,
      localizationsDelegates: const [
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: const [
        Locale('en', ''),
        Locale('fr', ''),
      ],
      home: Consumer<AuthProvider>(
        builder: (context, auth, _) {
          if (!auth.isAuthenticated) return const LoginScreen();

          if (auth.role == 'MOTHER') {
            return const MotherDashboard();
          } else {
            return const HealthWorkerDashboard();
          }
        },
      ),
    );
  }
}
