import 'package:flutter/material.dart';

class AuthProvider with ChangeNotifier {
  bool _isAuthenticated = false;
  String? _token;
  String _role = 'MOTHER';

  bool get isAuthenticated => _isAuthenticated;
  String? get token => _token;
  String get role => _role;

  Future<void> login(String phoneNumber, String password) async {
    // Demo Logic: if password is 'nurse', login as NURSE
    if (password.toLowerCase() == 'nurse') {
      _role = 'NURSE';
    } else {
      _role = 'MOTHER';
    }
    _isAuthenticated = true;
    _token = "mock_token";
    notifyListeners();
  }

  void logout() {
    _isAuthenticated = false;
    _token = null;
    notifyListeners();
  }
}
