#! /bin/node

var n = Math.round(Math.sqrt(600851475143)) ;

var testArray = [] ;
for ( var i = 3 ; i < n + 2 ; i++ )
	testArray.push(i) ;

var testPrime = 3 ;

var resultArray = [] ;
var capValue = Math.sqrt( n ) ;
var primesFound = [ 2, 3 ] ;
var tempArray = [] ;

while ( testPrime < capValue ){
	console.log( testPrime, testArray.length ) ;
	for ( var a = 0 ; a < testArray.length ; a ++ ){
		resultArray.push( ( testArray[a] % testPrime ) );
	}
	
	for ( var q = 0 ; q < testArray.length ; q ++ ){
		if ( resultArray[q] !== 0 ){
			tempArray.push( testArray[q] ) ;
		}
	}
	
	testArray = tempArray ;
	tempArray = [] ;
	resultArray = [] ;
	testPrime = testArray[0] ;
	testArray.shift() ;
	primesFound.push( testPrime ) ;
}

for ( var a = 0 ; a < testArray.length ; a ++ )
	primesFound.push(testArray[a]) ;

for ( var i = primesFound.length - 1 ; i >= 0 ; i -- )
	if ( 600851475143 % primesFound[i] === 0 )
		break;

console.log( primesFound[i], 600851475143 / primesFound[i] ) ;

