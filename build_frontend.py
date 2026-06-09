import os

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip())

write('frontend/lib/core/constants.dart', """
import 'package:flutter/material.dart';
class AppColors {
  static const Color backgroundPrimary = Color(0xFF0F172A);
  static const Color backgroundSecondary = Color(0xFF111827);
  static const Color cardBackground = Color(0xFF1E293B);
  static const Color surface = Color(0xFF1A2234);
  static const Color medicalBlue = Color(0xFF3B82F6);
  static const Color healthcareGreen = Color(0xFF10B981);
  static const Color warningAmber = Color(0xFFF59E0B);
  static const Color emergencyRed = Color(0xFFEF4444);
  static const Color aiPurple = Color(0xFF8B5CF6);
  static const Color textPrimary = Colors.white;
  static const Color textSecondary = Colors.grey;
}
class ApiConstants {
  static const String baseUrl = 'http://10.0.2.2:8000/api';
}
""")

write('frontend/lib/core/theme.dart', """
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'constants.dart';
class AppTheme {
  static ThemeData darkTheme = ThemeData(
    brightness: Brightness.dark,
    primaryColor: AppColors.medicalBlue,
    scaffoldBackgroundColor: AppColors.backgroundPrimary,
    textTheme: GoogleFonts.poppinsTextTheme(ThemeData.dark().textTheme),
  );
}
""")

write('frontend/lib/services/api_service.dart', """
import 'package:dio/dio.dart';
import '../core/constants.dart';
class ApiService {
  final Dio _dio = Dio(BaseOptions(baseUrl: ApiConstants.baseUrl));
  Future<Response> login(String username, String password) async {
    return await _dio.post('/auth/login/', data: {'username': username, 'password': password});
  }
}
""")

write('frontend/lib/providers/auth_provider.dart', """
import 'package:flutter/material.dart';
import '../services/api_service.dart';
class AuthProvider with ChangeNotifier {
  final ApiService _apiService = ApiService();
  String? _token;
  String? _role;
  String? get role => _role;
  bool get isAuthenticated => _token != null;
  Future<bool> login(String username, String password) async {
    try {
      final response = await _apiService.login(username, password);
      _token = response.data['access'];
      _role = response.data['user']['role'];
      notifyListeners();
      return true;
    } catch (e) { return false; }
  }
}
""")

write('frontend/lib/screens/auth/login_screen.dart', """
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../providers/auth_provider.dart';
import '../mother/mother_dashboard.dart';
import '../nurse/nurse_dashboard.dart';

class LoginScreen extends StatelessWidget {
  const LoginScreen({super.key});
  @override
  Widget build(BuildContext context) {
    final emailController = TextEditingController();
    final passwordController = TextEditingController();
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(32.0),
        child: Column(
          children: [
            TextField(controller: emailController, decoration: const InputDecoration(labelText: 'Email')),
            TextField(controller: passwordController, decoration: const InputDecoration(labelText: 'Password')),
            ElevatedButton(onPressed: () async {
              final success = await context.read<AuthProvider>().login(emailController.text, passwordController.text);
              if (success) {
                final role = context.read<AuthProvider>().role;
                Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => role == 'MOTHER' ? const MotherDashboard() : const NurseDashboard()));
              }
            }, child: const Text('Login'))
          ],
        ),
      ),
    );
  }
}
""")

write('frontend/lib/screens/mother/mother_dashboard.dart', """
import 'package:flutter/material.dart';
class MotherDashboard extends StatelessWidget {
  const MotherDashboard({super.key});
  @override
  Widget build(BuildContext context) => const Scaffold(body: Center(child: Text('Mother Dashboard')));
}
""")

write('frontend/lib/screens/nurse/nurse_dashboard.dart', """
import 'package:flutter/material.dart';
class NurseDashboard extends StatelessWidget {
  const NurseDashboard({super.key});
  @override
  Widget build(BuildContext context) => const Scaffold(body: Center(child: Text('Nurse Dashboard')));
}
""")

write('frontend/lib/screens/doctor/doctor_dashboard.dart', "import 'package:flutter/material.dart';\\nclass DoctorDashboard extends StatelessWidget { const DoctorDashboard({super.key}); @override Widget build(BuildContext context) => const Scaffold(body: Center(child: Text('Doctor Dashboard'))); }")
write('frontend/lib/screens/chw/chw_dashboard.dart', "import 'package:flutter/material.dart';\\nclass CHWDashboard extends StatelessWidget { const CHWDashboard({super.key}); @override Widget build(BuildContext context) => const Scaffold(body: Center(child: Text('CHW Dashboard'))); }")
write('frontend/lib/screens/admin/admin_dashboard.dart', "import 'package:flutter/material.dart';\\nclass AdminDashboard extends StatelessWidget { const AdminDashboard({super.key}); @override Widget build(BuildContext context) => const Scaffold(body: Center(child: Text('Admin Dashboard'))); }")

write('frontend/lib/main.dart', """
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'core/theme.dart';
import 'providers/auth_provider.dart';
import 'screens/auth/login_screen.dart';
void main() => runApp(MultiProvider(providers: [ChangeNotifierProvider(create: (_) => AuthProvider())], child: const MaterialApp(home: LoginScreen())));
""")
