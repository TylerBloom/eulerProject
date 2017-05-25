#! /bin/node

var start = "10000000";
var input = start;
var n = 0; 
var until = 1000;
var passes1 = new Array;
var index = input.length - 1; 
var passes2 = new Array;
var startIndex = index;

while ( n <= until ){
	if ( input.charAt(index) === input.charAt(startIndex-index) ){
		index --;
		if ( index <= startIndex / 2 )
			if ( input.charAt(index) === input.charAt(startIndex-index) ){
				passes1[n] = input;
				input = Number( input ) + 1;
				input = input.toString();
				startIndex = input.length - 1;
				index = startIndex;
				n ++;
			}
	}else{
		input = Number(input) + Math.pow(10, startIndex-index) ;
		input = input.toString();
		index = input.length - 1;
		startIndex = index;
	}
}
input = start;
n = 0;
while ( n <= until ){
	if ( input.charAt(index) === input.charAt(startIndex-index) ){
		index --;
		if ( index <= startIndex / 2 )
			if ( input.charAt(index) === input.charAt(startIndex-index) ){
				passes2[n] = input;
				input = Number( input ) + 1;
				input = input.toString();
				startIndex = input.length - 1;
				index = startIndex;
				n ++;
			}
	}else{
		input = Number( input ) + 1 ;
		input = input.toString();
		index = input.length - 1;
		startIndex = index;
	}
}

n = 0;
while ( n <= 1000 ){
	if ( passes1[n] !== passes2[n] )
		console.log ( n, false, passes1[n], passes2[n] );
	n ++;
}
console.log ( "Done" );
