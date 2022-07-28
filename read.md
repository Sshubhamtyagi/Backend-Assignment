Execution of program - 
Take the inputs from txt file.

Solution - 
Created 4 dicts -
1.Dictionary for  car and slot mapping ->{'KA-01-HH-1234':1,'PB-01-HH-1234' :2}
2.Dictionary for driver age and vehicle mapping - > {21:['KA-01-HH-1234 ','PB-01-HH-1234 ']}
3.Dictionary for driver age and slot mapping - > {21:[1,2]}
4. Slots array for storing the car info at particular slot

For finding the slot nearest to starting slot , I am iterating on the slots array and return first empty slot.
