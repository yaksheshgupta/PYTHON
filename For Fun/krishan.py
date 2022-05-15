import keyboard as k
import time as t
t.sleep(3)
k.write('''#include<stdio.h>
void theory(float a){
    if (a<40)
        printf("%f",a);
    else if (a>=40 && a<60)
        printf("%f",a+a*0.04);
    else if (a>=60 && a<80)
        printf("%f",a+a*0.06);
    else if (a>=80 )
        printf("%f",a+a*0.08);
        
}
void lab(float a){
   
    if (a<40)
        printf("%f",a);
    else if (a>=40 && a<60)
        printf("%f",a+a*0.02);
    else if (a>=60 && a<80)
        printf("%f",a+a*0.04);
    else if (a>=80 )
        printf("%f",a+a*0.06);
        
    }
int main()
{
    
    float marks;
    char q[1];
    scanf("%f",&marks);
    scanf("%s",&q);
    if (marks!=0){
        if (q=="T")
           theory(marks);
        lab(marks);
    }
    else{
    printf("Enter appropriate Mark");
    }
    return 0;

}''')