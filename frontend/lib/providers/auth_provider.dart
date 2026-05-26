import 'package:flutter/material.dart';
import '../services/auth_service.dart';

class AuthProvider with ChangeNotifier {
  final AuthService _authService = AuthService();
  bool _isAuthenticated = false;
  String? _role;

  bool get isAuthenticated => _isAuthenticated;
  String? get role => _role;

  Future<bool> login(String username, String password) async {
    bool success = await _authService.login(username, password);
    if (success) {
      _isAuthenticated = true;
      // Ideally fetch profile here to get role
      notifyListeners();
    }
    return success;
  }

  void logout() {
    _authService.logout();
    _isAuthenticated = false;
    notifyListeners();
  }
}
