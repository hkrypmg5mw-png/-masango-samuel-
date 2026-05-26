import 'package:flutter/material.dart';
import 'package:web_socket_channel/web_socket_channel.dart';
import 'package:provider/provider.dart';
import '../providers/auth_provider.dart';
import 'dart:convert';

class ChatScreen extends StatefulWidget {
  final int receiverId;
  final String receiverName;

  ChatScreen({required this.receiverId, required this.receiverName});

  @override
  _ChatScreenState createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final TextEditingController _controller = TextEditingController();
  late WebSocketChannel _channel;
  List<Map<String, dynamic>> _messages = [];

  @override
  void initState() {
    super.initState();
    // In production, use wss and the real host
    _channel = WebSocketChannel.connect(
      Uri.parse('ws://10.0.2.2:8000/ws/chat/'),
    );
    _channel.stream.listen((data) {
      setState(() {
        _messages.add(json.decode(data));
      });
    });
  }

  void _sendMessage() {
    if (_controller.text.isNotEmpty) {
      final msg = {
        'message': _controller.text,
        'receiver_id': widget.receiverId,
      };
      _channel.sink.add(json.encode(msg));
      _controller.clear();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Chat with ${widget.receiverName}")),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: _messages.length,
              itemBuilder: (context, index) {
                final m = _messages[index];
                return ListTile(
                  title: Text(m['message']),
                  subtitle: Text("From ID: ${m['sender_id']}"),
                );
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              children: [
                Expanded(child: TextField(controller: _controller)),
                IconButton(icon: Icon(Icons.send), onPressed: _sendMessage),
              ],
            ),
          )
        ],
      ),
    );
  }

  @override
  void dispose() {
    _channel.sink.close();
    super.dispose();
  }
}
