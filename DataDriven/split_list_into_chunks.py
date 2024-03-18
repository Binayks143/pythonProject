def split_list_into_chunks(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

numbers_list = (4498539,5334734,8918727,7746252,15812860,10616574,13889350,15812768,5469101,14562647,3824893,4822783,12482944,9403967,4855364,3861890,15798133,7411902,15810449,13430419,13318595,4626425,7273980,7004939,15812821,1176868,6703627,1964766,7353764,14266239,9945867,12185309,6807395,15812799,9573627,8648435,7229044,14232289,11970195,9725601,6707115,11671393,9931892,15812705,15812796,13517000,10102713,2477166,8489708,15810542,7642565,15812775,6087129,13013642,14446213,8371531,4377707,15204084,8683221,9839602,7262296,14366696,7617672,15812712,15810837,15812782,7052674,5676067,13679341,12910817,15812713,5051959,15572781,11588974,1526522,13411765,14124463,11117057,10433403,906879,15810600,12711418,15312793,15811133,9525681,10111325,3085538,13524831,10892157,15811199,13198442,14612964,10882981,2311699,13586421,14489549,15811420,12764364,15812664,15812630,15812615,120643,14492567,15812645,15703761,1350767,15812594,6722471,14262333,1992861,8638430,9990515,15522071,11584863,13588690,14059528,11762237,14592950,12543244,15811358,15811903,12874922,15811633,15811344,7748552,9626259,15812581,13045320,8261390,10466649,15812460,4315098,11358050,8796053,1876193,8432933,1818444,5591387,13067218,14203316,5319369,14749423,4066569,15681567,12145254,12498202,15812575,14149455,3359354,14241698,13886843,15790821,13075117,15109151,12048279,2747373,15811588,8623914,9189863,10087388,14709688,5841635,15168602,15796480,12368326,10723911,15689658,10250493,15795766,1838031,15812447,15812452,13704163,15812489,7259969,15812467,13555466,15812511,15812483,15812323,15810152,7025208,13330661,4728534,15812480,15812486,15810649,13533246,15812465,1749083,15812435,15809981,14615748,13309467,15812462,14156513,15812106,13552135,14075252,14879445,15812440,5245099,12423546,9822588,15812411,15812451,14027579,15812441,1622127,15812444,15758362,1716635,15812393,2064374,13137892,15811945,13880190,5298138,13235209,15811676,15812310,15812361,7579671,14032066,15811304,6017483,12752372,15812345,15812347,15812380,14589425,6753826,15812363,10024234,4476659,9288307,12930627,6144335,3307101,9731127,11559272,14960956,13556806,15811229,7648569,15812241,15812321,14191753,12289030,12874285,7133042,15812290,15812028,9871348,13485305,13287781,15812272,13845824,14530787,15812249,12759537,8900193,14495348,13922257,15261035,14029501,14048355,14056274,15812207,15812226,6683735,15811994,15812113,5058933,15812141,15812185,13532019,10609210,15812212,2389512,10222335,15812228,2549226,13732185,12178228,15812169,8949723,15812050,15812069,15812032,11616399,1442803,15812096,14583255,13972412,7445487,15583515,9120663,14753481,8417751,15812183,14808321,13562664,15559882,15811757,15812019,8186297,9130394,11963393,7999756,9726842,10748838,11855610,13389734,13105254,7512622,14051917,9775184,8651075,10304302,11853711,15810522,14245426,14328091,14561518,12579179,15812007,15812026,13578648,13556267,15464118,1080362,15370561,15811971,3961358,12852389,14701265,11533490,7213096,14731276,15811930,14696154,14410867,14556242,10222521,2892240,14755772,15454415,15811950,9147422,8488907,11090077,9273267,8577838,15768782,6126615,15811901,6031582,15811926,15808319,5475878,15811906,8538979,12621987,15778815,15811820,1252387,15811916,2867353,14536303,15811797,9718918,12717968,10741379,4266864,12541217,7927871,7486788,6588563,11099105,7761348,15811878,8875215,11905959,13972969,11509344,2482783,14625832,13578608,14506037,13553731,9840526,15713708,15811856,15811809,12510475,12462255,14575715,8564067,11663866,15811731,13484715,5407944,15811668,2367933,5493499,2870332,7026391,9843406,17104,11491249,15811852,13946487,15811806,2606723,15118598,5073287,15811777,15810510,15811817,7570217,9627593,8258302,9443170,13644047,10039741,14055371,3110865,15810054,8151363,3870802,13152316,15811745,12640879,13727444,13924894,13782911,10788642,14049532,15105451,13559793,9649823,15410464,5704172,12438695,15726164,8066630,11411617,15811753,15811754,8629749,9967263,15811749,9323087,15811742,15811732,14405491,8007881,15811201,9890800,15811696,15811699,14243860,15811684,15811650,15811685,15811670,7172595,10794238,15811652,12054495,8637930,15811563,13617748,5485777,14231400,13932282,13824263,9503992,9643163,14939817,15332869,7509609,9609237,15811666,15432084,11264318,15811497,11292234,5444707,15811637,6024783,12494377,2169106,15811574,1740077,7541815,12239880,3652496,11034204,12636909,5654832,13614920,7765581,12922371,14318322,7610238,1657438,7140859,10685245,15809707,7755008,11078877,15810086,15727498,15811558,598050,15811543,8884781,15545589,15811562,11490712,11974160,12572129,13943516,15811549,15364687,2405627,12357959,15688753,15809888,11238665,15811441,15811507,8368578,12115022,7784201,9357252,15811526,14730262,8848213,7587489,14192727,9818296,15811476,4950216,15811488,14490090,13686229,781028,15811491,6960696,15811431,11702645,7628402,9722263,10034442,12803270,15115214,7029260,6636539,7191410,14856867,15082755,4443551,15236796,15811447,6355567,14837382,13719486,5208948,12417403,15811356,15811230,13133802,8493665,11866377,14181180,15811438,9854725,11904248,15811285,7415339,901095,2725158,15805766,13146074,15811393,14534075,4975146,11398943,4501422,2160106,15811379,14776801,15811371,14387508,14402845,2456382,15165807,15009073,15811380,15658499,15811392,1258230,5512844,2009890,15811337,15799807,14058955,8079027,6884588,15811348,11522341,15811366,14263819,6792846,15811321,15811027,2084401,7353860,15811093,15810663,11367283,15810193,14956551,15811237,15810494,186562,15811288,15811328,15811354,4199914,15811264,13070077,14985139,10830760,11509633,13414586,8966002,14541880,14552798,15811210,11432750,12391311,9413479,15811267,12478572,15811253,13591154,10131573,11483341,13186294,15811183,15811252,15327503,15795827,11618484,8015701,14805624,7936111,6898226,15811184,4829467,9426989,4373367,3415849,8620749,15811185,4534641,3750709,15811191,10673838,13701453,1398479,3526237,5864237,8565193,12739703,2919336,13085516,15810929,15811202,10024449,8036705,7558796,15811130,15811140,235844,10390931,15811165,15811025,12919236,13827649,15811128,15811123,8537992,7871663,8940686,12253060,15811135,15245763,15345920,11554251,10159337,15811079,12869599,15811084,8637146,15811048,12772771,11576092,15811104,15780243,15811086,3517719,5034328,15810985,15258633,15019802,13477340,14370887,14057829,8272178,12313006,6639108,14115584,13275232,4937151,14056140,15234654,15811026,15811035,15255586,15300038,15811058,14401696,13088448,15791820,13203680,15811052,1448191,15014363,14068101,7348177,14269989,15811002,5614433,12593358,12479250,10909415,15810912,11028121,11495879,748688,14970375,15811004,15811003,7346272,15139124,15810886,15013246,12695819,5629363,15809562,15810992,14089062,15807732,15810935,8724556,8685183,15564477,1571974,2521575,3299625,15810963,5138506,15810876,15810898,14992363,15810890,15810949,2326747,15810917,9789659,12324823,9125355,9031893,12203583,4204648,14579968,14103242,15810858,15809118,15769550,14952311,12279084,8961702,6933210,15810891,13289929,11059606,9067435,15809748,7449498,8396462,15810808,14554311,13375502,5834601,5619838,12229614,679778,15807008,3540030,2779779,12997869,11844631,8478156,8665255,13269704,8607978,14373295,13311959,15810770,15805274,15810782,15426402,10985336,13044914,9533633,15810754,14105726,13288715,10179978,10461399,11796479,15810709,8802382,13285753,14733351,9376461,7886596,15782981,13223602,15608821,3216635,15563508,12224733,14756350,14845289,15679992,14784121,6222660,8159783,12174763,7641421,14547169,12560957,14866275,15652649,15810627,14563322,13558841,4900233,15810554,12455891,15810636,15810642,4338334,3223361,15084604,12570852,13777746,13323627,6552509,13646929,15810654,7221667,10941895,14018112,15038134,15810539,12346298,15781045,10153098,13523433,8561506,14376750,3784806,15804553,15810533,13410746,6362733,8315163,10783306,14164365,15810560,10349339,15810584,14065420,15264983,13653498,15810577,1647661,9909165,15807681,11644337,13160245,14220431,7220465,12957090,14487614,13363556,15810557,15807915,5678231,15810545,13381558,14419564,9164403,11447425,15141640,8703214,7401087,7062163,9507836,14339116,8869684,15810527,15810526,15810505,11009342,15422286,14072774,11486085,15810486,9964905,8575134,5827985,15810429,8995294,7893789,15781676,15810459,15810090,15810072,3469505,15810493,15810462,13130872,13272962,15415890,15810491,8789477,15810484,10233966,15810473,15810398,14491811,11575049,8829004,14666320,15810403,12912353,14102252,15810411,12920776,2515855,13943947,15807755,15434729,14590554,12727985,12104946,15793714,9525437,13118849,6669355,9334247,14288899,13186591,7513715,10712781,13709777,6998191,11214723,13992017,15810323,15810385,15810175,10857905,10080683,4181795,15810316,14501456,11590072,14578933,15810335,5962292
)
chunked_list = split_list_into_chunks(numbers_list, 500)

# Print the first few chunks to demonstrate
for i, chunk in enumerate(chunked_list[:5]):
    print(f"Chunk {i + 1}: {chunk}")
