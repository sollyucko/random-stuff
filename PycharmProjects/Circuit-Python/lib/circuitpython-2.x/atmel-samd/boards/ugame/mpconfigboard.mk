LD_FILE = boards/samd21x18-bootloader-external-flash-crystalless.ld
#LD_FILE = boards/samd21x18-bootloader.ld
USB_VID = 0x239A
USB_PID = 0x801F

#FLASH_IMPL = internal_flash.c
FLASH_IMPL = spi_flash.c

CHIP_VARIANT = SAMD21E18A
CHIP_FAMILY = samd21
