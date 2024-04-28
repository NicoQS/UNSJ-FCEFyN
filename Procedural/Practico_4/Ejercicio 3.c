#include <stdio.h>
#include <stdlib.h>

int mcd (int a, int b,int r)
{ 
if (a>b)
    { if(b>0)
        { r=b;
         b=a%b;
        a=r;
        return mcd(a,b,r);
        }//fin while
       else  return a;
        }//fin if
 else return 0;
}//fin mcd

int main (){
int a,b,r;
printf ("Ingrese un valor\n");
scanf("%d",&a);
printf ("Ingrese un valor\n");
scanf("%d",&b);
printf ("El valor de la funcion es %d\n",mcd(a,b,r));
system("pause");
}