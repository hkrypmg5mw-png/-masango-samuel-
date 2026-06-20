import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class DatabaseHelper {
  static final DatabaseHelper _instance = DatabaseHelper._internal();
  factory DatabaseHelper() => _instance;
  DatabaseHelper._internal();

  static Database? _database;

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
      onCreate: (db, version) {
        return db.execute(
          "CREATE TABLE patients(id INTEGER PRIMARY KEY, name TEXT, data TEXT, last_updated TIMESTAMP, is_synced INTEGER)",
        );
      },
    );
  }

  Future<void> insertPatient(Map<String, dynamic> patient) async {
    final db = await database;
    await db.insert('patients', patient, conflictAlgorithm: ConflictAlgorithm.replace);
  }

  Future<List<Map<String, dynamic>>> getUnsyncedPatients() async {
    final db = await database;
    return await db.query('patients', where: 'is_synced = ?', whereArgs: [0]);
  }
}
