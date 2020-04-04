open_project build/NES.xpr

set errors [check_syntax -fileset sources_1 -return_string]

if {$errors != ""} {
    puts "$errors"
    exit
}

set errors [check_syntax -fileset sim_1 -return_string]

if {$errors != ""} {
    puts "$errors"
    exit
}


start_gui

launch_simulation
