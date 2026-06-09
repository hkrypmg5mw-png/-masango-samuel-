import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class DatabaseService {
  static final DatabaseService _instance = DatabaseService._internal();
  factory DatabaseService() => _instance;
  DatabaseService._internal();

  Database? _database;

  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDatabase();
    return _database!;
  }

  Future<Database> _initDatabase() async {
    String path = join(await getDatabasesPath(), 'mch_local.db');
    return await openDatabase(
      path,
      version: 1,
      onCreate: (db, version) async {
        await db.execute('''
          CREATE TABLE records (
            id TEXT PRIMARY KEY,
            data TEXT,
            last_updated INTEGER,
            is_synced INTEGER DEFAULT 0
          )
        ''');
      },
    );
  }

  Future<void> saveRecord(String id, String data) async {
    final db = await database;
    await db.insert(
      'records',
      {
        'id': id,
        'data': data,
        'last_updated': DateTime.now().millisecondsSinceEpoch,
        'is_synced': 0,
      },
      conflictAlgorithm: ConflictAlgorithm.replace,
    );
  }

  Future<List<Map<String, dynamic>>> getUnsyncedRecords() async {
    final db = await database;
    return await db.query('records', where: 'is_synced = ?', whereArgs: [0]);
  }
}
