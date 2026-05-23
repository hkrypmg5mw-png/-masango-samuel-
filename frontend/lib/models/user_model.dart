class User {
  final int id;
  final String username;
  final String email;
  final String role;
  final String? phoneNumber;

  User({required this.id, required this.username, required this.email, required this.role, this.phoneNumber});

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      id: json['id'],
      username: json['username'],
      email: json['email'],
      role: json['role'],
      phoneNumber: json['phone_number'],
    );
  }
}

class Mother {
  final int id;
  final User user;
  final String dateOfBirth;
  final String address;
  final String emergencyContact;

  Mother({required this.id, required this.user, required this.dateOfBirth, required this.address, required this.emergencyContact});

  factory Mother.fromJson(Map<String, dynamic> json) {
    return Mother(
      id: json['id'],
      user: User.fromJson(json['user']),
      dateOfBirth: json['date_of_birth'],
      address: json['address'],
      emergencyContact: json['emergency_contact_number'],
    );
  }
}
