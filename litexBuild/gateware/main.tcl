
# Create Project

create_project -force -name main -part xc7a35tcpg236-1
set_msg_config -id {Common 17-55} -new_severity {Warning}

# Add Sources

read_verilog {/home/camilo/MEGA/RequerimientosLiteX/SoCTemplateLiteX/hardware/gpio/gpio.v}
read_verilog {/home/camilo/LiteX/pythondata-cpu-vexriscv/pythondata_cpu_vexriscv/verilog/VexRiscv.v}
read_verilog {/home/camilo/MEGA/RequerimientosLiteX/SoCTemplateLiteX/litexBuild/gateware/main.v}

# Add EDIFs


# Add IPs


# Add constraints

read_xdc main.xdc
set_property PROCESSING_ORDER EARLY [get_files main.xdc]

# Add pre-synthesis commands


# Synthesis

synth_design -directive default -top main -part xc7a35tcpg236-1

# Synthesis report

report_timing_summary -file main_timing_synth.rpt
report_utilization -hierarchical -file main_utilization_hierarchical_synth.rpt
report_utilization -file main_utilization_synth.rpt

# Optimize design

opt_design -directive default

# Add pre-placement commands


# Placement

place_design -directive default

# Placement report

report_utilization -hierarchical -file main_utilization_hierarchical_place.rpt
report_utilization -file main_utilization_place.rpt
report_io -file main_io.rpt
report_control_sets -verbose -file main_control_sets.rpt
report_clock_utilization -file main_clock_utilization.rpt

# Add pre-routing commands


# Routing

route_design -directive default
phys_opt_design -directive default
write_checkpoint -force main_route.dcp

# Routing report

report_timing_summary -no_header -no_detailed_paths
report_route_status -file main_route_status.rpt
report_drc -file main_drc.rpt
report_timing_summary -datasheet -max_paths 10 -file main_timing.rpt
report_power -file main_power.rpt

# Bitstream generation

write_bitstream -force main.bit 

# End

quit