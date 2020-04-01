-- Top module of the 6502 / RP2A03 / RP2A07 processor used in the NES

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity PROCESSOR is
  port (
         CLK            : in    std_logic;
         nRST           : in    std_logic;
         AUDIO1         : out   std_logic; -- Pulse waves
         AUDIO2         : out   std_logic; -- Triangle, noise and DPCM
         ADDRESS_BUS    : out   std_logic_vector(15 downto 0);
         DATA_BUS       : inout std_logic_vector(7 downto 0);
         OUT0           : out   std_logic; -- Controller ports
         OUT1           : out   std_logic; -- Controller ports
         OUT2           : out   std_logic; -- Controller ports
         OE1            : out   std_logic; -- Controller 1 enable
         OE2            : out   std_logic; -- Controller 2 enable
         RW             : out   std_logic; -- Data bus read/write
         NMI            : in    std_logic;
         IRQ            : in    std_logic;
         M2             : out   std_logic -- "Signals ready"
       );
end entity PROCESSOR;

architecture BEHAVIOURAL of PROCESSOR is
begin

  reset_proc : process (CLK, nRST) is
  begin
  end process TMP_PROC;


end architecture BEHAVIOURAL;
