#! /bin/node

var months = [31,28,31,30,31,30,31,31,30,31,30,31] ;

counter = 0 ;
day = 1 ;
month = 0 ;
year = 1901 ;

while ( year < 2001 ){
	day += months[month%12] ;
        month ++;
        if ( month % 12 === 0 ){
                year ++ ;
        }
	
	if ( month % 12 === 1 && year % 4 === 0){6
		day += 1;
	}
	if ( day % 7 === 6 ){
		counter++ ;
		console.log( year + "-" + month % 12 + "-" + day % 7 + " is a Sunday" ) ;
	}
}

console.log( counter );

