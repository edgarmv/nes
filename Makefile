VHDL_FILES=CPU/Processor.vhdl

ENV_SETUP=source /opt/Xilinx/Vivado/2019.2/settings64.sh
VIVADO_ARGS=-mode batch

SIM_ARGS=-source scripts/sim.tcl -log logs/sim.log -jou logs/sim.jou
SETUP_ARGS=-source scripts/setup.tcl -log logs/setup.log -jou logs/setup.jou


sim:
	$(ENV_SETUP) && vivado $(VIVADO_ARGS) $(SIM_ARGS)

setup:
	$(ENV_SETUP) && vivado $(VIVADO_ARGS) $(SETUP_ARGS)
