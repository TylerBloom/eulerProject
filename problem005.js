#! /bin/node

var testNumbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] ;

var testValue = 2522 ;

while ( true ){
	var passed = true ;
	for ( var i = 0 ; i < testNumbers.length ; i ++ ){
		if ( testValue % testNumbers[i] !== 0 ){
			passed = false ;
			testValue += 2 ;
			break ;
		}
	}
	
	if ( passed ){
		break ;
	}
}
console.log( testValue ) ;

