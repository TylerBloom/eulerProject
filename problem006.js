#! /bin/node

var sumSqrt = 0

for (var n = 1 ; n <= 100 ; n ++ ){
	sumSqrt += n*n ;
}

console.log( sumSqrt ) ;

sqrtSum = 0 ;

for (var i = 0 ; i <= 100 ; i ++ ){
	sqrtSum	+= i ;
}
sqrtSum	*= sqrtSum ;

console.log( sqrtSum ) ;

console.log( sqrtSum - sumSqrt ) ;

