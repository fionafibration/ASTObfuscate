O1lO11l10O00OlO01OOOl = lambda llOlOOOll00O0l0lOl1Ol: ~llOlOOOll00O0l0lOl1Ol
l11l1lOOll01Ol111101O = lambda O10OOl1OOO1OO000O1l01: -O10OOl1OOO1OO000O1l01
l0lO0O11OO01O1ll000Ol = lambda OOOll0l0O1O011lOl0l11: not OOOll0l0O1O011lOl0l11
ll0lO11OO1011O01ll00O = (lambda O000l0O111l1101OO00Ol,
    OOll1ll1Oll100000OO0O: O000l0O111l1101OO00Ol and OOll1ll1Oll100000OO0O)
l1O00ll1O1O1lOl1l1O00 = (lambda l1011lO01OOO0O0000Oll,
    OO0O100O0O1l0l0OO11ll: l1011lO01OOO0O0000Oll - OO0O100O0O1l0l0OO11ll)
OOllOO11Ol00ll0O0l10O = (lambda lll0l1l100l1Ol0O1O1lO,
    OOO0lO010l0l0ll010l0l: lll0l1l100l1Ol0O1O1lO * OOO0lO010l0l0ll010l0l)
Ol1O11lOO0O001OOO111l = (lambda O0l1l110Ol00OO0001lOO,
    OO00011O0O0l1O0lO1111: O0l1l110Ol00OO0001lOO % OO00011O0O0l1O0lO1111)
lO11l0O01l001O11l0101 = (lambda lO11l1l00ll00O11l000O,
    ll11llOll0l010O11O1l0: lO11l1l00ll00O11l000O + ll11llOll0l010O11O1l0)
O1lOO0ll10100OO0101lO = (lambda O1OlO111O0l101010lll1,
    O1ll001O000l110lO0OOl: O1OlO111O0l101010lll1 << O1ll001O000l110lO0OOl)
l0O1ll0OO1010OOlll11l = (lambda O1O00O000ll1l0OlO0l0l,
    O0O110ll01O10l1l1l1O0: O1O00O000ll1l0OlO0l0l ^ O0O110ll01O10l1l1l1O0)
l1OOOO00110O1O1001111 = (lambda l1ll0OO0O1101l0l11010,
    lll1O00OOO10OOlOO100O: l1ll0OO0O1101l0l11010 | lll1O00OOO10OOlOO100O)
