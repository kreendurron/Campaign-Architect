/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
use('dnd');

// Insert a few documents into the sales collection.
db.getCollection('npcs').insertMany([
  { 
    'name': 'Walter',
    'alive': true,
    'organizations': ["The Order of Durron", "The Disorder of the Flame"]
    },
  { 
    'name': 'Ratley',
    'alive': false,
    'organizations': ["The Emerald Flame"]
    },
    
]);

// Run a find command to view npcs in an orginization
const listNPCsInOrderOfDurron = db.getCollection('npcs').find({
    organizations: "The Order of Durron"
  });
  
  
  let count = 0;
  while(cursor.hasNext()) {
    cursor.next();
    count++;
  }
  
  // Print a message to the output window.
  console.log(`${count} NPCs in The Order of Durron.`);


