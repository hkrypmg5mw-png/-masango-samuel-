import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import '../services/api_service.dart';

class AuthProvider with ChangeNotifier {
  final ApiService _apiService = ApiService();
  final _storage = const FlutterSecureStorage();

  bool _isLoading = false;
  String? _token;
  String? _role;
  bool _mustChangePassword = false;

  bool get isLoading => _isLoading;
  String? get token => _token;
  String? get role => _role;
  bool get mustChangePassword => _mustChangePassword;

  Future<bool> login(String email, String password) async {
    _isLoading = true;
    notifyListeners();

    try {
      final response = await _apiService.post('/auth/login/', {
        'email': email,
        'password': password,
      });

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        _token = data['access'];

        // Decode JWT to get role and must_change_password (simplified)
        // In real app, use a JWT decoder package
        _role = data['role'] ?? 'MOTHER';
        _mustChangePassword = data['must_change_password'] ?? false;

        await _storage.write(key: 'jwt_token', value: _token);

        _isLoading = false;
        notifyListeners();
        return true;
      }
    } catch (e) {
      print("Login Error: $e");
    }

    _isLoading = false;
    notifyListeners();
    return false;
  }

  Future<void> logout() async {
    await _storage.delete(key: 'jwt_token');
    _token = null;
    _role = null;
    notifyListeners();
  }
}
