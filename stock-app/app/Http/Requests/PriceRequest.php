<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Validation\Rule;
class PriceRequest extends FormRequest
{
   
    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, mixed>
     */
    public function rules()
    {
        return [
            //
            'email' => ['required','email'],
            'user_price'=>['required','numeric',
            Rule::unique(table: 'users',column:'user_price')->where('email', $this->input(key:'email'))->where("stock_code", $this->input(key:'stock_code'))
            ]
        ];
    }


    public function messages()
    {
        return [
            'user_price.unique' => 'You have already entered this price for this Stock Code'
        ];
    }
}
