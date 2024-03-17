prod(map(lambda x: x+1, cnt))-1

"""
1) 의상의 종류가 "1가지"인 경우. ( 의상 A가 a 개 )
=> a개의 조합이 가능 

2) 의상의 종류가 "2가지"인 경우. ( 의상 A a개, 의상 B, b개 )
=> a + b + ab 개의 조합이 가능 

3) 의상의 종류가 "3가지"인 경우. ( 의상 A a개, 의상 B, b개, 의상 C c개)
=> a + b + c + ab + ac + bc + abc개의 조합이 가능

4) 의상의 종류가 "4가지"인 경우.  ( 의상 A a개, 의상 B, b개, 의상 C c개, 의상 D d개)
=> a + b + c + d + ab + ac + ad + bc + bd + cd + abc + abd+ bcd + abcd개의 조합이 가능


이 것을 공식으로 일반화 시키면,
(a + 1)(b + 1)(c + 1)...(해당 종류 옷의 수 + 1) -1 을 계산하면 된다.
출처 : https://aram-su.tistory.com/22
"""
