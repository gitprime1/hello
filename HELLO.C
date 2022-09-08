#include <stdio.h>
#include <conio.h>

int main()
{
    int tracker4 = 0;
    char a;
    int swap =0;
    int low = 0;
    int high =0;
    int count = 0;
    int sum =0;
    int i;
    int number;
    int x;
    int j;
    int length =0;
    int tracker =0;
    int array3[8];
    int array[3];
    int array1[4];
    char string[35];
    clrscr();
    for(j = 0; j< 16;j++) {
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
	    for(i =0 ;i< 3;i++) {
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
	for(x =0; x  < 8;x++) {
	    array3[x] = 0;
	}
	while(number > 0) {
	    if(number & 1 == 1) {
		array3[count++] = 1;
	    }
	    else {
		array3[count++] = 0;
	    }
	    number = number >> 1;
	}
	low =0;
	high =7;
	while(low < high) {
	    swap = array3[low];
	    array3[low] = array3[high];
	    array3[high] = swap;
	    low++;
	    high--;
	}
	for( j =0; j<8;j++) {
	    a = array3[j] + '0';
	    string[tracker4++] = a;
	    if(tracker4 == 35) {
		break;
	    }
	}
	if(tracker4  <  32) {
	    string[tracker4++] = '.';
	}
    }
    printf("%s",string);
    getch();
    return 0;
}