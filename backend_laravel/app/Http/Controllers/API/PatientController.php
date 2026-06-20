<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Mother;
use Carbon\Carbon;

class PatientController extends Controller
{
    public function sync(Request $request, $id)
    {
        $mother = Mother::findOrFail($id);
        $localData = $request->all();

        $updatedFields = [];

        foreach ($localData as $field => $value) {
            if (in_array($field, ['id', 'user_id', 'last_synced_at'])) continue;

            // Simple field existence check
            // In a real Laravel app, we'd check if field exists on model
            if ($value !== null && $value !== "" && $mother->$field !== $value) {
                $mother->$field = $value;
                $updatedFields[] = $field;
            }
        }

        if (!empty($updatedFields)) {
            $mother->last_synced_at = Carbon::now();
            $mother->save();
        }

        return response()->json([
            'status' => 'synced',
            'updated_fields' => $updatedFields,
            'data' => $mother
        ]);
    }
}
