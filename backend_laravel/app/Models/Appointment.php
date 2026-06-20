<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Appointment extends Model
{
    protected $fillable = [
        'mother_id', 'child_id', 'appointment_date', 'type', 'status', 'notes'
    ];
}
