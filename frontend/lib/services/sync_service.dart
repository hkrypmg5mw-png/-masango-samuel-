import 'dart:convert';
import 'package:http/http.dart' as http;
import 'database_helper.dart';
import 'auth_service.dart';

class SyncService {
  final String baseUrl = "http://10.0.2.2:8000/api/patients";
  final DatabaseHelper _dbHelper = DatabaseHelper();
  final AuthService _authService = AuthService();

  Future<void> syncData() async {
    final token = await _authService.getToken();
    if (token == null) return;

    final unsynced = await _dbHelper.getUnsyncedPatients();
    for (var item in unsynced) {
      try {
        final response = await http.post(
          Uri.parse('$baseUrl/mothers/${item['id']}/sync/'),
          body: item['data'],
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer $token'
          },
        );

        if (response.statusCode == 200) {
          final db = await _dbHelper.database;
          await db.update('patients', {'is_synced': 1}, where: 'id = ?', whereArgs: [item['id']]);
        }
      } catch (e) {
        print("Sync error for item ${item['id']}: $e");
      }
    }
  }
}
