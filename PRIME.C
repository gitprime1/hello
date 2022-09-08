
#include <stdio.h>
#include <conio.h>
#include <math.h>

void main()
{
   int tracker4 = 0;
    char a;
    int newone;
    int swap =0;
    int totalcount;
    int count = 0;
    int sum =0;
    int i;
    int lastBit;
    int number;
    int x;
    int j;
    int length =0;
    int tracker =0;
    int array3[4];
    int array[8];
    int array1[4];
    int array6[3];
    char string[15];
    clrscr();
    for(j = 0; j< 35;j++) {
	scanf("%c",&a);
	if(a == EOF || a == '\n') {
	    break;
	}
	if(a == '.') {
	    length = length + count;
	    sum =0;
	    for(i = 0; i< count;i++) {
		sum = sum * 10 + array[i];
	    }
	    for(i =0 ;i< 8;i++) {
		array[i] = 0;
	    }
	    count =0;
	    array1[tracker++] = sum;
	    continue;
	}
	array[count++] = a - '0';
    }
    sum =0;
    length = length + count;
    for(i = 0; i< count;i++) {
	sum = sum * 10 + array[i];

    }
    array1[tracker++] = sum;
    for(i =0; i< 4;i++) {
	number = array1[i];
	count =0;
	sum = 0;
	while(number > 0) {
	   lastBit = number%10;
	   if(lastBit == 1) {
	       sum = sum + pow(2,count);
	   }
	   count++;
	   number = number/10;
	}
	array3[tracker4++] = sum;

    }
    number = 0;
    newone =0;
    swap = 0;
    for(j =0; j < 4;j++) {
       swap++;
	number = array3[j];
	for( i =0 ;i < 3;i++) {
	    array6[i] = 0;
	}
	count =0;
	while(number > 0) {
	    array6[count++] = number%10;
	    number = number/10;
	}
	if(count == 0) {
	    string[newone++] = 0 + '0';
	    string[newone++] = 0 + '0';
	    string[newone++] = 0 + '0';
	}
	if(count == 2) {
	    string[newone++] = 0 + '0';
	}
	if(count == 1) {
	     string[newone++] = 0 + '0';
	     string[newone++] = 0 + '0';
	}
	for( i = count - 1;i>= 0;i--) {
	    string[newone++] = array6[i] + '0';

	}
	if(swap != 4) {
	    string[newone++] = '.';
	}
    }
    printf("%s",string);
    getch();
    return;
}
