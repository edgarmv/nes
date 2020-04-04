
library ieee;
  use ieee.std_logic_1164.all;
  use ieee.numeric_std.all;
  use work.common.all;

entity DECODE_ROM_TEST is
end entity DECODE_ROM_TEST;

architecture BEHAVIOUR of DECODE_ROM_TEST is

  signal ir     : std_logic_vector(7 downto 0);
  signal timing : type_timing_state;
  signal output : std_logic_vector(129 downto 0);

begin

  UUT: entity work.DECODE_ROM
    port map (
      IR      => ir,
      TIMING  => timing,
      OUTPUT  => output
    );

  TEST_PROC : process is

  begin

  ir      <= "10011011";
  wait for 10 ns;
  ir      <= "10011111";
  wait for 10 ns;
  ir      <= "10111011";
  timing  <= T2;
  wait for 10 ns;
  ir      <= "00010011";
  timing  <= T3;
  wait;

  end process TEST_PROC;

end architecture BEHAVIOUR;
