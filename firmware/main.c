#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <irq.h>
#include <uart.h>
#include <console.h>
#include <generated/csr.h>

unsigned int crt0 = 31;
int crt1 = 57;
unsigned char crt2 = 's';
char crt3 = 's';
unsigned short crt4 = 15;
short crt5 = 19;

void wait_ms(unsigned int time);

void wait_ms(unsigned int time){
	timer0_en_write(0);
	timer0_reload_write(0);
	timer0_load_write(time*(CONFIG_CLOCK_FREQUENCY/1000));
	timer0_en_write(1);
	timer0_update_value_write(1);
	while(timer0_value_read()) timer0_update_value_write(1);
}

int main(void) {
   irq_setmask((1<<GPIO_INTERRUPT)+(1<<UART_INTERRUPT));
	irq_setie(1);
   GPIO_ev_enable_write(1);
   uart_init();

   puts("hola");
   printf("%d, %d, %c, %c, %d, %d\n", crt0, crt1, crt2, crt3, crt4, crt5);

   while(1){
      char x = GPIO_SW_REG_read();
      if(x>9){
         puts("Estado de los switch: ");
         uart_write('1');
         uart_write((x-10)+48);
         uart_write('\n');
      }else{
         puts("Estado de los switch: ");
         uart_write(x+48);
         uart_write('\n');
      }

      

      if(x!=1){
         GPIO_LED_REG_write(0);
      }else{
         GPIO_LED_REG_write(1);
      }
      
      wait_ms(100);
      GPIO_LED_REG_write(2);
      wait_ms(100);
      GPIO_LED_REG_write(4);
      wait_ms(100);
      GPIO_LED_REG_write(8);
      wait_ms(100);
  
   }
   
   
   // while(1){
   //    if(switches_in_read() && 0x0007 != 0){
   //       leds_out_write(0xFFFF);
   //    }else{
   //       leds_out_write(0xFFFF);
   //    }
   // }
   return 0;
}