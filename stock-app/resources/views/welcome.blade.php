@extends('layouts.app')
@section('content')

    <div class="container">
        <div class="row">
            <div class="col-12 text-center pt-5">
                <h1 class="display-one mt-5">{{ config('app.name') }}</h1>
                <p>Click on the button below to view VN30 Stock</p>
                <a href = "{{route('get_info')}}" class="btn btn-primary" >Press to view</a>
            </div>
        </div>
    </div>
@endsection