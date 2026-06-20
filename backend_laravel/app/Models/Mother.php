<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Mother extends Model
{
    protected $fillable = [
        'user_id',
        'date_of_birth',
        'address',
        'emergency_contact_name',
        'emergency_contact_phone',
        'blood_group',
        'last_synced_at',
    ];

    public function user() {
        return $this->belongsTo(User::class);
    }
}
