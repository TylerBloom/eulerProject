#! /bin/node

var n = 2000000 ;

var testArray = [] ;
for ( var i = 5 ; i < n + 2 ; i++ )
	testArray.push(i) ;

var testPrime = 3 ;

var resultArray = [] ;
var capValue = Math.sqrt( n ) ;
var primesFound = [ 2, 3 ] ;
var tempArray = [] ;

while ( testPrime < capValue ){
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

for ( var y = 0 ; y < testArray.length ; y ++ ){
	primesFound.push(testArray[y]) ;
}

var sum = 0 ;

for (var j = 0 ; j < primesFound.length ; j ++ ){
	sum += primesFound[j] ;
}

