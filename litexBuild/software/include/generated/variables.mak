PACKAGES=libcompiler_rt libbase libfatfs liblitespi liblitedram libliteeth liblitesdcard liblitesata bios
PACKAGE_DIRS=/home/camilo/LiteX/litex/litex/soc/software/libcompiler_rt /home/camilo/LiteX/litex/litex/soc/software/libbase /home/camilo/LiteX/litex/litex/soc/software/libfatfs /home/camilo/LiteX/litex/litex/soc/software/liblitespi /home/camilo/LiteX/litex/litex/soc/software/liblitedram /home/camilo/LiteX/litex/litex/soc/software/libliteeth /home/camilo/LiteX/litex/litex/soc/software/liblitesdcard /home/camilo/LiteX/litex/litex/soc/software/liblitesata /home/camilo/LiteX/litex/litex/soc/software/bios
LIBS=libcompiler_rt libbase-nofloat libfatfs liblitespi liblitedram libliteeth liblitesdcard liblitesata
TRIPLE=riscv64-unknown-elf
CPU=vexriscv
CPUFLAGS=-march=rv32im     -mabi=ilp32 -D__vexriscv__
CPUENDIANNESS=little
CLANG=0
CPU_DIRECTORY=/home/camilo/LiteX/litex/litex/soc/cores/cpu/vexriscv
SOC_DIRECTORY=/home/camilo/LiteX/litex/litex/soc
COMPILER_RT_DIRECTORY=/home/camilo/LiteX/pythondata-software-compiler_rt/pythondata_software_compiler_rt/data
export BUILDINC_DIRECTORY
BUILDINC_DIRECTORY=/home/camilo/MEGA/RequerimientosLiteX/SoCTemplateLiteX/litexBuild/software/include
LIBCOMPILER_RT_DIRECTORY=/home/camilo/LiteX/litex/litex/soc/software/libcompiler_rt
LIBBASE_DIRECTORY=/home/camilo/LiteX/litex/litex/soc/software/libbase
LIBFATFS_DIRECTORY=/home/camilo/LiteX/litex/litex/soc/software/libfatfs
LIBLITESPI_DIRECTORY=/home/camilo/LiteX/litex/litex/soc/software/liblitespi
LIBLITEDRAM_DIRECTORY=/home/camilo/LiteX/litex/litex/soc/software/liblitedram
LIBLITEETH_DIRECTORY=/home/camilo/LiteX/litex/litex/soc/software/libliteeth
LIBLITESDCARD_DIRECTORY=/home/camilo/LiteX/litex/litex/soc/software/liblitesdcard
LIBLITESATA_DIRECTORY=/home/camilo/LiteX/litex/litex/soc/software/liblitesata
BIOS_DIRECTORY=/home/camilo/LiteX/litex/litex/soc/software/bios