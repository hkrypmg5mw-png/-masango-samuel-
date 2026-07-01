import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class DatabaseHelper {
  static final DatabaseHelper _instance = DatabaseHelper._internal();
  static Database? _database;

  factory DatabaseHelper() => _instance;

  DatabaseHelper._internal();

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
      onCreate: _onCreate,
    );
  }

  Future _onCreate(Database db, int version) async {
    // Mothers Table
    await db.execute('''
      CREATE TABLE mothers (
        id INTEGER PRIMARY KEY,
        full_name TEXT,
        date_of_birth TEXT,
        last_menstrual_period TEXT,
        estimated_date_of_delivery TEXT,
        risk_level TEXT,
        is_synced INTEGER DEFAULT 1
      )
    ''');

    // Children Table
    await db.execute('''
      CREATE TABLE children (
        id INTEGER PRIMARY KEY,
        mother_id INTEGER,
        full_name TEXT,
        date_of_birth TEXT,
        gender TEXT,
        is_synced INTEGER DEFAULT 1,
        FOREIGN KEY (mother_id) REFERENCES mothers (id)
      )
    ''');

    // Offline Sync Queue
    await db.execute('''
      CREATE TABLE sync_queue (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        endpoint TEXT,
        method TEXT,
        body TEXT,
        timestamp TEXT
      )
    ''');
  }
}
