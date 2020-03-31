-- Top module of the 6502 / RP2A03 / RP2A07 processor used in the NES

library ieee;
  use ieee.std_logic_1164.all;
  use ieee.numeric_std.all;

entity PROCESSOR is
  port (
    CLK            : in    std_logic;
    RST            : in    std_logic
  );
end entity PROCESSOR;

architecture BEHAVIOURAL of PROCESSOR is

begin

  TMP_PROC : process (clk) is
  begin

  end process TMP_PROC;

end architecture BEHAVIOURAL;
