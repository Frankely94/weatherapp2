var greetdate=new Date()
var hours=greetdate.getHours()
 
if (hours>=5&&hours<=11) 

document.write('<h3>Hello! Good Morning!</h3>')
else if (hours==12) 
document.write('<h2>Good!! it is mid-day </h2>')
else if (hours>=13&&hours<=17) 

document.write('<h2>Good Afternoon! </h2>')
else if (hours>=18&&hours<=20) 

document.write('<h2>Good Evening! </h2>')
else if (hours>=21&&hours<=23) 

document.write('<h2>Good Night! </h2>')
else 

document.write('<h2>A Little Late to be awake.</h2>')

