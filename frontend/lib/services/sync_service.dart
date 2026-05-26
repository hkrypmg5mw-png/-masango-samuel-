import 'dart:convert';
import 'package:http/http.dart' as http;
import 'database_helper.dart';

class SyncService {
  final String baseUrl = "http://10.0.2.2:8000/api/patients";
  final DatabaseHelper _dbHelper = DatabaseHelper();

  Future<void> syncData() async {
    final unsynced = await _dbHelper.getUnsyncedPatients();
    for (var item in unsynced) {
      final response = await http.post(
        Uri.parse('$baseUrl/sync/'),
        body: item['data'],
        headers: {'Content-Type': 'application/json'},
      );

      if (response.statusCode == 200) {
        // Mark as synced
        final db = await _dbHelper.database;
        await db.update('patients', {'is_synced': 1}, where: 'id = ?', whereArgs: [item['id']]);
      }
    }
  }
}
