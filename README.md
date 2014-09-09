tty2NewsML
==========

Prerequisites
-------------

* Python 3
* PySerial
  * `yum install python-setuptools`
  * `easy_install pyserial`
  * or `pip install pyserial`


Communication parameters:
* 4800 baud
* 8 data bits
* no parity
* 1 stop bit

Format: [IPTC 7901](http://www.iptc.org/site/News_Exchange_Formats/IPTC_7901/Specification/)

Priorities
----------

* 5 - Normal
* 4 - Dringend
* 3 - Vorrang
* 2 - Blitz/Eil
