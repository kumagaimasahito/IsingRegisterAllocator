/**************************************/
/*  モンテカルロ法で円周率πを求める  */
/*  単位円と外接矩形                  */
/**************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double solve(){
    int  j,jmax=10000000;                        // 点の発生数
    int  Ni;                                     // 単位円内の回数
    double x,y,max,pi;

    max=(double)RAND_MAX;                        // 乱数最大値
    srand(time(NULL));                           // 乱数の準備

    for( j=0,Ni=0; j<jmax; j++ )                 // 点を発生
      {
        x=(double)rand( )/max;                   // x=乱数(0～1)
        y=(double)rand( )/max;                   // y=乱数(0～1)
        if ( x*x+y*y<=1.0 ) Ni++;                // 点は単位円内
      }

    pi=(double)Ni/(double)jmax*4;                // π/4を4倍

    return pi;
}

int main(void)
{
    printf("\nπ≒%lf\n",solve());
    return 0;
}