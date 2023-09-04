#include <stdio.h>
#include "unif01.h"
#include "bbattery.h"
extern double MRG32k3a(void);

int main(void)
{
   unif01_Gen *gen;
   gen = unif01_CreateExternGen01 ("MRG32k3a", MRG32k3a);
   bbattery_SmallCrush(gen);
   unif01_DeleteExternGen01(gen);
   return 0;
}
