from Cracker import Cracker

x = Cracker("ABCDEFGHIJKLMNOPQRSTUVWXYZ","RIGHT");
a = x.crack_code("""KRGBF IATEU VUNNW WAKAF RAPTU TCYNG ECWJH
XYQFH HZMXR RBOCI WRIJU EWAHS MTGPA JIQGV
RKBFT VBKJR EPAPN XYMZV GHVOQ GJYWU GWYUI
NXBLG FCNYA XUHAF HFPFJ VKVNA OPEXT HHUQQ
MKXTM NEBII TLVUX FSZCB NAUKI RGJQA ZGTOE
CXUIJ MNVVB YBXUT RWGHD ZTEYO NRBDX LVSNK
VJPQF BOBIG PJMTC PBENB OBIYU INEQH CRCYQ
RACCQ FRLZW YXCCS SYEFS RYBTP PGRRG PIW""", ["EXPERIENCE", "FATALITIES"])

code_2 = """AASSH GOXBG DYFVQ RVHYZ UCKNU UIFPM UNBGB EPXFN
IJKZG HSBXC TMCRV GQJGX APLRJ UAQSG XFNBR ECHNL
IXQXJ RYCHL SXVVC VVQRG GWBOY DLVWP TRIHX ZHARJ
AYIWX TXTIJ NBLBT FXTYM VVLKR AZMYP AVYJH YJSOV
HAKGP UQNJB TRTTR KGUSQ HJPWR ZKUPC ZRIJO VIVTC
MQMVF BVFWK RUQMZ GCZYZ HFWBR QCXRC RLRSI HQNTQ
NJMRK FIAPX UFAYF VQVGG LVFVS RUHLF TVKJV KINOO
GHXJU RGHTQ IJPWV JBHPN ZRZHT PPDGN APXTY MTLRS
RAOIU DYRYV VBJWV MAIBL BANMU IKPHQ WBUFC DIFPH
TWBPH IHXJN OKZVS NKCUT YVZEQ AAVUT T"""
b = x.crack_code(code_2,["EMPRESA","STOP"])
print (b[0], "\n", b[1])