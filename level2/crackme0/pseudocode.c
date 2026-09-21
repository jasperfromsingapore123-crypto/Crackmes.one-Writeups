#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(int argc, char **argv){
	if (argc<2) return 0;
	char *input = argv[1];
	int var = 0;
	size_t length = strlen(input);
	for(int i = 0;i<length;i++){
		if ((i&1) == 1){
			continue;
		}
		else{
			var+=input[i]&0xf;
		}

	}
	int capacity = 1;
	char *odd_idx_chars = malloc(1);
	for(int count = 0;count<length;count++){
		if((count&1) == 1){
			capacity+=1;	
			odd_idx_chars = (char *)realloc(odd_idx_chars,capacity*sizeof(char));
			odd_idx_chars[capacity-2] = input[count];	
		}
	}	
	odd_idx_chars[capacity - 1] = '\0';
	size_t odd_length = strlen(odd_idx_chars);
	int sum = 0;
	for(int i = 0;i<odd_length;i++){
		char curr_char = odd_idx_chars[i];
		int value;
		if (curr_char >= 'a' && curr_char <= 'f') {
			value = curr_char-'a'+10;
			sum+=value;
		}
		else if (curr_char >= 'A'&& curr_char <= 'F') {
			value = curr_char-'A'+10;
			sum+=value;
		}
		else return 0;
	}
	int final;
	int temp = var + length;
	int variable = length+sum;
	if (var >= sum) final = temp % variable;
	else final = variable % temp;
	free(odd_idx_chars);
	if (final == 0) return 1;
	return 0;
}
