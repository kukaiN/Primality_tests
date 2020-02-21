#include<iostream>

int baillie_PSW(int n){
    if miller_rabbin_test(n){
        if lucas_test(n){
            return 1;
        }
    }
    return 0;
}

int miller_rabbin_test(int n){
    int number = n-1;
    int pow_of_two = 0;
    int base_2;
    while(1){
        if(not number & 1){
            number = number/2;
            pow_of_two+=1;
        }
        else{break;}
    }
    if(number < 1001){base_2 = (2**number)%n;}
    else{base_2 = exp_and_mod(2 number, n);}
    if (abs(base_2) == 1){ return 1;}
    for(int t = 0; t < pow_of_two; ++t){
        base_2 = (base_2*base_2)%n;
        if(abs(base_2) == 1){return 1;}
    }
    return 0;
}

int lucas_test(int n){
    if (math.sqrt(n)%1 == 0){return 0;}
    int D_and_Q = find(n); // arrayyyyyy is being returned.
    int D = D_and_Q

}

int recursive_UV(int P, int Q, int D, int n, int N){
    //stuff
}

int exp_and_mod(int base, int exponent, n){
    
    int sub_exponent;
    if(exponent == 0){return 1;}
    if(exponent%2==0){base = abs(base);}
    if(base == 0 or base == 1){return base;}
    if(base == 4){base = 2; exponent*=2;}
    if(abs(base) == 2){sub_exponent=128;}
    elif(abs(base) == 3){sub_exponent=80;}
    elif(abs(base) == 5){sub_exponent=56;}
    elif(abs(base) <= 10){sub_exponent=38;}
    elif(abs(base) <= 100){sub_exponent=9;}
    else{std::cout<<"need to rewrite exponent and mod function to accpet higher values.\n";}
    int quotient = exponent/sub_exponent;
    int remainder = exponent%sub_exponent;
    int new_base = (base**sub_exponent)%n;


}

int is_prime(int n){
}

int jacobi_symbol(int a, int p){


}

int find_D(int n){

}


int main(){
    int* D;
    int* Q;
    
    return 0;
}