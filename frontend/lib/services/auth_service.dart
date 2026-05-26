import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class AuthService {
  // Use 10.0.2.2 for Android Emulator, localhost for iOS/Web
  final String baseUrl = "http://10.0.2.2:8000/api/auth";
  final storage = FlutterSecureStorage();

  Future<Map<String, dynamic>?> login(String username, String password) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/login/'),
        body: {'username': username, 'password': password},
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        await storage.write(key: 'access', value: data['access']);
        await storage.write(key: 'refresh', value: data['refresh']);

        // Fetch profile to get role
        final profileResponse = await http.get(
          Uri.parse('$baseUrl/profile/'),
          headers: {'Authorization': 'Bearer ${data['access']}'},
        );
        if (profileResponse.statusCode == 200) {
          return json.decode(profileResponse.body);
        }
      }
    } catch (e) {
      print("Login error: $e");
    }
    return null;
  }

  Future<void> logout() async {
    await storage.deleteAll();
  }

  Future<String?> getToken() async {
    return await storage.read(key: 'access');
  }
}
