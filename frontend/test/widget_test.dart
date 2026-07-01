import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mch_app/main.dart';
import 'package:mch_app/providers/auth_provider.dart';
import 'package:provider/provider.dart';

void main() {
  testWidgets('Login screen loads correctly', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => AuthProvider()),
        ],
        child: const MCHApp(),
      ),
    );

    // Verify that the login title exists.
    expect(find.text('MCH Cameroon'), findsOneWidget);
    expect(find.text('Login'), findsOneWidget);
  });
}
