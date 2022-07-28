from collections import defaultdict
class ParkingLot:
  def __init__(self,size):
    self.size = size
    self.slots = [0] * (self.size+1)
    self.car_map  = {}
    self.driver_vehicle_map  = defaultdict(list)
    self.driver_slot_map  = defaultdict(list)


  
  def slot_available(self):
    for i in range(1,self.size):
      if self.slots[i] == 0:
        return True,i
    return False,-1
    
  def book_slot(self,slot_no,vehicle_no,driver_age):
    self.slots[slot_no] = (vehicle_no,driver_age)
    self.car_map[vehicle_no] = slot_no
    self.driver_slot_map[driver_age].append(slot_no)
    self.driver_vehicle_map[driver_age].append(vehicle_no)
    
  
  def park_car(self,vehicle_number,driver_age):
    slot_avalable, slot_no = self.slot_available()
    
    if not slot_avalable:
      return slot_avalable, slot_no  
    self.book_slot(slot_no,vehicle_number,driver_age)
    
    return slot_avalable, slot_no
    
      
  def get_slot_numbers_using_age(self,age):
    return self.driver_slot_map[age]

  def get_vehicle_numbers_using_age(self,age):
    return self.driver_vehicle_map[age]

  def get_slot_number_of_vehicle(self,vehicle_no):
    return self.car_map.get(str(vehicle_no))
        
  def leave_slot(self,slot_no):
    parked_vehicle_no = self.slots[slot_no][0]
    driver_age = self.slots[slot_no][1]
    self.slots[slot_no] = 0
    self.car_map.pop(parked_vehicle_no)
    self.driver_slot_map[driver_age].remove(slot_no)
    self.driver_vehicle_map[driver_age].remove(parked_vehicle_no)
    
    return parked_vehicle_no,driver_age
  
  

def main():
  parking_lot =None
  with open('input.txt') as f:
    for line in f:
        line = line.split(' ')
        command = line[0]
        if command == 'Create_parking_lot':
          parking_lot = ParkingLot(int(line[1]))
          print('Created parking of '+ str(int(line[1])) +' slots')
          
        elif  command == 'Park':
          vehicle_no = str(line[1])
          driver_age = int(line[3])
          slot_available,slot_no = parking_lot.park_car(vehicle_no,driver_age)
          print('Car with vehicle registration number '+ vehicle_no+' has been parked at slot number '+str(slot_no))
          
        elif command == 'Slot_numbers_for_driver_of_age':
          age = int(line[1])
          print(parking_lot.get_slot_numbers_using_age(age))
          
        elif command == 'Slot_number_for_car_with_number':
          vehicle_no = line[1].strip('\n')
          slot_no = parking_lot.get_slot_number_of_vehicle(vehicle_no)
          print(slot_no)
          
        elif command == 'Leave':
          slot_no = int(line[1])
          vehicle_no ,driver_age = parking_lot.leave_slot(slot_no)
          print('Slot number '+ str(slot_no)+' vacated, the car with vehicle registration number '+vehicle_no+' left the space, the driver of the car was of age '+str(driver_age))
          
        elif command == 'Vehicle_registration_number_for_driver_of_age':
          print(parking_lot.get_vehicle_numbers_using_age(int(line[1])))
 
    

if __name__ == "__main__":
    main()  
  
    
    
    
    
