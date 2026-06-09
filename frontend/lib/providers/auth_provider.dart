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