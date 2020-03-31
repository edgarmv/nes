
library ieee;
  use ieee.std_logic_1164.all;

entity PROCESSORTEST is
end entity PROCESSORTEST;

architecture BEHAVIOUR of PROCESSORTEST is

  signal clk, rst : std_logic;

begin

  UUT: entity work.PROCESSOR
    port map (
      CLK => clk,
      RST => clk
    );

  clk <= '0';
  wait 20 ns;
  clk <= '1';
  wait 40 ns;
  clk <= '0';

end architecture BEHAVIOUR;
