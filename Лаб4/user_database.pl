test1(0,"Alex","rexpass",["1","2","3"]).
test1(1,"Sierra","paswwword",["1","3"]).
test1(2,"DirFar","123456",["1","2"]).
test1(3,"Kegler","tristan",["2","3"]).
test1(4,"KidNamedFinger","elevate",["1","2","3"]).

test_id_to_user(ID,Username):-test1(ID,Username,_,_).
test_user_to_pass(Username,Password):-test1(_,Username,Password,_).
test_iduser_awards(ID,Username,Awards):-test1(ID,Username,_,Awards).