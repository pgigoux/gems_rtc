# gems_rtc

Gems RTC data processing programs and data

Programs:
* common.py     Common functions
* matrices.py   Process data matching a timestamp
* copy_data.py  Copy data from the RTC area into data

Data files:

* data/*20220928114409.txt Reconstructor files with all zeroes and loaded successfully to the RTC.

* data/*20221013112754.txt Reconstructor files generated writing half the data with 1's

* data/*20221013124112.txt Write directly to IRAM. SDRAM was all 0010 after read with diag21k

* data/*20221013124947.txt Write zero scrambled matrix to SDRAM. Display shows all zeroes.

* data/*20221013125844.txt Write 1's to IRAM, SDRAM was zero pre previous tests. SDRAM stays zero. 

* data/*20221013130313.txt Write 1's to SDRAM, memory dump shows 1's, data is corrupted on the display (part of dm0).

* data/*20221013131110.txt Write 5's to SDRAM, memory dump shows 5's, data is corrupted on the display (part of dm0).
