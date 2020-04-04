-- 21x130 Decode ROM

library ieee;
  use ieee.std_logic_1164.all;
  use ieee.numeric_std.all;
  use work.common.all;

entity DECODE_ROM is
  port (
    IR      : in    std_logic_vector(7 downto 0);
    TIMING  : in    TYPE_TIMING_STATE;
    OUTPUT  : out   std_logic_vector(129 downto 0)
  );
end entity DECODE_ROM;

architecture BEHAVIOURAL of DECODE_ROM is

begin

  OUTPUT(PLA_STY)      <= '1' when std_match(IR, "100--1--")                 else '0';
  OUTPUT(PLA_OP_IND_Y) <= '1' when std_match(IR, "---100-1") and TIMING = T3 else '0';
  OUTPUT(PLA_OP_ABS_Y) <= '1' when std_match(IR, "---110-1") and TIMING = T2 else '0';

end architecture BEHAVIOURAL;
