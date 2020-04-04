
library ieee;
  use ieee.std_logic_1164.all;
  use ieee.numeric_std.all;

package COMMON is

  constant pla_sty      : natural := 0;
  constant pla_op_ind_y : natural := 1;
  constant pla_op_abs_y : natural := 2;

  type type_timing_state is (T0, T1, T2, T3, T4, T5);

end package COMMON;
