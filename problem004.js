#! /bin/node

var num1 = 999 ;
var num2 = 999 ;
var value = num1 * num2 ;
var record = [] ;
while ( num2 > 901 ){
	num1 -- ;
	
	if ( num1 === 900 ){
		num1 = num2 - 2 ;
		num2 -- ;
	}
	if ( num1 % 10 === 0 ){
		num1 -- ;
	}
	if ( num2 % 10 === 0 ){
                num2 -- ;
        }
	value = num1 *  num2 ;
	value = value.toString() ;
	var found = true ;
	for ( var i = 0 ; i < value.length / 2 ; i ++ ){
		if( value.charAt(i) !== value.charAt(value.length - 1 - i)){
			found = false ;
		}
		if ( found === false ){
			break ;
		}
	}
	if ( found === true ){
		record.push(Number(value)) ;
	}
}
var largest = 0 ;
for ( var t = 0 ; t < record.length ; t ++ ){
	if ( record[t] > largest ){
		largest = record[t] ;
	}
}
console.log(largest) ;




