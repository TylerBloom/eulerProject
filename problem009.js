#! /bin/node

var num1 = 1 ;
var num2 = 1 ;
var found = false ;

while ( ! found ){
	num1 ++ ;
	if ( num1 === 1000 ){
		num1 = 1 ;
		num2 ++ ;
	}
	if ( Number.isSafeInteger(Math.sqrt(num1*num1 + num2*num2)) && 
		num1 + num2 + Math.sqrt(num1*num1 + num2*num2) === 1000 ){
		
		found = true ;
	}
	
	if ( num2 > 1001 )
		break ;
}

