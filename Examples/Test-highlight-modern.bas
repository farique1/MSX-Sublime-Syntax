define [ifa] [if a$ = ]

rem get #1,i :a$ = f$ :p$ = bin$(asc(a$)):
a = len(p$) :z = 8-a :c$ = string$(z,"0") :b$ = c$+p$:
rem line warps the highlight if : at end

{read_keyboard_main}
	a$ = inkey$
	if a$ = chr$(13) and hs = 0 then goto {edit_screen}
	if a$ = "1" then c1=c1-1 :gosub {set_color}
	if a$ = "2" then c1=c1+1 :gosub {set_color}
	[ifa]chr$(&h1c) and sx+8 < 95 then sx=sx+8 :ps=ps+80 :gosub {move_scan_sprite}
	[ifa]chr$(&h1d) and sx-8 > 15 then sx=sx-8 :ps=ps-80 :gosub {move_scan_sprite}
goto {read_keyboard_main}

{set_color}
	c1 = abs(c1 mod 16+16) mod 16: ' use DEF FN
	c2 = abs(c2 mod 16+16) mod 16: ' use DEF FN

	color c2,c1,c1
	vpoke 8194,c4*16+c1 :vpoke 8195,c4*16+c1
	vpoke 6915,c2 :vpoke 6919,c2 :vpoke 6923,c2 :vpoke 6927,c2
	for f=8208 to 8220 :vpoke f,c3*16+c1 :next
return

{move_scan_sprite}
	ay=sy+(ss-2) :ax=0
	if sy+(ss-2) > 101 then ax=8 :ay=23+(sy+(ss-2))-103
	if sx+ax > 95 then ay=200

	vpoke 6912,sy :vpoke 6913,sx
	:vpoke 6916,ay :vpoke 6917,sx+ax

	## [?@] becomes locatex,y:print
	[?@]3,17string$(4-len(hex$(ps)),"0")+hex$(ps):' use PRINT USING ?
	[?@]8,17string$(4-len(hex$(ps+(ss-1))),"0")+hex$(ps+(ss-1)):' use PRINT USING ?
return

## Label with non standard character
{freeze refresh}
	if a$ = "C" then _
		hs = abs(hs-1):
		if hs = 1 then _
			locate4,7:print "FREEZE" _
		else _
			locate3,7:print "UNFREEZE":
			gosub {update_memory_position}
		endif 
	endif 

{character_shapes}
	data 231,195,165,024,344,165,195,231:' data lines
	data 255,128,128,128,abc,"8",128,255:' uniform color

	data 255,129,000,000,000,000,000,000,_ 
		 129,255,000,000,000,000,000,000:' even with line break
