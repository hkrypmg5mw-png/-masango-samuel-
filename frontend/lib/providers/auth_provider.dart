import 'package:flutter/material.dart';
import '../services/auth_service.dart';

class AuthProvider with ChangeNotifier {
  final AuthService _authService = AuthService();
  bool _isAuthenticated = false;
  String? _role;
  Map<String, dynamic>? _userProfile;

  bool get isAuthenticated => _isAuthenticated;
  String? get role => _role;
  Map<String, dynamic>? get userProfile => _userProfile;

  Future<bool> login(String username, String password) async {
    final profile = await _authService.login(username, password);
    if (profile != null) {
      _isAuthenticated = true;
      _userProfile = profile;
      _role = profile['role'];
      notifyListeners();
      return true;
    }
    return false;
  }

  void logout() {
    _authService.logout();
    _isAuthenticated = false;
    _role = null;
    _userProfile = null;
    notifyListeners();
  }
}
