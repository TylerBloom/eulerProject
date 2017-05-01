#! /bin/node

var sum = 0 ;
var x = 1 ;
var y = 1 ;
var temp = 0 ;

while ( y < 4000000 ){
	if ( y % 2 === 0 )
		sum += y ;
	temp = y ;
	y += x ;
	x = temp ;
	console.log( y ) ;
}

