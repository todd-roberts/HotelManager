from manager import Manager
from guest import Guest
from room import Room, Door

class Hotel:
    def __init__(self):
        self.manager = None
        self.lobby = None
        self.rooms = []
        self.vacant_rooms = []
        self.doors = []
        self.guests = []
        self.guests_checking_in = []
        self.create_hotel()

    def create_hotel(self):
        lobby = Room('Lobby', (0, 0), (15, 20))
        office = Room('Office', (0, -10), (10, 10))
        hall = Room('Hall', (10, -55), (5, 55))

        self.rooms.append(lobby)
        self.rooms.append(office)
        self.rooms.append(hall)

        office_door = Door((2, 0), (3, 0), False, lobby, office)
        hall_door = Door((11, 0), (3, 0), False, lobby, hall)

        self.doors.append(office_door)
        self.doors.append(hall_door)

        lobby.add_door(office_door)
        office.add_door(office_door)
        lobby.add_door(hall_door)
        hall.add_door(hall_door)

        self.manager = Manager([5, -5], 1, 6.0, office)

        self.guests.append(Guest([lobby.loc[0] + 50, lobby.loc[1] + 50], 1, 4, (255, 0, 0)))
        self.guests.append(Guest([lobby.loc[0] + 100, lobby.loc[1] + 100], 1, 4, (0, 255, 0)))

    def update(self):
        self.manager.update()
        for guest in self.guests:
            guest.update()

    def draw(self, screen):
        offset = self.manager.get_offset()
        
        for room in self.rooms:
            room.draw(screen, offset)
        for door in self.doors:
            door.draw(screen, offset)
        self.manager.draw(screen)
        for guest in self.guests:
            guest.draw(screen, offset)


    def handle_mouse_click(self, pos):
        if self.manager.interactable_state == Manager.CHECK_IN_STATE:
            guest = self.get_guest_at_position(pos)
            room = self.get_room_at_position(pos)
            if guest and room:
                guest.assign_room(room)
                self.guests_checking_in.remove(guest)
                self.vacant_rooms.remove(room)
                guest.next_state()

    def get_guest_at_position(self, pos):
        for guest in self.guests_checking_in:
            if guest.is_clicked(pos):
                return guest
        return None

    def get_room_at_position(self, pos):
        for room in self.vacant_rooms:
            if room.is_clicked(pos):
                return room
        return None
