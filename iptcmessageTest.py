#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import iptcmessage
import unittest

TEST1 = b"\x01v2557 4 txx 613 1tvks\r\nAP-APTN-1330:BosniaMineR\r\n\x02^AP-APTN-1330: Bosnia Mine Rescue<\r\n^Friday, 5 September 2014<\r\n<\r\nSTORY:Bosnia Mine Rescue- Rescuers begin pulling trapped workers out of collapsed mine\r\nLENGTH: 03:31\t\r\nFIRST RUN: 1130\r\nRESTRICTIONS: AP Clients Only\r\nTYPE: Natsound\r\nSOURCE: AP TELEVISION\r\nSTORY NUMBER: 2021347\r\n\r\nDATELINE: Zenica - 5 Sept 2014\r\nLENGTH: 03:31\t\r\n\r\n\r\n\x08\x08RESTRICTION SUMMARY: AP CLIENTS ONLY\r\n\x08\x08\r\n\x08\x08SHOTLIST:\r\n\x08\x08\r\n\x08\x08AP TELEVISION - AP CLIENTS ONLY\r\n\x08\x081. Zoom into rescued miner being escorted from Raspotocje Mine by rescue workers\r\n\x08\x082. Ambulance workers carrying miner on a stretcher\r\n\x08\x083. Ambulance driving away\r\n\x08\x084. Miner being helped out and people greeting him\r\n\x08\x085. Miner being escorted out and pausing to retch \r\n\x08\x086. Miner being put on stretcher inside ambulance\r\n\x08\x087. Close of rescued mine inside ambulance\r\n\x08\x088. Various of medics attending to rescued miners \r\n\x08\x089. Ambulance driving away, pan to miner walking out and man hugging him\r\n\x08\x0810. Miner being helped to ambulance\r\n\x08\x0811. Miner on stretcher being carried by medics to ambulance\r\n\x08\x0812. Ambulance driving away\r\n\x08\x0813. Miner being escorted out, man hugging him, another miner being greeted\r\n\x08\x0814. Miner talking with associates\r\n\x08\x0815. Miner on stretcher being carried by medics to ambulance\r\n\x08\x0816. Miner being helped away\r\n\x08\x0817. Miner walking past TV crew\r\n\x08\x0818. Ambulance backing up, distraught woman looking towards mine\r\n\x08\x0819. Wide of police and onlookers outside mine entrance\r\n\x08\x08\r\n\x08\x08STORYLINE:\r\n\x08\x08\r\n\x08\x08Rescuers on Friday were pulling out some of the 34 miners who had been trapped deep inside a coal mine that collapsed in central Bosnia.\r\n\x08\x08\r\n\x08\x08Tired, their faces smeared with coal dust, the men came out of the Zenica mine one by one, after spending the night more than 500 metres (1,600 feet) below the ground.\r\n\x08\x08\r\n\x08\x08Many were met by anxious family members relieved to embrace their loved ones. \r\n\x08\x08\r\n\x08\x08Ambulances were parked outside the mine entrance to take the miners for medical examinations.\r\n\x08\x08\r\n\x08\x08More than two dozen emerged looking relatively well, but there was no firm information on the fate of those still in the mine.\r\n\x08\x08\r\n\x08\x08The union leader at the Zenica coal mine said two tunnels in the mine collapsed on Thursday evening following a gas explosion triggered by a minor earthquake that had hit the area near the town of Zenica.\r\n\x08\x08\r\n\x08\x08He said 22 other miners managed to leave the pit after the tunnels collapsed, two of whom were injured.\r\n\x08\x08\r\n\x08\x08The Zenica coal mine was the site of one of the greatest mining tragedies in Bosnia's history, when 39 miners were killed in a gas explosion in 1982.\r\n\x08\x08\r\n\x08\x08The latest incident was the third in the mine this year. \r\n\x08\x08\r\n\x08\x08A total of 16 miners were hurt in two previous gas explosions, the most recent less than four weeks ago.\r\n\x08\x08\r\n\x08\x08Families and the union leaders have accused the management of poor response to the accident, particularly in initially claiming that only eight people were trapped inside the pit.\r\n\x08\x08\r\n\x08\x08===========================================================\r\n\x08\x08\r\n\x08\x08Clients are reminded: \r\n\x08\x08(i) to check the terms of their licence agreements for use of content outside news programming and that further advice and assistance can be obtained from the AP Archive on: Tel +44 (0) 20 7482 7482 Email: info@aparchive.com\r\n\x08\x08(ii) they should check with the applicable collecting society in their Territory regarding the clearance of any sound recording or performance included within the AP Television News service \r\n\x08\x08(iii) they have editorial responsibility for the use of all and any content included within the AP Television News service and for libel, privacy, compliance and third party rights applicable to their Territory.\r\n\x08\x08\r\n\x08\x08\r\n\x08\x08\r\n\x08\x08\r\n\x08\x08\r\nAPTN\r\n\r\n\r\n\t   \x03050932 sep 14EDT\r\n\x04"

