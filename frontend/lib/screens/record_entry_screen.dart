import 'package:flutter/material.dart';

class RecordEntryScreen extends StatefulWidget {
  final String recordType; // ANC or Vaccination

  RecordEntryScreen({required this.recordType});

  @override
  _RecordEntryScreenState createState() => _RecordEntryScreenState();
}

class _RecordEntryScreenState extends State<RecordEntryScreen> {
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("New ${widget.recordType} Record")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: ListView(
            children: [
              TextFormField(decoration: InputDecoration(labelText: "Patient ID")),
              if (widget.recordType == "ANC") ...[
                TextFormField(decoration: InputDecoration(labelText: "Weight (kg)")),
                TextFormField(decoration: InputDecoration(labelText: "BP Systolic")),
                TextFormField(decoration: InputDecoration(labelText: "BP Diastolic")),
              ] else ...[
                TextFormField(decoration: InputDecoration(labelText: "Vaccine Name")),
                TextFormField(decoration: InputDecoration(labelText: "Batch Number")),
              ],
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text("Record Saved Locally")));
                  Navigator.of(context).pop();
                },
                child: Text("Save Record"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
