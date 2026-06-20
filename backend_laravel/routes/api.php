<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\API\AuthController;
use App\Http\Controllers\API\PatientController;

Route::post('/auth/login', [AuthController::class, 'login']);

Route::middleware('auth:sanctum')->group(function () {
    Route::get('/auth/profile', [AuthController::class, 'profile']);
    Route::post('/patients/mothers/{id}/sync', [PatientController::class, 'sync']);
    Route::post('/ml/predict', [MLController::class, 'predict']);
    Route::get('/appointments', [AppointmentController::class, 'index']);
    Route::get('/chat/messages', [ChatController::class, 'messages']);
    Route::post('/appointments', [AppointmentController::class, 'store']);
    Route::get('/chat/messages', [ChatController::class, 'messages']);
});
