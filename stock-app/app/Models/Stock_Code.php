<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Stock_Code extends Model
{
    use HasFactory;
    protected $fillable = [
        'name',
    ];
}
