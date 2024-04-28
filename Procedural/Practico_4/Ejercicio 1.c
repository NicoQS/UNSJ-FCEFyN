#include <stdio.h>
#define N 4

void FuncionA (int n){
 if (n)
 { printf("%d", n%10);
 n=n/10;
 FuncionA (n);
 }
}

int FuncionB (int n){
if (n==0){
 return n;}
 else{
 return FuncionB (n/10)+(n%10);}
}

int FuncionC (int x[], int n, int dato){
if(n==0)
 {if (dato > x[n])
 return x [0];
 else
 return dato;
 }
 else
 {if (dato > x[n])
return FuncionC (x, n-1, x[n]);
else return FuncionC (x, n-1, dato);
 }
}
int main(){
int a,b,c,dato;
int x[N]= {25,18,56,35};
printf ("Ingrese un numero para la funcion A\n");
scanf("%d",&a);
FuncionA(a);
printf ("\nIngrese un numero para la funcion B\n");
scanf("%d",&b);
printf ("Resultado obtenido de B: %d\n",FuncionB(b));
printf ("\nIngrese un numero para la funcion C\n");
scanf ("%d",&c);
printf ("\nIngrese un dato para la funcion B\n");
scanf("%d",&dato);
printf ("Resultado de la funcion C %d",FuncionC(x,c,dato));
}



