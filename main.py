
import machine,dht,ssd1306,time,esp
import pbm

esp.osdebug(None) 
GPIO2 = 2
sensor = dht.DHT22(machine.Pin(GPIO2))
spi = machine.SPI(1, baudrate=80000000, polarity=0, phase=0)
oled = ssd1306.SSD1306_SPI(128, 64, spi, machine.Pin(5), machine.Pin(0), machine.Pin(15))
                                            #DC, reset, and CS
cat = pbm.PBM_P1("cat.pbm")          

OLED_WIDTH,OLED_HEIGTH = 128,64
machine.freq(160000000)
        
    
##MAIN LOOP
while True:
    
    oled.fill(0)
    
    for row in range(cat.height):
        for col in range(cat.width):
            oled.pixel(col, row, cat.get(row,col))
    oled.show()
    
