/* calculate tip */
#include<stdio.h>

int main()
{
    float bill, tip, total, payup;
    int share;
    printf("***TIP CALCULATOR***\n");
    printf("How much was the bill? ");
    scanf("%f", &bill);
    printf("How much is the tip 10, 12, 20%?");
    scanf("%f",&tip);
    printf("How many are sharing the bill?");
    scanf("%d",&share);
    total = bill + (bill * (tip/100));
    payup = total / share;
    printf("The bill plus tip is: %.2f.", total);
    printf("Each person needs to payup %.2f .", payup);

    return 0;
}
