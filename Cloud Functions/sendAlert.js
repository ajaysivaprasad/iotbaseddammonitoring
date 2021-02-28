const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);
var level = 0;

exports.sendAlert = functions.database.ref('/CollectedData/WaterLevel')
    .onWrite(( change,context) => {
  	   const wlvl = change.after.val();
  	   var nevval = parseFloat(wlvl);
  		
  		var title = "";
  		var f = 0;
  		if(nevval<=30.00){level = 0;}
		else if(nevval>30.00 && nevval<=35.00 && level != 1){
        	level = 1;f=1;
          	title = "Yellow Alert";
        }else if(nevval>35.00 && nevval<=40.00 && level != 2){
        	level = 2;f=1;
          	title = "Orange Alert";
        }else if(nevval>40.00 && level != 3){
        	level = 3;f=1;
          	title = "Red Alert";
        }
  			
  
  
  if(f==1){
  
       const payload = {
        notification: {
          title : title,
          body: "The water level is "+ nevval,
          icon: "default"
          
        }
        };
        const options = {
            priority: "high",
            timeToLive: 60 * 60 * 24
        };
        
      
        return admin.messaging().sendToTopic("Notifications", payload, options);
        }
  		else
        {
          return 0;
        }
    });
