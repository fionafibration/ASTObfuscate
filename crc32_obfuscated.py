O1l1l000OO10lO1Ol0001 = lambda Oll0OO11110OO0llOOl1l: ~Oll0OO11110OO0llOOl1l
OO1OO0O10l1l10Ol1O10l = lambda l1l11lO1lO0OOOll11l00: not l1l11lO1lO0OOOll11l00
O110l00l0lO0000OO1llO = (lambda lllllO10l001O1110l000,
    l11l00lO001l11l0l0l0O: lllllO10l001O1110l000 * l11l00lO001l11l0l0l0O)
l1Oll111O0l1OOll00OOO = (lambda O0lOl0001l1O01100OO1l,
    l11O0OOl00OlO00l0lO0O: O0lOl0001l1O01100OO1l % l11O0OOl00OlO00l0lO0O)
OllllO11lO01OlOllOl11 = (lambda l1lOlO1lO0Ol010O101ll,
    lO011OO0lO1ll1ll1111O: l1lOlO1lO0Ol010O101ll + lO011OO0lO1ll1ll1111O)
OlOlO1000llOl1OllO010 = (lambda l10OOl1100l011l110101,
    l1llOllll10O1100l0OO1: l10OOl1100l011l110101 ^ l1llOllll10O1100l0OO1)
OOOOll11l11O00lO110l0 = (lambda l0lOl10O0Ol1011l100l0,
    l0OO0l0ll1l101O1ll000: l0lOl10O0Ol1011l100l0 | l0OO0l0ll1l101O1ll000)
OO110O0lOl1l10l11010l = (lambda ll10l01O11lO01ll1lO10,
    l0l0O011O1llOlO1lOl1O: ll10l01O11lO01ll1lO10 >> l0l0O011O1llOlO1lOl1O)
lO000O1l00ll0l0OO0l00 = (lambda Ol00011101lOO0O01011O,
    Oll010O0lOOll1001O010: Ol00011101lOO0O01011O & Oll010O0lOOll1001O010)


