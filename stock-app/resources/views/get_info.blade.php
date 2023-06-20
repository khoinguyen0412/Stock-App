@extends('layouts.app')
@section('content')
        <div class="table-container" >
            <table border=10 cellpadding=20>
            <thead>
                 <tr>
                    <td>#</td>
                    <td>Stock Code</td>
                    <td>Current Price</td>
                 </tr>  
            </thead>
                 @foreach($stock_codes as $keys => $stock_code) 
                 <tr>
                    <td>{{$keys+1}}</td>
                    <td>{{$stock_code->name}}</td>
                    <td class = "price-box" id="price-{{$stock_code->name}}">Loading data...</td>
                 </tr>
                @endforeach
            </table>

        </div>


            <h1 style="text-align:center ; margin:10px">Please check the box to track your stock</h1>
            
            <div class = "form-control">
                <div class="checkbox-row"> 
                    @foreach($stock_codes as $stock_code)
                        <label class = "rc-label">
                            <div class="form-check">
                                <input class="form-check-input" type = "checkbox" data-toggle="modal" data-target="#exampleModalCenter" 
                                data-backdrop="static" data-keyboard="false" id= "{{$stock_code->name}}" onclick= "updateDialog(this)"></input>
                                    <span class="form-check-label">
                                            {{ $stock_code->name}}
                                    </span>
                            </div>
                        </label>
                    @endforeach
                </div>
            </div>

            <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true" >
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLongTitle">Fill in the blank</h5>
                            <button id="close-button" type="button" class="close" data-dismiss="modal" aria-label="Close" onclick= "uncheck()">
                            <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">

                        <form id="form" action="{{route('get_info.post')}}" method="post">
                            @csrf
                                <div class="form-group row">
                                <label id="modal-label" for="email" class="col-md-4 col-form-label">Stock Code</label>
                                    <input id="input_stock" type="text" class="form-control" value="" readonly= "true" name="stock_code">
                                </div>

                                <div class="form-group row">
                                <label id="modal-label" for="email" class="col-md-4 col-form-label">Desired Price</label>
                                    <input id = "user_price" type="number" step="0.01" class="form-control" placeholder="0.00" name= "user_price" required>             
                                </div>

                                <div class="form-group row">
                                    <label id="modal-label" for="email" class="col-md-4 col-form-label">E-Mail Address</label>
                                    <input id = "Email" type="email" class="form-control" placeholder="Your Email" name="email" required>
                                </div>
                                
                        
                        </div>
                            <div class="modal-footer">
                                <button id ="close-button" type="button" class="btn btn-secondary" data-dismiss="modal" onclick = "uncheck()">Close</button>
                                <button type="submit" class="btn btn-primary" >Submit</button>
                            </div>
                        </form>
                        </div>
                    </div>
            </div>
@endsection