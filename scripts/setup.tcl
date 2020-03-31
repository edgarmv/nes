set part xc7k70tfbv676-1
set outputdir build

create_project -part $part -force NES $outputdir

set obj [get_projects NES]
set_property "simulator_language" "Mixed" $obj
set_property "target_language" "VHDL" $obj

add_files -fileset sources_1 [glob CPU/*.vhdl]
add_files -fileset sim_1 [glob tests/*.vhdl]

update_compile_order -fileset sources_1

set_property top PROCESSOR [get_filesets sources_1]
set_property top ProcessorTest [get_filesets sim_1]

update_compile_order -fileset sources_1
update_compile_order -fileset sim_1
