#include <time.h>

#define norm 2.328306549295728e-10
#define m1   4294967087.0
#define m2   4294944443.0
#define a12     1403580.0
#define a13n     810728.0
#define a21      527612.0
#define a23n    1370589.0

double MRG32k3a (void)
{
   static double s10 = 12345, s11 = 12345, s12 = 123,
                 s20 = 12345, s21 = 12345, s22 = 123;

   /* Initialize seed based on current time */
   static int seed_initialized = 0;
   if (!seed_initialized) {
       unsigned int seed = (unsigned int)time(NULL);
       s10 = seed;
       s11 = seed;
       s12 = seed;
       s20 = seed;
       s21 = seed;
       s22 = seed;
       seed_initialized = 1;
   }

   long   k;
   double p1, p2;
   /* Component 1 */
   p1 = a12 * s11 - a13n * s10;
   k = p1 / m1;   p1 -= k * m1;   if (p1 < 0.0) p1 += m1;
   s10 = s11;   s11 = s12;   s12 = p1;

   /* Component 2 */
   p2 = a21 * s22 - a23n * s20;
   k  = p2 / m2;  p2 -= k * m2;   if (p2 < 0.0) p2 += m2;
   s20 = s21;   s21 = s22;   s22 = p2;

   /* Combination */
   if (p1 <= p2) return ((p1 - p2 + m1) * norm);
   else return ((p1 - p2) * norm);
}
