import 'dart:convert';
import 'package:http/http.dart' as http;
import 'database_helper.dart';

class SyncService {
  final String baseUrl = "http://10.0.2.2:8000/api"; // Android Emulator localhost

  Future<void> syncData() async {
    final db = await DatabaseHelper().database;
    final List<Map<String, dynamic>> queue = await db.query('sync_queue', orderBy: 'timestamp ASC');

    for (var item in queue) {
      try {
        final success = await _processSyncItem(item);
        if (success) {
          await db.delete('sync_queue', where: 'id = ?', whereArgs: [item['id']]);
        }
      } catch (e) {
        print("Sync failed for item ${item['id']}: $e");
        // Implement exponential backoff or retry logic if needed
      }
    }
  }

  Future<bool> _processSyncItem(Map<String, dynamic> item) async {
    final payload = json.decode(item['payload']);
    final response = await http.post(
      Uri.parse("$baseUrl/${item['table_name']}/"),
      body: json.encode(payload),
      headers: {"Content-Type": "application/json"},
    );

    return response.statusCode >= 200 && response.statusCode < 300;
  }

  Future<void> addToQueue(String tableName, String action, Map<String, dynamic> payload) async {
    final db = await DatabaseHelper().database;
    await db.insert('sync_queue', {
      'table_name': tableName,
      'action': action,
      'payload': json.encode(payload),
      'timestamp': DateTime.now().millisecondsSinceEpoch,
    });
  }
}
