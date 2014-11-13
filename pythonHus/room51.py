from . import room

def do():
	print("""
                          .oyhhs:   
                 ..--.., shhhhhh-   
               -+++++++++`:yyhhyo`  
          .--  -++++++++/-.-::-`    
        .::::-   :-----:/+++/++/.   
       -:::::-.          .:++++++:  
  ,,, .:::::-`             .++++++- 
./+++/-`-::-                ./////: 
+++++++ .::-  Ubuntu 14.04
./+++/-`-::-                :yyyyyo 
  ``` `-::::-`             :yhhhhh: 
       -:::::-.         `-ohhhhhh+  
        .::::-` -o+///+oyhhyyyhy:   
         `.--  /yhhhhhhhy+,....     
               /hhhhhhhhh-.-:::;    
               `.:://::- -:::::;    
                         `.-:-'     
""")
	import speedsolve
	
	svar = "j" 
	fyrirUtan = room.grunnur(51)
	if(svar[0]=='j' or svar[0]=='y'):
		fyrirUtan.go('n')
	else:
		raise ValueError(fyritUtan.info)
