<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Message;

class ChatController extends Controller
{
    public function messages(Request $request)
    {
        $user = $request->user();
        return Message::where('sender_id', $user->id)
                      ->orWhere('receiver_id', $user->id)
                      ->orderBy('created_at', 'asc')
                      ->get();
    }
}
