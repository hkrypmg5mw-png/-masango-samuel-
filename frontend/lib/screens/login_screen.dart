import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import '../providers/auth_provider.dart';
import 'mother_dashboard.dart';
import 'health_worker_dashboard.dart';
import 'admin_dashboard.dart';

class LoginScreen extends StatelessWidget {
  final Function(bool) onLanguageToggle;
  LoginScreen({required this.onLanguageToggle});

  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;

    return Scaffold(
      appBar: AppBar(
        title: Text(l10n.appTitle),
        actions: [
          IconButton(
            icon: Icon(Icons.language),
            onPressed: () {
              onLanguageToggle(Localizations.localeOf(context).languageCode == 'en');
            },
          )
        ],
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: _usernameController,
              decoration: InputDecoration(labelText: l10n.username),
            ),
            TextField(
              controller: _passwordController,
              decoration: InputDecoration(labelText: l10n.password),
              obscureText: true,
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () async {
                bool success = await Provider.of<AuthProvider>(context, listen: false)
                    .login(_usernameController.text, _passwordController.text);
                if (success) {
                   String role = Provider.of<AuthProvider>(context, listen: false).role ?? 'MOTHER';
                   Widget targetDashboard;
                   if (role == 'ADMIN') {
                     targetDashboard = AdminDashboard();
                   } else if (role == 'MOTHER') {
                     targetDashboard = MotherDashboard();
                   } else {
                     targetDashboard = HealthWorkerDashboard();
                   }
                   Navigator.of(context).pushReplacement(
                     MaterialPageRoute(builder: (_) => targetDashboard)
                   );
                } else {
                  ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text("Login Failed")));
                }
              },
              child: Text(l10n.login),
            ),
          ],
        ),
      ),
    );
  }
}
