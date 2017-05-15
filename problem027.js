#! /bin/node

var num = 0;
var count = 0;
var maxCount = 0;

for( var b = -1000; b <= 1000; b++){
	console.log(b,a);
	for ( var a = -999; a < 1000; a ++){
		n = -1000;
		while( n < 1001 ){
			num = n*n + a*n + b;
			if ( num > 1 ){
				var ceil = Math.sqrt(num);
				i = 2;
				while ( i <= ceil ){
					if (num % i == 0)
						if ( count > maxCount ){
							maxCount = count;
							var maxB = b;
							var maxA = a;
						}
						count = 0;
					i += 1;
				}
			}
			if ( num < 0 )
				if ( count > maxCount ){
					maxCount = count;
					var maxB = b;
					var maxA = a;
				}
				count = 0
			n += 1;
			count += 1;

		}
		if ( count > maxCount ){
			maxCount = count;
			var maxB = b;
			var maxA = a;
		}
		count = 0;
	}
}

console.log(maxCount, maxB, maxA);