def flag_check(buf):
 if OO1OO0O10l1l10Ol1O10l(getattr(buf, OllllO11lO01OlOllOl11(''.join(filter
     (lambda l1Ol1l0O10Ol01lO1101O: ord(l1Ol1l0O10Ol01lO1101O) % 6 != 0,
     '$\x00\x0cT<*\x0c`\x0c*0\x18`\x18\x0c')).join(chr(
     l0lOl01101110l001ll0O ^ l01O01lll111OOl1O1lO1) for 
     l01O01lll111OOl1O1lO1, l0lOl01101110l001ll0O in zip(b'_4e;\x04',
     b'+F\x04Ow'))[::OllllO11lO01OlOllOl11((-1 ^ 0) * (2 ^ 1), 1 ^ 0) ^ (0 ^
     1 ^ 0)], ''.join(chr(O0l11llOl01l1100l01OO ^ lOll00l0O1010O0O100O1) for
     lOll00l0O1010O0O100O1, O0l11llOl01l1100l01OO in zip(b'\xe9#0\x86\xcd',
     b'\x9aTY\xf2\xa5'))[::-1 ^ 0][::O110l00l0lO0000OO1llO(-1 * (3 ^ 5) + (
     0 ^ 5), 0 * (0 ^ 5) + (4 ^ 0)) + (0 * 4 + 3)]))(bytes(''.join(chr(
     OlOlO1000llOl1OllO010(O10l0l01O1O0lO1000010, l11l10OOlO0O1Ol0l1llO)) for
     l11l10OOlO0O1Ol0l1llO, O10l0l01O1O0lO1000010 in zip(
     b'YGdh\xe6\xe3\xe7L\x8eW&\xd7\x10',
     b'\x1f\x0b%/\xb9\xa0\xa6\x1c\xda\x02t\x92O')), encoding=''.join(filter
     (lambda O0l0l0lOl01O001OO1l1O: l1Oll111O0l1OOll00OOO(ord(
     O0l0l0lOl01O001OO1l1O), OllllO11lO01OlOllOl11(0 *
     OllllO11lO01OlOllOl11(0 * (1 * 6 + 0), 4), 0 ^ 2) ^
     OllllO11lO01OlOllOl11(0 * (3 ^ 0), 0)) != OllllO11lO01OlOllOl11(
     O110l00l0lO0000OO1llO(OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(0, 2 ^
     6), 0), 0 ^ 1 ^ (0 ^ 2) ^ 0), OllllO11lO01OlOllOl11(0 *
     OllllO11lO01OlOllOl11(0 * 5, 1 * 4 + 0), 0 * (0 * 5 + 3) + 0)),
     'l:6Jj\\\x12V\x0e\x1c 22B>')).join(chr(OlOlO1000llOl1OllO010(
     ll101OOl11011100100Ol, l11OOll011OO00l1OO0l0)) for 
     l11OOll011OO00l1OO0l0, ll101OOl11011100100Ol in zip(
     b'\xa6\xe1\r\xd7\xf9', b'\xd3\x95k\xfa\xc1'))))):
  return l1Oll111O0l1OOll00OOO(OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(
      O110l00l0lO0000OO1llO(1 * 3 + 0, 0 * 5 + 1 ^ (1 ^ 3)) + (0 ^ 1), 7 ^ 
      1), 0 * (3 * 2 + 0) + (0 * 5 + (0 * 6 + 4))), (0 * 6 + 2) * (0 ^ 4) +
      (1 ^ 0) ^ OllllO11lO01OlOllOl11((0 * 6 + 1) * (1 ^ 4), 1 ^ 0)
      ) == OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(
      O110l00l0lO0000OO1llO(0 * 2 + 0, 6 ^ 0) + (0 * 3 + 0),
      OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(0 ^ (0 ^ 1), 0 * 6 + 2),
      OllllO11lO01OlOllOl11((0 * 4 + 0) * (O110l00l0lO0000OO1llO(0, 3 ^ 6) +
      (4 ^ 0)), 0))), O110l00l0lO0000OO1llO(0, 5 ^ 0) + 0)
 OO0O000l000Ol0O0l11lO = OlOlO1000llOl1OllO010(OllllO11lO01OlOllOl11(
     O110l00l0lO0000OO1llO(OlOlO1000llOl1OllO010(532811983 ^ 122315104, 
     108000957 ^ 17032445), (0 * 4 + 1) * OlOlO1000llOl1OllO010(3, 0 * 5 + 
     1) + (O110l00l0lO0000OO1llO(0, 5) + 1)), 2), OlOlO1000llOl1OllO010(
     OlOlO1000llOl1OllO010(OllllO11lO01OlOllOl11((194756005 * 6 + 4) * 3, 2
     ), 379815885), OlOlO1000llOl1OllO010(O110l00l0lO0000OO1llO(84742958 * 
     2 + 1, 1 * 4 + 0) + (0 * 5 + 2), 328902600 * 4 + 3)))
 lO1l0l00l0l1l0Ol1l11O = []
 for lO0OOlO1111Ol1O1O0O1l in range(OllllO11lO01OlOllOl11(
     O110l00l0lO0000OO1llO(O110l00l0lO0000OO1llO(21 ^ 2, 1 ^ 2) + (1 ^ 0) ^
     (0 * 4 + 0 ^ 1 * 6 + 0), OlOlO1000llOl1OllO010(0 * 6 + 3 ^ (0 ^ 5) ^ (
     0 * 2 + 1 ^ 1 * 3 + 0), 0)), 0)):
  O1ll001101O1ll0ll11lO = lO0OOlO1111Ol1O1O0O1l
  for O0Ol1l0l1011O00l011Ol in range(OllllO11lO01OlOllOl11(
      OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(OllllO11lO01OlOllOl11(
      O110l00l0lO0000OO1llO(0 * 6 + 0, 4 ^ 1), 0), 2), 0 ^
      OllllO11lO01OlOllOl11((0 * 4 + 0) * (2 ^ 4), 1 ^ 0)) *
      OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(OllllO11lO01OlOllOl11(0 *
      (0 * 4 + 2), 0) ^ 0 * (1 * 5 + 2 ^ 3) + (0 * 6 + 1 ^ 0),
      OlOlO1000llOl1OllO010(5, 0)), 0), OllllO11lO01OlOllOl11(
      OlOlO1000llOl1OllO010(0 * 2 + 1, 0) * (0 * 4 + 3), 0))):
   if lO000O1l00ll0l0OO0l00(O1ll001101O1ll0ll11lO, OllllO11lO01OlOllOl11(
       OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(OllllO11lO01OlOllOl11(0 *
       OllllO11lO01OlOllOl11(1 * (0 * 4 + 2), 0 * 5 + 1), 0),
       OllllO11lO01OlOllOl11(OllllO11lO01OlOllOl11(0 * (2 ^ 7), 0 * 6 + 3) *
       OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(0, 6 ^ 0), 0 ^ 2), 0 * 3 +
       0)), OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(0, (0 * 5 + 1) * (1 *
       3 + 1) + 0 ^ (0 * 2 + 1 ^ 0)), OllllO11lO01OlOllOl11(((0 * 4 + 0) *
       (1 * 3 + 2) + 0) * (4 ^ 1), 0 * 4 + 0))) * OlOlO1000llOl1OllO010(0, 
       2 ^ 1), OlOlO1000llOl1OllO010(0 * 2 + 0, 0 * (0 * 4 + 2) + (0 ^ 1)))):
    O1ll001101O1ll0ll11lO = lO000O1l00ll0l0OO0l00(O1l1l000OO10lO1Ol0001(
        lO000O1l00ll0l0OO0l00(O1ll001101O1ll0ll11lO, OlOlO1000llOl1OllO010(
        OllllO11lO01OlOllOl11((72067588 * (1 ^ 4) + (3 ^ 7)) *
        OlOlO1000llOl1OllO010(5, 0 ^ 1), 2 ^ 0), OlOlO1000llOl1OllO010(
        7368583 * 4 + 1 ^ 42073356 ^ (56835697 ^ 27846324 ^ 128097447),
        OlOlO1000llOl1OllO010(20959527 * 3 + 1, 228417188 ^ 49608730))) * (
        OlOlO1000llOl1OllO010(7 ^ 0, 0) ^ (OllllO11lO01OlOllOl11(
        O110l00l0lO0000OO1llO(0 * 5 + 0, 1 ^ 3), 0 ^ 1) ^
        OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(0, 1 * 2 + 1 ^ (1 ^ 7)),
        0 * 4 + 3))) + (0 ^ 1 ^ 0 ^ (0 ^ 1 ^ (3 ^ 0)) ^ 0 * (1 * 2 + 1) + (
        0 * 6 + 0)))), O1l1l000OO10lO1Ol0001(lO000O1l00ll0l0OO0l00(
        O1l1l000OO10lO1Ol0001(O1ll001101O1ll0ll11lO), O1l1l000OO10lO1Ol0001
        (OlOlO1000llOl1OllO010(262227893 * 5 + 0 ^ 5444974552 ^ (111906984 *
        4 + 1) * (2 ^ 1) + (0 ^ 2), OlOlO1000llOl1OllO010((128940633 * 3 + 
        0) * (1 * 4 + 0) + (1 ^ 0), 3723472089))))))
   O1ll001101O1ll0ll11lO = OO110O0lOl1l10l11010l(O1ll001101O1ll0ll11lO, 
       OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO((0 * 4 + 0) * 5 + 0, 
       O110l00l0lO0000OO1llO(OlOlO1000llOl1OllO010(0 * 4 + 0, 1 ^ 0 ^ 0 * 2 +
       0), 1 ^ 4) + (0 * 4 + 1 ^ 0 * 4 + 0)), (0 * 3 + 0) * ((1 ^ 0) * 4 + 
       0) + 0) ^ OlOlO1000llOl1OllO010(O110l00l0lO0000OO1llO(
       OllllO11lO01OlOllOl11(0 * 2, 0), OllllO11lO01OlOllOl11(0 * (1 * 5 + 
       1), 2 ^ 1)) + OlOlO1000llOl1OllO010(0, 0 * (0 * 5 + 3) + (0 * 3 + 1)
       ), 0 * OllllO11lO01OlOllOl11((1 ^ 0) * (0 ^ 4), 0 * 5 + 2) + ((0 * 2 +
       0) * 4 + 0)))
  getattr(lO1l0l00l0l1l0Ol1l11O, OllllO11lO01OlOllOl11(''.join(filter(lambda
      O001l0OO0O0O1ll10OOl0: l1Oll111O0l1OOll00OOO(ord(
      O001l0OO0O0O1ll10OOl0), 1 * 4 + 2) != 0 * 4 + 0,
      'lf<$<\x18T`Z``N\x06\x06$')).join(chr(OOO100O10l110000O0l10 ^
      l1O0ll0O0011lO00l10OO) for l1O0ll0O0011lO00l10OO,
      OOO100O10l110000O0l10 in zip(b'\xfb\x00\xcc', b'\x9ap\xbc')), ''.join
      (filter(lambda lll01lO1OO01l001OlOO0: ord(lll01lO1OO01l001OlOO0) % 6 !=
      0, 'ZH\x18\x18\x12\x12rNr\x06\x00x`NH')).join(filter(lambda
      l0O01l1lOlOO00lOlll0l: ord(l0O01l1lOlOO00lOlll0l) % 5 != 0,
      '#ZK#}\x00\x1eU#\x14\x00\x00}iF')).join(chr(OlOlO1000llOl1OllO010(
      ll00O001OOlOlOllOO1O1, Oll10O011llO1000OlO0O)) for 
      Oll10O011llO1000OlO0O, ll00O001OOlOlOllOO1O1 in zip(b'\xb3\x92\x1d',
      b'\xd6\xfcy'))))(O1ll001101O1ll0ll11lO)
 for OOl0100O0O11ll0OllOOl in buf:
  OO0O000l000Ol0O0l11lO = OlOlO1000llOl1OllO010(OO110O0lOl1l10l11010l(
      OO0O000l000Ol0O0l11lO, OllllO11lO01OlOllOl11(OllllO11lO01OlOllOl11(
      O110l00l0lO0000OO1llO(O110l00l0lO0000OO1llO(OllllO11lO01OlOllOl11((0 *
      6 + 0) * (2 * 2 + 0), 0), OllllO11lO01OlOllOl11((1 ^ 0) * (5 ^ 1),
      OllllO11lO01OlOllOl11((0 * 3 + 0) * 4, 0))) + (O110l00l0lO0000OO1llO(
      0, 2) + 0), OlOlO1000llOl1OllO010(3, 0 * 4 + 0 ^ 1)),
      OllllO11lO01OlOllOl11((0 * (1 * 3 + 0) + (0 * 3 + 0)) * (5 ^ 2 ^ 3), 
      O110l00l0lO0000OO1llO(0, 4 ^ 2) + 1)) * OlOlO1000llOl1OllO010(0 * 5 +
      0 ^ (0 ^ 1) ^ 0 * (1 * 3 + 0) + 0, OlOlO1000llOl1OllO010(2 * (0 ^ 2) +
      0, 0 * (2 ^ 7) + 0)), (0 * 2 + 0) * (OlOlO1000llOl1OllO010(3 ^ 4, 1 ^
      0 * 6 + 2) ^ (0 * 5 + 0) * ((0 ^ 1) * (1 * 5 + 0) + 0) + (1 ^ 2 ^ 0 *
      5 + 1)) + (OllllO11lO01OlOllOl11(0 * (0 * 4 + 2), 1 ^ 0) *
      OlOlO1000llOl1OllO010(1 ^ 2, 0 * (2 ^ 0) + (1 ^ 0)) + (
      OllllO11lO01OlOllOl11((0 * 6 + 0) * (2 * 3 + 0), 0) ^ 0 * 2 + 1)))),
      lO1l0l00l0l1l0Ol1l11O[OOOOll11l11O00lO110l0(lO000O1l00ll0l0OO0l00(
      O1l1l000OO10lO1Ol0001(O1l1l000OO10lO1Ol0001(lO000O1l00ll0l0OO0l00(
      O1l1l000OO10lO1Ol0001(lO000O1l00ll0l0OO0l00(OO0O000l000Ol0O0l11lO,
      OlOlO1000llOl1OllO010(OlOlO1000llOl1OllO010(OllllO11lO01OlOllOl11(
      OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(0 ^ 7, 0 * 6 + 2), 0 * 5 +
      1) * (O110l00l0lO0000OO1llO(0 ^ 2 ^ 0, 0 * 6 + (2 ^ 0)) + (0 ^ 1 ^ 0)
      ), 2 ^ 6), 0 * 4 + 0 ^ (0 ^ 1) ^ (0 * 6 + 0) * 6 + (2 * 2 + 1) ^ 
      O110l00l0lO0000OO1llO(77 ^ 3 * 5 + 0, 0 * 6 + 2) + (0 * 5 + 0 ^ 0 * 3 +
      1)), OlOlO1000llOl1OllO010(OllllO11lO01OlOllOl11(
      O110l00l0lO0000OO1llO(OlOlO1000llOl1OllO010(1, OlOlO1000llOl1OllO010(
      1 * 3 + 2, 0 * 6 + 0)), 1 ^ 0 ^ 3), 0 * 6 + 0), O110l00l0lO0000OO1llO
      (9, 5 ^ 3) + 3)))), O1l1l000OO10lO1Ol0001(lO000O1l00ll0l0OO0l00(
      OO0O000l000Ol0O0l11lO, OlOlO1000llOl1OllO010(O110l00l0lO0000OO1llO(
      OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(4 ^ 0, 0 * (7 ^ 1) +
      OlOlO1000llOl1OllO010(1 ^ 2, 0)), OlOlO1000llOl1OllO010(0 ^ (0 ^ 1),
      OllllO11lO01OlOllOl11(0 * (1 * 3 + 0), 0 * 6 + 0))),
      OlOlO1000llOl1OllO010(OllllO11lO01OlOllOl11(0 * (2 ^ 6), 2), 0 * 3 + 
      0)) + OlOlO1000llOl1OllO010(0, 1 ^ 0), O110l00l0lO0000OO1llO(
      OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(22, OllllO11lO01OlOllOl11
      ((0 * 6 + 0) * (2 * 2 + 0), 2)), (O110l00l0lO0000OO1llO(0 * 2 + 0, 1 *
      4 + 0) + (0 * 2 + 0)) * (2 ^ 1 ^ 1 * 5 + 2) + (O110l00l0lO0000OO1llO(
      0, 1 * 2 + 1) + (0 ^ 1))), OllllO11lO01OlOllOl11(
      O110l00l0lO0000OO1llO(OllllO11lO01OlOllOl11(0 * (1 * 6 + 0), 0 * 2 + 
      0) * (1 * 3 + 0 ^ 1 * 4 + 1) + OllllO11lO01OlOllOl11(0 * (1 ^ 4), 0),
      OlOlO1000llOl1OllO010((0 * 5 + 2) * 2 + (0 * 5 + 0), 0 * (2 * 3 + 0) +
      2)), O110l00l0lO0000OO1llO(1 ^ 0, 0 ^ 0 * 5 + 3) + (0 ^ 3 ^ 1))) +
      OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(O110l00l0lO0000OO1llO(0 *
      3 + 0, 3) + (0 ^ 1), (1 ^ 0) * (O110l00l0lO0000OO1llO(0 * 4 + 0, 1 ^ 
      7) + (0 ^ 2)) + ((0 * 6 + 0) * 4 + 0)), OllllO11lO01OlOllOl11(0 * (1 ^
      3), 0 * (1 * 3 + 0) + (0 * 3 + 1))))))))), OOl0100O0O11ll0OllOOl), 
      O1l1l000OO10lO1Ol0001(lO000O1l00ll0l0OO0l00(O1l1l000OO10lO1Ol0001(
      lO000O1l00ll0l0OO0l00(OO0O000l000Ol0O0l11lO, OllllO11lO01OlOllOl11(
      O110l00l0lO0000OO1llO(9 * 3 + 0, 7 ^ 1), 0 * 3 + 0) ^ (
      O110l00l0lO0000OO1llO(0 ^ 9, 1 ^ 3) + (1 ^ 0) ^ (22 ^ 17 * 5 + 3)))),
      O1l1l000OO10lO1Ol0001(OO0O000l000Ol0O0l11lO & OlOlO1000llOl1OllO010(
      OlOlO1000llOl1OllO010(OlOlO1000llOl1OllO010(22 ^ (0 * 3 + 0 ^ 3 * 4 +
      3), 5 ^ (12 ^ 41)), OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(4 ^ 0 ^
      12 ^ O110l00l0lO0000OO1llO(0, 5) + (0 * 4 + 3), OllllO11lO01OlOllOl11
      (O110l00l0lO0000OO1llO(OlOlO1000llOl1OllO010(0 * 5 + 1, 0 * 5 + 0), 0 *
      3 + 2 ^ 0), 0 * 6 + 0)), 0)), OlOlO1000llOl1OllO010(
      OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(23, 1 * 3 + 1), 
      O110l00l0lO0000OO1llO(0, 2 ^ 4) + 3), 6 ^ 24 ^ 113 ^ (5 ^ 32) * (0 ^ 
      6) + (2 ^ 0)))))) & O1l1l000OO10lO1Ol0001(OOl0100O0O11ll0OllOOl))])
 OO0O000l000Ol0O0l11lO = OlOlO1000llOl1OllO010(OO0O000l000Ol0O0l11lO, 
     O110l00l0lO0000OO1llO(OlOlO1000llOl1OllO010(OllllO11lO01OlOllOl11(
     O110l00l0lO0000OO1llO(5234349 * 3 + 0, 4), 0 * 4 + 3) ^ 75699197 * 6 +
     5 ^ (314185190 ^ 621363469), OlOlO1000llOl1OllO010(492994506,
     OlOlO1000llOl1OllO010(2124804 * 3 + 2 ^ (11266942 ^ 6061299), 12115665 ^
     (9445616 ^ 32518748)))), OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(0 ^
     OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(0 * 3 + 0, 1 * 2 + 1 ^ 7),
     1), 4), OlOlO1000llOl1OllO010(OllllO11lO01OlOllOl11(0 * 5, 0 * 2 + 1),
     0))) + OllllO11lO01OlOllOl11(OllllO11lO01OlOllOl11(
     OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(0, 5 ^ 0), 0 * 3 + 0) * (2 ^
     (3 ^ 7)), 0 * 6 + (0 * 4 + 0)) * OlOlO1000llOl1OllO010(3 ^ 0, 0), 0))
 return OlOlO1000llOl1OllO010(OllllO11lO01OlOllOl11(OOOOll11l11O00lO110l0(
     OllllO11lO01OlOllOl11(OO0O000l000Ol0O0l11lO ^ O110l00l0lO0000OO1llO(
     OlOlO1000llOl1OllO010(OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(
     OlOlO1000llOl1OllO010(59849879, 1339708 ^ 32172652), (0 ^ 2) * (0 * 4 +
     2) + (0 * 4 + 0)), 0 * 6 + 0), OllllO11lO01OlOllOl11(((80960830 ^ 
     48189664) * (1 ^ 4) + 0) * (0 * 4 + (0 * 3 + 2)), 0 * 2 + 0)),
     OlOlO1000llOl1OllO010(O110l00l0lO0000OO1llO(0, 6) +
     OllllO11lO01OlOllOl11(1 * (1 ^ 3), 1), OllllO11lO01OlOllOl11(
     O110l00l0lO0000OO1llO((0 * 4 + 0) * (3 ^ 6) + 0, (0 * 3 + 2) * 3 + 0),
     0 * 3 + 0))) + (O110l00l0lO0000OO1llO(0, 2 ^ 4) + 0),
     OllllO11lO01OlOllOl11(OllllO11lO01OlOllOl11(0 * (3 ^ 0), 0) *
     OllllO11lO01OlOllOl11((0 * 2 + (1 ^ 0)) * ((0 * 5 + 0) * 4 + (1 * 2 + 
     0)), 0 * 5 + 0), OlOlO1000llOl1OllO010(0 ^ 1, 0))) &
     O1l1l000OO10lO1Ol0001(OO0O000l000Ol0O0l11lO ^ OllllO11lO01OlOllOl11(
     O110l00l0lO0000OO1llO(OllllO11lO01OlOllOl11(OllllO11lO01OlOllOl11(
     O110l00l0lO0000OO1llO(O110l00l0lO0000OO1llO(OlOlO1000llOl1OllO010(
     13123650, 592232 * 5 + 1), 1 * 4 + 1) + (0 * 3 + 2), (1 ^ 0) * 2 + 1),
     OlOlO1000llOl1OllO010(0 * 2 + 0, 1 ^ 0)) * ((O110l00l0lO0000OO1llO(0, 
     5 ^ 1) + (0 ^ 1)) * (1 ^ 0 * 4 + 2) + (O110l00l0lO0000OO1llO(
     OllllO11lO01OlOllOl11(0 * (1 * 5 + 0), 0), 1 ^ 0 ^ 0 * 4 + 2) + (0 * 4 +
     1))), 0 * 2 + 0), O110l00l0lO0000OO1llO(0, OlOlO1000llOl1OllO010(2 * (
     2 ^ 0) + 0, 0)) + 0 ^ OlOlO1000llOl1OllO010(O110l00l0lO0000OO1llO(0, 0 *
     6 + 4) + 1, 1 ^ 3)), O110l00l0lO0000OO1llO(0, OllllO11lO01OlOllOl11(
     O110l00l0lO0000OO1llO(O110l00l0lO0000OO1llO(0, 6 ^ 3) + (0 ^ 1), 3), 0 *
     3 + 0)) + (O110l00l0lO0000OO1llO(0, 7 ^ 1) + 0))), 
     O110l00l0lO0000OO1llO(((22537789 * 3 + 1) * ((0 * 4 + 1) * (2 ^ 0) + (
     0 * 6 + 0)) + 0) * (0 ^ 1 ^ 1 * 3 + 1 ^ 0 * 5 + 1) + (0 ^
     OllllO11lO01OlOllOl11(0 * (1 * 5 + 1), 0 ^ 1)), OlOlO1000llOl1OllO010(
     0 * (0 ^ 1 ^ (0 ^ 0 * 5 + 2)) + (0 * 3 + 2), O110l00l0lO0000OO1llO(0 *
     2 + 0, OllllO11lO01OlOllOl11((0 * 3 + 0) * (0 * 6 + 4), 3)) + (0 * 6 +
     0))) + (0 * (3 ^ 5) + (0 * 6 + 0))), lO000O1l00ll0l0OO0l00(
     O1l1l000OO10lO1Ol0001(lO000O1l00ll0l0OO0l00(OllllO11lO01OlOllOl11(
     OlOlO1000llOl1OllO010(OO0O000l000Ol0O0l11lO, ((22052184 * 2 + 0) * 6 +
     (0 * 6 + 5) ^ (83418512 * 6 + 5 ^ 15157942)) * (0 ^ 1 * 5 + 0) + (0 * 
     3 + 2) ^ OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO((85737199 * 2 + 0
     ) * (3 ^ 6) + (3 ^ 0), (0 * 6 + 1) * (1 ^ 4) + 0), (
     O110l00l0lO0000OO1llO(0, 0 * 6 + 4) + 0) * (0 * 5 + 2 ^ (2 ^ 6)) + (0 *
     (4 ^ 2) + (1 ^ 2)))), OlOlO1000llOl1OllO010(OllllO11lO01OlOllOl11(
     OllllO11lO01OlOllOl11(OllllO11lO01OlOllOl11(0 * 6, 0) * (2 ^ 7 ^ 0),
     OllllO11lO01OlOllOl11(0 * (1 * 6 + 0), 0)) * (OlOlO1000llOl1OllO010((0 *
     6 + 1) * (0 * 4 + 2) + (0 * 4 + 1), 0) ^ OllllO11lO01OlOllOl11(
     O110l00l0lO0000OO1llO(OlOlO1000llOl1OllO010(1, 0 * 5 + 0), 7 ^ 1), 0 *
     (3 * 2 + 0) + (0 * 2 + 0))), O110l00l0lO0000OO1llO(0 * 6 + 0, 1 * 4 + 
     1) + (0 * 6 + 1)), 0)), O1l1l000OO10lO1Ol0001(OlOlO1000llOl1OllO010(
     OO0O000l000Ol0O0l11lO, OlOlO1000llOl1OllO010(OlOlO1000llOl1OllO010((
     71358549 * 6 + 4) * (1 ^ 3) + 0, O110l00l0lO0000OO1llO(100535680 ^ 
     60315405 ^ 126361865 * 3 + 1, OlOlO1000llOl1OllO010(0 ^ 3, 5)) + 5), (
     773889970 ^ 531207083) * (6 ^ 3) + (0 * 5 + 2)))))),
     OllllO11lO01OlOllOl11(OlOlO1000llOl1OllO010(OllllO11lO01OlOllOl11(
     O110l00l0lO0000OO1llO(OlOlO1000llOl1OllO010(OlOlO1000llOl1OllO010(
     6430941 * 5 + 3, 46099246), 8324543 * 4 + 3), (0 ^ 1 ^ 0 * 3 + 0) * (1 *
     3 + 0 ^ 0) + (O110l00l0lO0000OO1llO(0 * 3 + 1, 2) + (0 * 3 + 0))),
     OlOlO1000llOl1OllO010(0, 3)), O110l00l0lO0000OO1llO(9018291, 3 ^ 0 * 3 +
     1 ^ (0 * 6 + 4 ^ (2 ^ 1))) + (O110l00l0lO0000OO1llO((0 * 5 + 0) * (1 *
     6 + 0) + 2, 0 * 6 + 2) + 0)) * OlOlO1000llOl1OllO010(
     OlOlO1000llOl1OllO010(0 * 2 + (0 * 4 + 0), 0 ^ 1),
     OllllO11lO01OlOllOl11((0 ^ 1) * (1 ^ 2), 1 ^ 3)), (0 * 4 + 0) * 5 + 1 ^
     0 * 3 + 0))), O110l00l0lO0000OO1llO((143124424 * (1 * 2 + 0) + 0) * 5 +
     OlOlO1000llOl1OllO010(0 * 4 + 3, 1), OllllO11lO01OlOllOl11(
     O110l00l0lO0000OO1llO(0 * (1 * 3 + 0) + 1, 0 * (1 * 3 + 0) + (3 ^ 1)),
     ((0 * 3 + 0) * 2 + (0 * 4 + 0)) * ((0 * 2 + 0) * 6 + (1 ^ 5)) + ((0 * 
     2 + 0) * (0 ^ 5) + (0 * 2 + 1)))) + (O110l00l0lO0000OO1llO(
     OllllO11lO01OlOllOl11(0 * 4, 1 ^ 0 * 4 + 0), OlOlO1000llOl1OllO010(1, 
     0 * 6 + 3)) + (0 * OlOlO1000llOl1OllO010(2 ^ 0, 4 ^ 2) + 0))
     ) == OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(OllllO11lO01OlOllOl11
     (O110l00l0lO0000OO1llO(OlOlO1000llOl1OllO010(17511 ^ 9406 ^ 14217,
     OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(7922 * 4 + 0, 
     O110l00l0lO0000OO1llO(0 * 5 + 0, 6) + (0 * 6 + 2)), 0)), 
     O110l00l0lO0000OO1llO(0 * 2 + 0 ^ (1 ^ 0), O110l00l0lO0000OO1llO(0, 1 *
     3 + 0) + 1 ^ (0 * 5 + 1) * (1 * 6 + 0) + 1) + ((0 * 4 + 0) * (0 * 6 + 
     4) + 0)), O110l00l0lO0000OO1llO(O110l00l0lO0000OO1llO(0, 2 * 2 + 0) +
     (0 * 6 + 0), 2 ^ 0 ^ 4) + (O110l00l0lO0000OO1llO((0 * 5 + 0) * 4 + 0,
     OlOlO1000llOl1OllO010(2, 6)) + (0 * 5 + 0 ^ 0 * 2 + 1))), 
     OlOlO1000llOl1OllO010(1 * 5 + 1 ^ 3, 0 * 6 + 0) ^ 
     O110l00l0lO0000OO1llO(0, OllllO11lO01OlOllOl11((0 * 3 + 2) *
     OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(0, 4), 3 ^ 1), 1 ^ 0)) + (
     0 * 2 + (0 * 5 + 0))), OlOlO1000llOl1OllO010(0 * 5 + 0, 
     O110l00l0lO0000OO1llO(0, 2) + (0 ^ 1) ^ (0 * 6 + 0) * (0 ^ 6) + 0) ^ (
     OlOlO1000llOl1OllO010(OllllO11lO01OlOllOl11(O110l00l0lO0000OO1llO(0, 4
     ), 1), 0) ^ (0 ^ 2)))
