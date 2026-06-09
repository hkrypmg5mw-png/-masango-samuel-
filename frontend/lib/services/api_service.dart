import 'package:dio/dio.dart';
import '../core/constants.dart';
class ApiService {
  final Dio _dio = Dio(BaseOptions(baseUrl: ApiConstants.baseUrl));
  Future<Response> login(String username, String password) async {
    return await _dio.post('/auth/login/', data: {'username': username, 'password': password});
  }
}