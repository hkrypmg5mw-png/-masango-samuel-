<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Process;

class MLController extends Controller
{
    public function predict(Request $request)
    {
        // For local development, we call the existing Python script
        // In a real export, the user would need Python and the joblib model.

        $data = json_encode($request->all());

        // This command assumes a python environment is available
        // and points to the utility script we wrote earlier.
        $command = "python3 ../backend/apps/ml/utils.py '" . $data . "'";

        // Mocking the result for now since we cannot easily bridge in this environment
        return response()->json([
            'risk_score' => 0.85,
            'is_high_risk' => true,
            'recommendation' => 'Consult a specialist immediately (Laravel Bridge Mock)'
        ]);
    }
}