Ol01llllO1ll11OO11010 = (lambda ll0OlOOl111OlOl01011l,
    OOOOOl11O0l01lO011O01: ll0OlOOl111OlOl01011l // OOOOOl11O0l01lO011O01)
O10lOOllO10lOll0010OO = (lambda ll1l1OlO10Oll101O100O,
    ll0O0l1O0ll100llO111l: ll1l1OlO10Oll101O100O & ll0O0l1O0ll100llO111l)


def flag_check(buf):
 if l0lO0O11OO01O1ll000Ol(getattr(buf, ''.join(filter(lambda
     OlOlOll00O101000O000O: ord(OlOlOll00O101000O000O) % 3 != 0,
     'f\x0fQfH?f\t\x18lB\x1e?\x00*')).join(chr(Ol0l00l1O110O0Ol010l0 ^
     O10OOOO0ll01lO1Olll0O) for O10OOOO0ll01lO1Olll0O,
     Ol0l00l1O110O0Ol010l0 in zip(b'\xc9fA\x97\xdf\x9e\xf6\x13\xb5\x82',
     b'\xba\x12 \xe5\xab\xed\x81z\xc1\xea')))(bytes(lO11l0O01l001O11l0101(
     ''.join(filter(lambda O01101OOll0l0l1OOl1O1: ord(O01101OOll0l0l1OOl1O1
     ) % 5 != 0, '}\n_nUsZ\x1e-\x05PZ\x00U_')).join(chr(
     l01000l00Ol11001O1OOl ^ l1OlO1O1O001110l1OO0l) for 
     l1OlO1O1O001110l1OO0l, l01000l00Ol11001O1OOl in zip(b'f\xe3\xdc\xe6dm',
     b'\x1d\x85\xa8\x85;\x08')), ''.join(filter(lambda
     lOl11OlO1110l0001111l: ord(lOl11OlO1110l0001111l) % 5 != 0,
     'F7x-P\x00d\x14UP-i\x0f-\x00')).join(chr(l11O1l00l010OOlOlOlO0 ^
     l10O00Ol101101O0O1lO1) for l10O00Ol101101O0O1lO1,
     l11O1l00l010OOlOlOlO0 in zip(b'\xb6\xa3V\xb0\xdc4',
     b'\xda\xd3;\xd1\xa4Q')))[::lO11l0O01l001O11l0101(OOllOO11Ol00ll0O0l10O
     (-1 ^ 0, 1 * 3 + 2), 4)], encoding=(''.join(chr(l11ll1lO11110000O101O ^
     O0Ol0l11ll11llll0l00l) for O0Ol0l11ll11llll0l00l,
     l11ll1lO11110000O101O in zip(b']\xfb', b'e\xd6')) + 'ftu'[::-1][::-1 *
     12 + 11])[::-1 ^ 0]))) and buf[l11l1lOOll01Ol111101O(
     lO11l0O01l001O11l0101(OOllOO11Ol00ll0O0l10O(0, ((0 * 3 + 0) * (0 * 14 +
     2) + 0) * (0 * 15 + 14) + (0 * 7 + 6)), 0 * 13 + (0 * 12 + 1) ^ 0))
     ] == chr(3 - (7 * 15 + 9 ^ 12) + (2 ^ 0) * ((O1lO11l10O00OlO01OOOl(3) |
     10 * 11 + 4 ^ (10 ^ 6)) - (O1lO11l10O00OlO01OOOl(3) ^ (10 * 11 + 4 ^ (
     10 ^ 6))))):
  return (O1lO11l10O00OlO01OOOl(17 * 9 + 1 & (5 ^ 26)) & ~
      O10lOOllO10lOll0010OO(O1lO11l10O00OlO01OOOl(154), ~(10 * 3 + 1))
      ) % l0O1ll0OO1010OOlll11l(1 * 14 + 6 ^ 1 * 6 + 3, 2 ^ 1 * 10 + 5) == 0
 l111OOl1OOlOlllO0lO10 = lO11l0O01l001O11l0101((67108863 * (2 * 8 + 0) + 15
     ) * lO11l0O01l001O11l0101(OOllOO11Ol00ll0O0l10O(0 ^ 1, 3),
     lO11l0O01l001O11l0101(0 * (12 ^ 6), 1)), lO11l0O01l001O11l0101(
     l1O00ll1O1O1lOl1l1O00(0 * 2 + 0, (1 ^ 0) * 3 + 0),
     OOllOO11Ol00ll0O0l10O(2, ~(0 * 13 + 0) & 1 * (0 ^ 3) + 0)))
 O10l10100llOlO00OlO0O = []
 for l00000l10lO1000l11100 in range(lO11l0O01l001O11l0101(
     OOllOO11Ol00ll0O0l10O(1 * 12 + 4, 26 ^ 10), 0)):
  OO0111O1ll0lOOO11l0ll = l00000l10lO1000l11100
  for l110l11lOO1l10100OO0O in range((0 * 15 + 0) * 13 + 8):
   if l1OOOO00110O1O1001111(OO0111O1ll0lOOO11l0ll, lO11l0O01l001O11l0101(0 *
       5 + 0 - (0 * 7 + 0 ^ 0 * 9 + 1), OOllOO11Ol00ll0O0l10O(0 * 7 + 2,
       O10lOOllO10lOll0010OO(~(0 * 15 + 0), 0 ^ 0 * 13 + 1)))) - (
       OO0111O1ll0lOOO11l0ll ^ (0 * 7 + 0) * (10 ^ 1) + (0 * 9 + 1)):
    OO0111O1ll0lOOO11l0ll = O10lOOllO10lOll0010OO(O1lO11l10O00OlO01OOOl(
        O10lOOllO10lOll0010OO(OO0111O1ll0lOOO11l0ll, l0O1ll0OO1010OOlll11l(
        lO11l0O01l001O11l0101(OOllOO11Ol00ll0O0l10O(lO11l0O01l001O11l0101((
        37763906 ^ 32962418) * (1 ^ 4), 3), 4), l0O1ll0OO1010OOlll11l(2, 0 ^
        1)), l0O1ll0OO1010OOlll11l(1353243622, 2514445517 * 3 + 2)))), ~
        O10lOOllO10lOll0010OO(O1lO11l10O00OlO01OOOl(OO0111O1ll0lOOO11l0ll),
        O1lO11l10O00OlO01OOOl(lO11l0O01l001O11l0101(OOllOO11Ol00ll0O0l10O(
        886287196, lO11l0O01l001O11l0101((0 * 16 + 1) * 5, 1 ^ 5)), 0 ^ (0 *
        15 + 0) * (9 ^ 5) + (6 ^ 2)))))
   OO0111O1ll0lOOO11l0ll = Ol01llllO1ll11OO11010(OO0111O1ll0lOOO11l0ll,
       l0O1ll0OO1010OOlll11l(0 * 14 + 0, 0 ^ (0 ^ 2)))
  getattr(O10l10100llOlO00OlO0O, ''.join(chr(O110O1ll011l0111O1OOO ^
      O00lO1lO0OOlO001OOO01) for O00lO1lO0OOlO001OOO01,
      O110O1ll011l0111O1OOO in zip(b'V\xe8\xac\x13\x80\xea',
      b'7\x98\xdcv\xee\x8e'))[::-1][::-1])(OO0111O1ll0lOOO11l0ll)
 for l01OOO01OOllOl1l01O11 in buf:
  l111OOl1OOlOlllO0lO10 = Ol01llllO1ll11OO11010(l111OOl1OOlOlllO0lO10,
      lO11l0O01l001O11l0101(l0O1ll0OO1010OOlll11l(0 * 15 + 9, 11 ^ 30) * (
      OOllOO11Ol00ll0O0l10O(0 * 6 + 1 ^ 0, (1 ^ 0) * (6 ^ 3) + (1 ^ 0)) + (
      0 ^ 3)), 2 * 2 + 0 ^ 0 * 10 + 0)) ^ O10l10100llOlO00OlO0O[
      l1OOOO00110O1O1001111(l1OOOO00110O1O1001111(O1lO11l10O00OlO01OOOl(
      O1lO11l10O00OlO01OOOl(O1lO11l10O00OlO01OOOl(~(~(l111OOl1OOlOlllO0lO10 &
      lO11l0O01l001O11l0101((57 ^ 6) * (3 ^ 7), 2 ^ 1)) and ~(
      l111OOl1OOlOlllO0lO10 & lO11l0O01l001O11l0101(OOllOO11Ol00ll0O0l10O(
      63, 4), 1 * 3 + 0)))) & O1lO11l10O00OlO01OOOl((l111OOl1OOlOlllO0lO10 |
      OOllOO11Ol00ll0O0l10O(17 ^ 12 ^ 0 * 16 + 10 ^ (3 ^ 7) * (0 ^ 2) + (0 *
      15 + 0), OOllOO11Ol00ll0O0l10O(1, 0 * 6 + 3) + (0 * 8 + 2) - 13 + 2 *
      (~(OOllOO11Ol00ll0O0l10O(1, 0 * 6 + 3) + (0 * 8 + 2)) & 13)) +
      lO11l0O01l001O11l0101(OOllOO11Ol00ll0O0l10O(0 * (13 ^ 4) + (1 ^ 2), 0 *
      6 + 1 ^ (1 ^ 2)), (0 * 12 + 0) * (3 ^ 0) + (1 ^ 0))) - (
      l111OOl1OOlOlllO0lO10 ^ lO11l0O01l001O11l0101(OOllOO11Ol00ll0O0l10O(
      l0O1ll0OO1010OOlll11l(l0O1ll0OO1010OOlll11l(6 ^ 10, 27), 1 * 7 + 1), 
      ~(OOllOO11Ol00ll0O0l10O(0, 11 ^ 0) + 5 & (0 ^ 13)) & ~(~(
      OOllOO11Ol00ll0O0l10O(0, 11 ^ 0) + 5) & ~(0 ^ 13))), 3 * 2 + 1))))),
      l01OOO01OOllOl1l01O11) - (O1lO11l10O00OlO01OOOl(O1lO11l10O00OlO01OOOl
      (O1lO11l10O00OlO01OOOl(O10lOOllO10lOll0010OO(l111OOl1OOlOlllO0lO10, 
      51 * 5 + 0)) & O1lO11l10O00OlO01OOOl(O10lOOllO10lOll0010OO(
      l111OOl1OOlOlllO0lO10, OOllOO11Ol00ll0O0l10O(31, 
      l0O1ll0OO1010OOlll11l(3, 1) * (5 ^ 0 * 10 + 1) + 0) +
      lO11l0O01l001O11l0101(OOllOO11Ol00ll0O0l10O(0, 15),
      lO11l0O01l001O11l0101(1 * 7, 0)))))) ^ l01OOO01OOllOl1l01O11),
      l1O00ll1O1O1lOl1l1O00(~O10lOOllO10lOll0010OO(~(l111OOl1OOlOlllO0lO10 &
      lO11l0O01l001O11l0101(OOllOO11Ol00ll0O0l10O(l0O1ll0OO1010OOlll11l(0, 
      18 ^ 0), OOllOO11Ol00ll0O0l10O(0, 13) + (0 * 15 + 5) ^ 0 * (2 * 6 + 2
      ) + (11 ^ 0)), 1 * 3 + 0 ^ lO11l0O01l001O11l0101(0 * (2 ^ 7), 0 * 10 +
      0))), O1lO11l10O00OlO01OOOl(O10lOOllO10lOll0010OO(
      l111OOl1OOlOlllO0lO10, l0O1ll0OO1010OOlll11l(lO11l0O01l001O11l0101((4 ^
      15) * (0 ^ 14), 8), lO11l0O01l001O11l0101((2 ^ 15) * (
      OOllOO11Ol00ll0O0l10O(1, 0 * 14 + 4) + (1 ^ 2)), 0 * (6 ^ 10) + (0 * 
      13 + 2)))))) | O1lO11l10O00OlO01OOOl(l01OOO01OOllOl1l01O11),
      l0O1ll0OO1010OOlll11l(O1lO11l10O00OlO01OOOl(O10lOOllO10lOll0010OO(
      O1lO11l10O00OlO01OOOl(l111OOl1OOlOlllO0lO10 & lO11l0O01l001O11l0101(
      OOllOO11Ol00ll0O0l10O(l0O1ll0OO1010OOlll11l(0 ^ 6 ^ (14 ^ 16),
      lO11l0O01l001O11l0101((3 ^ 1) * 5, 0 * 8 + 0)), ~2 & 1 * 7 + 5 | 2 & 
      ~(1 * 7 + 5)), (0 * 7 + 0) * (4 ^ 8) + (2 ^ 1))), ~
      O10lOOllO10lOll0010OO(l111OOl1OOlOlllO0lO10, l0O1ll0OO1010OOlll11l(
      l0O1ll0OO1010OOlll11l(19 * 12 + 0, 5 * 13 + 5), 93)))),
      O1lO11l10O00OlO01OOOl(l01OOO01OOllOl1l01O11))))]
 l111OOl1OOlOlllO0lO10 = O1lO11l10O00OlO01OOOl(l111OOl1OOlOlllO0lO10 &
     lO11l0O01l001O11l0101((451360121 ^ 156634730) * (((1 ^ 0) * 5 + (0 ^ 1
     )) * (0 ^ 0 * 5 + 2) + (0 * 7 + (0 * 10 + 1))), 8)
     ) & O1lO11l10O00OlO01OOOl(O10lOOllO10lOll0010OO(O1lO11l10O00OlO01OOOl(
     l111OOl1OOlOlllO0lO10), O1lO11l10O00OlO01OOOl(lO11l0O01l001O11l0101(
     OOllOO11Ol00ll0O0l10O(l0O1ll0OO1010OOlll11l(~(6017518 * 14 + 9) & 
     1776320 * 7 + 2 | 6017518 * 14 + 9 & ~(1776320 * 7 + 2), 369752924), 0 *
     14 + 13), lO11l0O01l001O11l0101((0 * (0 * 14 + 9) + 0) * (1 * (3 * 3 +
     0) + (0 * 10 + 7)), (0 * 6 + 0) * (0 ^ 11) + 8)))))
 return l0O1ll0OO1010OOlll11l(Ol1O11lOO0O001OOO111l((lambda
     Ol11l1ll0l1lO11001O10, O1OOll11l0l1OO011OO11: (lambda
     O0ll11010l0OOOl0011l0, O110OlO0O1010llll0O11, l1101O0Ol00110llOO0l0:
     O0ll11010l0OOOl0011l0(O0ll11010l0OOOl0011l0, O110OlO0O1010llll0O11,
     l1101O0Ol00110llOO0l0))(lambda O00Ol0ll100Ol0OO10Ol1,
     O111l00lOOOllOOOllOlO, OOOl10l0l1OOOO1l1l0O0: O00Ol0ll100Ol0OO10Ol1(
     O00Ol0ll100Ol0OO10Ol1, l0O1ll0OO1010OOlll11l(O111l00lOOOllOOOllOlO,
     OOOl10l0l1OOOO1l1l0O0), O1lOO0ll10100OO0101lO(O111l00lOOOllOOOllOlO &
     OOOl10l0l1OOOO1l1l0O0, lO11l0O01l001O11l0101(OOllOO11Ol00ll0O0l10O(0,
     l0O1ll0OO1010OOlll11l(l0O1ll0OO1010OOlll11l(4 ^ 1, 1),
     l0O1ll0OO1010OOlll11l(0 * 10 + 3, 1 ^ 0))), 0 ^ 0 * 15 + 1 ^ 0))) if
     OOOl10l0l1OOOO1l1l0O0 else O111l00lOOOllOOOllOlO,
     Ol11l1ll0l1lO11001O10, O1OOll11l0l1OO011OO11))(O10lOOllO10lOll0010OO(
     lO11l0O01l001O11l0101(l0O1ll0OO1010OOlll11l(l111OOl1OOlOlllO0lO10,
     lO11l0O01l001O11l0101(OOllOO11Ol00ll0O0l10O(~((104833219 ^ 370930734) &
     812118641) & O1lO11l10O00OlO01OOOl(~(64298838 ^ 334580667) &
     O1lO11l10O00OlO01OOOl(62470664 * 13 + 9)), lO11l0O01l001O11l0101(0 * (
     (0 * 4 + 2) * 5 + (0 * 9 + 3)), (0 * 8 + 0) * (15 ^ 4) + (0 * 8 + 5))),
     l0O1ll0OO1010OOlll11l(0 * 11 + 0, 0 ^ 3 ^ (5 ^ 2)))),
     lO11l0O01l001O11l0101(0 * l0O1ll0OO1010OOlll11l(0, 0 ^ 3), 
     OOllOO11Ol00ll0O0l10O(0, 4 ^ 12 ^ 24) + (0 ^ 1 ^ 0))), ~
     l0O1ll0OO1010OOlll11l(l111OOl1OOlOlllO0lO10, O10lOOllO10lOll0010OO(
     O1lO11l10O00OlO01OOOl(O10lOOllO10lOll0010OO(O10lOOllO10lOll0010OO(~
     lO11l0O01l001O11l0101((10981333 * 13 + 1) * (7 * 2 + 0), 1 ^ 5), 
     33994789 ^ 70196807 ^ 391130512) | O10lOOllO10lOll0010OO(
     OOllOO11Ol00ll0O0l10O(204665102 ^ 78691548, 14) + 4,
     O1lO11l10O00OlO01OOOl(103392866 ^ 391130512)), 208713910 * (1 * 12 + 4
     ) + (0 * 10 + 2))), ~(~l0O1ll0OO1010OOlll11l(1998602624, (11494526 ^ 
     26275201) * (0 * 15 + 14) + (0 * 7 + 0)) & O1lO11l10O00OlO01OOOl(
     3006484538 ^ 1949883224))))) | l0O1ll0OO1010OOlll11l(
     l0O1ll0OO1010OOlll11l(25513302 * 15 + 6, 873564420) ^ (146931 * 12 + 
     10 ^ 101249799 * 3 + 1), 4261706 ^ 15107909 ^ (1082012597 ^ 271158556 *
     3 + 0)), O10lOOllO10lOll0010OO(O1lO11l10O00OlO01OOOl(
     lO11l0O01l001O11l0101(l111OOl1OOlOlllO0lO10 ^ lO11l0O01l001O11l0101(
     lO11l0O01l001O11l0101(((1524174 ^ 14026) * 16 + (2 * 5 + 2)) *
     l0O1ll0OO1010OOlll11l(10 ^ 7, 0 * 7 + 6), 4 ^ 14) *
     l0O1ll0OO1010OOlll11l(4 * 3 + 0 ^ 0 * 6 + 1, lO11l0O01l001O11l0101(1 *
     (0 * 8 + 7), 0)), OOllOO11Ol00ll0O0l10O(0, 4 * 2 + 0) + (0 * 7 + 1) ^ 
     5), l0O1ll0OO1010OOlll11l(0, lO11l0O01l001O11l0101(((0 * 7 + 0) * (0 ^
     13) + 0) * (1 ^ 3 ^ (0 ^ 1)), 1))) & O1lO11l10O00OlO01OOOl(
     l111OOl1OOlOlllO0lO10 ^ OOllOO11Ol00ll0O0l10O((38591503 ^ 7830064) * (
     0 * 7 + 6) + 5 ^ (19848547 ^ 130996239), 0 * (6 ^ 12) + (1 ^ 8) - (4 ^
     3) + 2 * (~(0 * (6 ^ 12) + (1 ^ 8)) & (4 ^ 3))) + (
     OOllOO11Ol00ll0O0l10O(OOllOO11Ol00ll0O0l10O(0 * 11 + 0, 5 ^ 9) + 0, (1 ^
     3) * (5 ^ 3) + (0 * 5 + 4)) + (2 ^ 4)))), OOllOO11Ol00ll0O0l10O(
     27324865 * 13 + 7, 3) + (~(0 * 5 + 0) & (1 ^ 0) | 0 * 5 + 0 & ~(1 ^ 0)
     ))), O1lOO0ll10100OO0101lO(0 * ((0 ^ 1) - 4 + 2 * (~(0 ^ 1) & 4)) + (0 *
     (1 * 5 + 4) + (0 * 14 + 1)), l0O1ll0OO1010OOlll11l(2 * 7 + 2 ^ 1 * 9 +
     0, 5 * 11 + 2))), (205488027 ^ 8489386 ^ 54535334) * ((0 * 8 + 4) * 4 +
     0) + (7 ^ 13 ^ 0 * 9 + 2)) == OOllOO11Ol00ll0O0l10O(246913, 0 * 12 + 7 ^
     (2 ^ 0)) + ((0 * (4 ^ 20) + 0) * (0 * 9 + 4 ^ 0 * 7 + 1) + (0 * 6 + 2))
