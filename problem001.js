#! /bin/node

var array = [] ;
for ( var i = 1 ; i < 1000 ; i ++ ){
	array.push(i) ;
}

var sum = 0 ;

for ( var n = 0 ; n < array.length ; n ++){
	if ( array[n] % 3 === 0 || array[n] % 5 === 0 ){
		sum += array[n] ;
	}
}

console.log( sum ) ;