TEST2 = b'\x01v2572 4 txx 25 1tvbr\r\nAP-APTN-1400Entertainmen\r\n\x02^AP-APTN-1400 Entertainment Week Advisories-<\r\n^Friday, 5 September 2014<\r\n\r\n^Entertainment Week Advisories<\r\n\r\n\r\n\x08\r\n\x08B-u-l-l-e-t-i-n begins at 1400 GMT.\r\n\r\n\r\n\t   \x03050945 sep 14EDT\r\n\x04'

TEST3 = b'\x01v2595 4 txx 232 1tvkr\r\nAP-APTN-1330PrimeNews-Fi\r\n\x02^AP-APTN-1330 Prime News-Final<\r\n^Friday, 5 September 2014<\r\n\r\n^Prime News<\r\n\r\n++UK NATO 4 02:57 AP Clients Only\r\n^Reaction to NATO leaders decision to post several thousand troops in Eastern Europe<\r\n\r\nUK NATO 3 03:20 AP Clients Only\r\n^NATO chief announces formation of rapid reaction force<\r\n\r\n++Bosnia Mine 4 01:34 AP Clients Only\r\n^Mine official on rescued and missing miners; familes at mine<\r\n\r\nUkraine Donetsk 02:31 AP Clients Only\r\n^People of Donetsk not hopeful that ceasefire will happen<\r\n\r\nUkraine Mariupol 03:03 AP Clients Only\r\n^Fighting continuing around strategic port city, despite Minsk talks and hopes of ceasefire<\r\n\r\n++US Ebola 2 01:03 Access all outside North America/No Access Broadcast or Digital in North America\r\n^Infected missionary arrives at hospital in Nebraska for treatment<\r\n\r\nBosnia Mine Rescue 03:31 AP Clients Only\r\n^Rescuers begin pulling trapped workers out of collapsed mine<\r\n\r\nBosnia Mine 3 01:55 AP Clients Only\r\n^Injured miner tells of dramatic escape after gas explosion caused by quake<\r\n\r\nBelarus Talks 01:27 Part No Access Russia/EBU\r\n^Talks aimed at arranging a ceasefire in Ukraine get under way<\r\n\r\n++India Kashmir Flooding 2 02:00 AP Clients Only\r\n^Rescued residents and submerged houses in worst floods for years<\r\n\r\n++Bosnia Mine 5 02:30 AP Clients Only\r\n^Hospital spokesman comments on the condition of the rescued injured miners<\r\n\r\n\r\n\x08\r\n\x08B-u-l-l-e-t-i-n begins at 1330 GMT.\r\n\r\n\r\n\t   \x03051001 sep 14EDT\r\n\x04'

DPATEST = b'bdt0534 3 vm 144  dpa 2777\r\n\nVorschau/Tagesvorschau/dpa/Wissen/\r\n\x02(Vorschau)\nTerminvorschau sieben - Wissen\ndpa-Terminvorschau f\xfcr Sonntag, 07. September 2014 =\r\n\n---------------------------------------------------------------------\r\nAuf www.dpa-news.de bieten wir Ihnen einen laufend aktualisierten\r\n\xdcberblick \xfcber die dpa-Topthemen des Tages. Auch Ihre Fragen und\r\nAnregungen beantworten wir dort online. Die Planung f\xfcr die n\xe4chsten\r\n14 Tage finden Sie jederzeit auf dem aktuellen Stand auf\r\nwww.dpa-agenda.de.\r\n---------------------------------------------------------------------\r\nRedaktion Wissen \r\nTel.: +49 30 285232261; E-Mail: wissen@dpa.com\r\n---------------------------------------------------------------------\r\nThemen und Termine Wissen\r\n\nNairobi       -      Schmelzende Sch\xf6nheiten: Klimawandel bedroht\r\n                     Ostafrikas Gletscher (zum UN-Klimagipfel in New\r\n                     York am 23. September)\r\n                     Der Schnee des Kilimandscharo ist weltber\xfchmt -\r\n                     und vom Klimawandel bedroht. Ganze \xd6kosysteme\r\n                     sind von den Gletschern der Berge Ostafrikas\r\n                     abh\xe4ngig.\r\n                     - KORR-Bericht Wiederholung des KORR-Berichts\r\n                     vom Samstag, bis 1200, ca. 60 Zl.\r\n                     +++ Kenia/Klima/Umwelt;Wissenschaft/ +++\r\n\n* Weitere Termine voraussichtlich ohne Berichterstattung\r\n\nCascais       -      * Europ\xe4ischer Kongress \xfcber Weltallforschung\r\n                     und Raumfahrtwissenschaft (bis 12.09.2014)\r\n\nM\xfcnchen       - 1030 * Pk zur Er\xf6ffnung des Internationalen\r\n                     Kongresses der Lungenmediziner (bis 10.09.2014)\r\n                     mit Vorstellung der H\xf6hepunkte des Programms\r\n\n-------------------------------------------------------------------\r\n\ndpa kll yyzz s5 akn\r\n\r\n\x03051508 Sep 14\r\n\x7f\n\x7f'

class IPTCMessageTestCase(unittest.TestCase):

    def testMessageParsing(self):
        iptc = iptcmessage.IPTCMessage(DPATEST)
        self.assertGreater(iptc.length, 0)

if __name__=='__main__':
    unittest.main()


