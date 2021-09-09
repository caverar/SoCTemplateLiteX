#!/usr/bin/env python3

from migen import *

from migen.genlib.io import CRG

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform

from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *

from litex.soc.cores.clock import *

#from litex.soc.cores import dna, xadc
#from litex.soc.cores.spi import SPIMaster



from Hardware.gpio import gpio

# IOs ----------------------------------------------------------------------------------------------


_io = [
    ("user_led"         , 0 , Pins("U16"), IOStandard("LVCMOS33")),
    ("user_led"         , 1 , Pins("E19"), IOStandard("LVCMOS33")),
    ("user_led"         , 2 , Pins("U19"), IOStandard("LVCMOS33")),
    ("user_led"         , 3 , Pins("V19"), IOStandard("LVCMOS33")),
    ("user_led"         , 4 , Pins("W18"), IOStandard("LVCMOS33")),
    ("user_led"         , 5 , Pins("U15"), IOStandard("LVCMOS33")),
    ("user_led"         , 6 , Pins("U14"), IOStandard("LVCMOS33")),
    ("user_led"         , 7 , Pins("V14"), IOStandard("LVCMOS33")),
    ("user_led"         , 8 , Pins("V13"), IOStandard("LVCMOS33")),
    ("user_led"         , 9 , Pins("V3" ), IOStandard("LVCMOS33")),
    ("user_led"         , 10, Pins("W3" ), IOStandard("LVCMOS33")),
    ("user_led"         , 11, Pins("U3" ), IOStandard("LVCMOS33")),
    ("user_led"         , 12, Pins("P3" ), IOStandard("LVCMOS33")),
    ("user_led"         , 13, Pins("N3" ), IOStandard("LVCMOS33")),
    ("user_led"         , 14, Pins("P1" ), IOStandard("LVCMOS33")),
    ("user_led"         , 15, Pins("L1" ), IOStandard("LVCMOS33")),
    ("user_sw"          , 0 , Pins("V17"), IOStandard("LVCMOS33")),
    ("user_sw"          , 1 , Pins("V16"), IOStandard("LVCMOS33")),
    ("user_sw"          , 2 , Pins("W16"), IOStandard("LVCMOS33")),
    ("user_sw"          , 3 , Pins("W17"), IOStandard("LVCMOS33")),
    ("user_sw"          , 4 , Pins("W15"), IOStandard("LVCMOS33")),
    ("user_sw"          , 5 , Pins("V15"), IOStandard("LVCMOS33")),
    ("user_sw"          , 6 , Pins("W14"), IOStandard("LVCMOS33")),
    ("user_sw"          , 7 , Pins("W13"), IOStandard("LVCMOS33")),
    ("user_sw"          , 8 , Pins("V2" ), IOStandard("LVCMOS33")),
    ("user_sw"          , 9 , Pins("T3" ), IOStandard("LVCMOS33")),
    ("user_sw"          , 10, Pins("T2" ), IOStandard("LVCMOS33")),
    ("user_sw"          , 11, Pins("R3" ), IOStandard("LVCMOS33")),
    ("user_sw"          , 12, Pins("W2" ), IOStandard("LVCMOS33")),
    ("user_sw"          , 13, Pins("U1" ), IOStandard("LVCMOS33")),
    ("user_sw"          , 14, Pins("T1" ), IOStandard("LVCMOS33")),
    ("user_sw"          , 15, Pins("R2" ), IOStandard("LVCMOS33")),    
    ("user_btn"         , 0 , Pins("T18"), IOStandard("LVCMOS33")),
    ("user_btn"         , 1 , Pins("W19"), IOStandard("LVCMOS33")),
    ("user_btn"         , 2 , Pins("T17"), IOStandard("LVCMOS33")),
    ("user_btn"         , 3 , Pins("U17"), IOStandard("LVCMOS33")),


    ("clk100", 0, Pins("W5"), IOStandard("LVCMOS33")),
    ("cpu_reset", 0, Pins("U18"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("tx", Pins("A18")),
        Subsignal("rx", Pins("B18")),
        IOStandard("LVCMOS33"),
    ),
]


## PLL/MMCM CLockGenerator
class _CRG(Module):
    def __init__(self, clk, rst=0, sys_clk_freq=125e6, in_clk_freq = 100e6):

        # Clock Domains:
        
        self.clock_domains.cd_sys = ClockDomain()
        self.clock_domains.cd_app1  = ClockDomain()
        

        # PLL Instance
        self.submodules.pll = pll = S7MMCM(speedgrade=-1)
        pll.register_clkin(clk, in_clk_freq)
        pll.create_clkout(self.cd_sys, sys_clk_freq,with_reset=False)
        pll.create_clkout(self.cd_app1, sys_clk_freq/10,with_reset=False)

        # Timing Constraints
        platform.add_period_constraint(self.cd_sys.clk, int(sys_clk_freq))
        platform.add_period_constraint(self.cd_app1.clk, int(sys_clk_freq/10))

        # Reset Connection to ClockDomain
        self.comb += [
            self.cd_sys.rst.eq(rst),
            self.cd_app1.rst.eq(rst)
        ]

# Platform -----------------------------------------------------------------------------------------


class Platform(XilinxPlatform):
    default_clk_name   = "clk100"
    default_clk_period = 1e9/100e6

    def __init__(self):
       XilinxPlatform.__init__(self, "xc7a35tcpg236-1", _io, toolchain="vivado")

# Create our platform (fpga interface)
platform = Platform()

platform.add_source("Hardware/gpio/gpio.v")
    
# Design -------------------------------------------------------------------------------------------


class BaseSoC(SoCCore):
    def __init__(self, platform):

        sys_clk_freq = 140e6 # Desired frequency with PLL/MMCM
        in_clk_freq = 100e6

        interrupt_map= {
            'GPIO': 7,
        }
        SoCCore.interrupt_map.update(interrupt_map)

        # SoC with CPU
        SoCCore.__init__(self, platform,
            cpu_type                 = "vexriscv",
            csr_data_width           = 32,
            clk_freq                 = sys_clk_freq,
            ident                    = "LiteX CPU Test SoC", ident_version=True,
            integrated_rom_size      = 0x8000,
            integrated_main_ram_size = 0x4000)

        # Clock Reset Generation
        
        # Reset Synchronizer without PLL
        #self.submodules.crg = CRG(platform.request("clk100"), platform.request("cpu_reset"))

        # Synchronizer with PLL
        self.submodules.crg = _CRG(platform.request("clk100"),platform.request("cpu_reset"), sys_clk_freq, in_clk_freq)
 


        # GPIO 
        gpio_leds = Cat(*[platform.request("user_led", i) for i in range(4)])
        gpio_sw = Cat(*[platform.request("user_sw", i) for i in range(4)])
        self.submodules.GPIO= gpio()
        self.add_csr("GPIO")
        self.comb += [
            self.GPIO.CLK.eq(ClockSignal()),
            self.GPIO.RST.eq(ResetSignal()),
            self.GPIO.SW.eq(gpio_sw),       # Entradas
            gpio_leds.eq(self.GPIO.LED)     # Salidas
        ]
            


def main():

    soc = BaseSoC(platform)
    # Build --------------------------------------------------------------------------------------------
    builder = Builder(soc, output_dir="build", csr_csv="memoryMap.csv", memory_x="memoryStructure.x", generate_doc="x.doc")
    builder.build(build_name="top")


if __name__ == "__main__":
    main()
