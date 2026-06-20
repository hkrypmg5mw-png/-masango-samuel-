<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Appointment;

class AppointmentController extends Controller
{
    public function index(Request $request)
    {
        if ($request->user()->role == 'MOTHER') {
            return Appointment::where('mother_id', $request->user()->id)->get();
        }
        return Appointment::all();
    }

    public function store(Request $request)
    {
        $data = $request->validate([
            'mother_id' => 'nullable|exists:mothers,id',
            'child_id' => 'nullable|exists:children,id',
            'appointment_date' => 'required|date',
            'type' => 'required|string',
            'notes' => 'nullable|string',
        ]);

        return Appointment::create($data);
    }
}
