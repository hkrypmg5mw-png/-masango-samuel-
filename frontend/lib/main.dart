import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'providers/auth_provider.dart';
import 'screens/login_screen.dart';
import 'screens/register_screen.dart';
import 'screens/mother_dashboard.dart';
import 'screens/health_worker_dashboard.dart';
import 'screens/admin_dashboard.dart';

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
      title: 'MCH Follow-up',
      theme: ThemeData(
        primarySwatch: Colors.teal,
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.teal),
      ),
      home: Consumer<AuthProvider>(
        builder: (context, auth, _) {
          if (!auth.isAuthenticated) return const LoginScreen();
          if (auth.user?.role == 'MOTHER') return const MotherDashboard();
          if (auth.user?.role == 'ADMIN') return const AdminDashboard();
          return const HealthWorkerDashboard();
        },
      ),
      routes: {
        '/login': (context) => const LoginScreen(),
        '/register': (context) => const RegisterScreen(),
        '/home': (context) => const HomeWrapper(),
      },
    );
  }
}

class HomeWrapper extends StatelessWidget {
  const HomeWrapper({super.key});

  @override
  Widget build(BuildContext context) {
    final auth = Provider.of<AuthProvider>(context);
    if (auth.user?.role == 'MOTHER') return const MotherDashboard();
    if (auth.user?.role == 'ADMIN') return const AdminDashboard();
    return const HealthWorkerDashboard();
  }
}
