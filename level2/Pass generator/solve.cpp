#include <iostream>
#include <string>
using namespace std;
int main(){
	string target = "Tl0d";
	string var_60 = "P0G";
	int x = rand();
	for (char &c:target){
		c+=16;
	}
	for (char &c:var_60){
		c+=16;
	}

	int key1,key2,key3;
	int temp = target[1]*var_60[2]&0x80000001;
	if (temp < 0){
		temp = ((temp - 1) | 0xfffffffe) + 1;
	}
	key1 = (temp+target[0])*var_60[0]+target[3]*target[2];
	key2 = ((var_60[0]+var_60[2]-target[0]+var_60[1])/target[3])*var_60[1]+0xbb;
	key3 = (((target[2]+var_60[1])*0x26f6)/var_60[0])-target[3]*5+0x369;
	cout<<"Key 1: "<<key1<<"\n";
	cout<<"key 2: "<<key2<<"\n";
	cout<<"Key 3: "<<key3<<"\n";

	return 0;
}

/*
Notes:
I have split the target string into 2, namely target and var_60 for the ease of writing this script,
else if have to constantly do addition when calculating which index to use.

There are 3 keys which are decided by the random value that is generated.

*/
