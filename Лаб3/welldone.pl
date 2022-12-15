man(s,otl).
man(k,tr).
woman(l,hor).
woman(r,tr).
w(M):-man(M,otl);woman(M,otl);man(M,hor);woman(M,hor).
isman(M):-w(M),man(M,_). 