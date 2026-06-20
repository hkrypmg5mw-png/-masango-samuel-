<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up()
    {
        Schema::create('appointments', function (Blueprint $table) {
            $table->id();
            $table->foreignId('mother_id')->nullable()->constrained();
            $table->foreignId('child_id')->nullable()->constrained();
            $table->dateTime('appointment_date');
            $table->string('type'); // ANC, Vaccination, etc.
            $table->string('status')->default('SCHEDULED');
            $table->text('notes')->nullable();
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('appointments');
    }
};
