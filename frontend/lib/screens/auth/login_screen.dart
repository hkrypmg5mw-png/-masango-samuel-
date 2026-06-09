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