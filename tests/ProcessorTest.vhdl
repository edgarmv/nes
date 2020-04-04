
library ieee;
  use ieee.std_logic_1164.all;

entity PROCESSORTEST is
end entity PROCESSORTEST;

architecture BEHAVIOUR of PROCESSORTEST is

  signal clk          : std_logic;
  signal nrst         : std_logic;
  signal audio1       : std_logic;
  signal audio2       : std_logic;
  signal address_bus  : std_logic_vector(15 downto 0);
  signal data_bus     : std_logic_vector(7 downto 0);
  signal out0         : std_logic;
  signal out1         : std_logic;
  signal out2         : std_logic;
  signal oe1          : std_logic;
  signal oe2          : std_logic;
  signal rw           : std_logic;
  signal nmi          : std_logic;
  signal irq          : std_logic;
  signal m2           : std_logic;

begin

  UUT: entity work.PROCESSOR
    port map (
      CLK         => clk,
      NRST        => nrst,
      AUDIO1      => audio1,
      AUDIO2      => audio2,
      ADDRESS_BUS => address_bus,
      DATA_BUS    => data_bus,
      OUT0        => out0,
      OUT1        => out1,
      OUT2        => out2,
      OE1         => oe1,
      OE2         => oe2,
      RW          => rw,
      NMI         => nmi,
      IRQ         => irq,
      M2          => m2
    );

  TEST_PROC : process is
  begin

  clk <= '0';
  wait for 20 ns;
  clk <= '1';
  wait for 40 ns;
  clk <= '0';

  end process TEST_PROC;

end architecture BEHAVIOUR;
