<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Child extends Model
{
    protected $fillable = [
        'mother_id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'birth_weight', 'birth_height'
    ];
}
