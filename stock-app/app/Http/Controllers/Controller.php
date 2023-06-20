<?php

namespace App\Http\Controllers;

use App\Models\Stock_Code;
use App\Models\User;
use Illuminate\Http\Request;
use App\Http\Requests\PriceRequest;
use Illuminate\Validation\Rule;
use Illuminate\Routing\Controller as BaseController;

class Controller extends BaseController
{
    // use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

    public function index(){
        $stock_codes = Stock_Code::all();
        return view('get_info')->with('stock_codes', $stock_codes);
    }

    public function store(PriceRequest $request){
        
        // $request->validate([
        //     'email' => ['required','email'],
        //     'user_price'=>['required','numeric',
        //     Rule::unique(table: 'users',column:'user_price')->where('email', $input_email)->where("stock_code",$input_stock_code)
        //     ]
        // ]);

        $newRequest = User::create([
            'email'=>$request->email,
            'stock_code'=>$request->stock_code,
            'user_price'=>$request->user_price,
            'is_active'=> 1 ,
        ]);

        return response()->noContent();
    }
}
