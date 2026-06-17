import 'package:flutter/material.dart';
import 'package:flutter_neumorphic_plus/flutter_neumorphic.dart';
import 'package:provider/provider.dart';
import '../../core/theme.dart';
import '../../providers/auth_provider.dart';
import '../mother/mother_dashboard.dart';
import '../nurse/nurse_dashboard.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(
              "MCH-FUS",
              style: Theme.of(context).textTheme.headlineLarge?.copyWith(
                color: AppColors.medicalBlue,
                fontSize: 32,
              ),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 48),
            Neumorphic(
              style: NeumorphicStyle(
                depth: -8,
                boxShape: NeumorphicBoxShape.roundRect(BorderRadius.circular(12)),
                color: AppColors.backgroundSecondary,
              ),
              padding: const EdgeInsets.symmetric(horizontal: 16),
              child: TextField(
                controller: _emailController,
                decoration: const InputDecoration(
                  hintText: "Email or Phone",
                  border: InputBorder.none,
                ),
              ),
            ),
            const SizedBox(height: 20),
            Neumorphic(
              style: NeumorphicStyle(
                depth: -8,
                boxShape: NeumorphicBoxShape.roundRect(BorderRadius.circular(12)),
                color: AppColors.backgroundSecondary,
              ),
              padding: const EdgeInsets.symmetric(horizontal: 16),
              child: TextField(
                controller: _passwordController,
                obscureText: true,
                decoration: const InputDecoration(
                  hintText: "Password",
                  border: InputBorder.none,
                ),
              ),
            ),
            const SizedBox(height: 40),
            NeumorphicButton(
              onPressed: () async {
                final auth = Provider.of<AuthProvider>(context, listen: false);
                final success = await auth.login(_emailController.text, _passwordController.text);
                if (success) {
                  if (mounted) {
                    if (auth.role == 'MOTHER') {
                      Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => const MotherDashboard()));
                    } else if (auth.role == 'NURSE') {
                      Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => const NurseDashboard()));
                    }
                  }
                } else {
                  if (mounted) {
                    ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text("Login Failed")));
                  }
                }
              },
              style: NeumorphicStyle(
                shape: NeumorphicShape.flat,
                boxShape: NeumorphicBoxShape.roundRect(BorderRadius.circular(12)),
                color: AppColors.medicalBlue,
              ),
              child: const Text(
                "Login",
                textAlign: TextAlign.center,
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
