import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class SOSScreen extends StatefulWidget {
  @override
  _SOSScreenState createState() => _SOSScreenState();
}

class _SOSScreenState extends State<SOSScreen> {
  bool _isSending = false;

  void _triggerSOS() async {
    setState(() => _isSending = true);
    // Simulate sending SOS to SMS, Facility, and Workers
    await Future.delayed(Duration(seconds: 2));
    if (mounted) {
      setState(() => _isSending = false);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("SOS Alerts Sent Successfully!"), backgroundColor: Colors.red),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Emergency SOS")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("In case of emergency, press the button below:", style: TextStyle(fontSize: 18)),
            SizedBox(height: 40),
            GestureDetector(
              onTap: _isSending ? null : _triggerSOS,
              child: Container(
                width: 200,
                height: 200,
                decoration: BoxDecoration(
                  color: Colors.red,
                  shape: BoxShape.circle,
                  boxShadow: [BoxShadow(color: Colors.redAccent, blurRadius: 20, spreadRadius: 5)],
                ),
                child: Center(
                  child: _isSending
                    ? CircularProgressIndicator(color: Colors.white)
                    : Icon(FontAwesomeIcons.triangleExclamation, size: 80, color: Colors.white),
                ),
              ),
            ),
            SizedBox(height: 20),
            Text(_isSending ? "Alerting Emergency Contacts..." : "HOLD TO TRIGGER",
                 style: TextStyle(color: Colors.red, fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}
