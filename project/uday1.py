def game(a,b):
	from .uday import function_tradewar
	country1 = int(a);
	country2 = int(b);
	country={1:"INDIA",2:"US",3:"JAPAN",4:"PAKISTAN"}
	c1=country[country1]
	c2=country[country2]
	if(country1 == 1 and country2==2):
		function_tradewar(50,45,19,43,13,15,19,19,51,15,c1,c2)
	if(country1 == 1 and country2 == 4):
		function_tradewar(65,75,40,200,30,33,40,30,120,33,c1,c2)
	if(country1 == 2 and country2 == 4):
		function_tradewar(55,70,75,150,30,70,75,30,120,65,c1,c2)
	if(country1 == 2 and country2 == 3):
		function_tradewar(15,16,79,140,63,67,79,63,136,79,c1,c2)
	if(country1 == 1 and country2 ==3):
		function_tradewar(100,100,120,45,45,10,120,14,12,12,c1,c2)
	if(country1 == 3 and country2 == 4):
		function_tradewar(35,47,60,85,47,53,60,43,80,41,c1,c2)
