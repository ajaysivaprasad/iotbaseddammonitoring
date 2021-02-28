const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);

exports.motionSensor = functions.database.ref('/CollectedData/VibrationLevel')
    .onWrite(( change,context) => {
  const status = change.after.val();
 
  const payload = {
     notification: {
        title : "Security Alert",
        body: "Dam Movement Detected",
        icon: "default"
          
        }
        };
   const options = {
        priority: "high",
        timeToLive: 60 * 60 * 24
        };
   if(status == "Movement Detected!")
     return admin.messaging().sendToTopic("Notifications", payload, options);
   else
     return 0;
  
  
    });
