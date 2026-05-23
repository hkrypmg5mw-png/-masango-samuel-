import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import '../utils/config.dart';

class ApiService {
  static const String baseUrl = Config.baseUrl;
  final _storage = const FlutterSecureStorage();

  Future<String?> get _token async => await _storage.read(key: 'access_token');

  Future<Map<String, String>> get _headers async {
    final token = await _token;
    return {
      'Content-Type': 'application/json',
      if (token != null) 'Authorization': 'Bearer $token',
    };
  }

  Future<http.Response> login(String username, String password) async {
    final response = await http.post(
      Uri.parse('$baseUrl/token/'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'username': username, 'password': password}),
    );
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      await _storage.write(key: 'access_token', value: data['access']);
      await _storage.write(key: 'refresh_token', value: data['refresh']);
    }
    return response;
  }

  Future<http.Response> getMothers() async {
    return await http.get(Uri.parse('$baseUrl/mothers/'), headers: await _headers);
  }

  // Add more methods for other endpoints...
}
