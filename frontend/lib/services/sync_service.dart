import 'package:dio/dio.dart';
import 'database_service.dart';
import 'api_service.dart';

class SyncService {
  final DatabaseService _dbService = DatabaseService();
  final ApiService _apiService = ApiService();

  Future<void> syncData() async {
    final unsynced = await _dbService.getUnsyncedRecords();
    for (var record in unsynced) {
      try {
        // Logic for "Latest update wins" (simply sync if local is newer or as requested)
        // This is a simplified placeholder for the sync logic
        print('Syncing record: \${record['id']}');

        // Mock API call to sync
        // await _apiService.syncRecord(record['id'], record['data']);

        final db = await _dbService.database;
        await db.update('records', {'is_synced': 1}, where: 'id = ?', whereArgs: [record['id']]);
      } catch (e) {
        print('Sync failed for record \${record['id']}: \$e');
      }
    }
  }
}
