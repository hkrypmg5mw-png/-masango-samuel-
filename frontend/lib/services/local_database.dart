import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class LocalDatabase {
  static final LocalDatabase instance = LocalDatabase._init();
  static Database? _database;

  LocalDatabase._init();

  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDB('mch.db');
    return _database!;
  }

  Future<Database> _initDB(String filePath) async {
    final dbPath = await getDatabasesPath();
    final path = join(dbPath, filePath);

    return await openDatabase(path, version: 1, onCreate: _createDB);
  }

  Future _createDB(Database db, int version) async {
    await db.execute('''
      CREATE TABLE mothers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        date_of_birth TEXT,
        address TEXT
      )
    ''');
    // Add other tables...
  }

  Future<void> cacheMothers(List<dynamic> mothers) async {
    final db = await instance.database;
    for (var mother in mothers) {
      await db.insert('mothers', {
        'id': mother['id'],
        'name': mother['user']['username'],
        'date_of_birth': mother['date_of_birth'],
        'address': mother['address'],
      }, conflictAlgorithm: ConflictAlgorithm.replace);
    }
  }

  Future<List<Map<String, dynamic>>> getCachedMothers() async {
    final db = await instance.database;
    return await db.query('mothers');
  }
}
