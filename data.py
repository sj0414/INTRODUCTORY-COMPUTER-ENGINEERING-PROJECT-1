#theater
def add_Theater(ID,name):
    File_A("theater.txt",ID+'/'+name+'\n')
    
def get_Theater_list():
    theater_list=File_R("theater.txt")
    return theater_list

#seat
def add_Seat(seat_ID,theater_ID,seat_num):
    File_A("seat.txt",seat_ID+'/' +theater_ID+'/'+seat_num+'\n')
    
def get_Seat_list():
    seat_list=File_R("seat.txt")
    return seat_list

#movie
def add_Movie(ID,name,time):
    File_A("movie.txt",ID+'/'+name+'/'+time+'\n')
    
def get_Movie_list():
    movie_list=File_R("movie.txt")
    return movie_list

#schedule
def add_Schedule(timetable_ID,theater_ID,movie_ID,date,time):
    File_A("schedule.txt",timetable_ID+'/'+theater_ID+'/'+movie_ID+'/'+date+'/'+time+'\n')
    
def get_Schedule_list():
    schedule_list=File_R("schedule.txt")
    return schedule_list

#ticket
def add_ticket(ticket_ID,reservation_ID,seat_ID,timetable_ID):
    File_A("ticket.txt",ticket_ID+'/'+reservation_ID+'/'+seat_ID+'/'+timetable_ID+'\n')
    
def get_ticket_list():
    ticket_list=File_R("ticket.txt")
    return ticket_list

#reservation
def add_reservation(reservation_ID,reservation_person_ID,num,cancel):
    File_A("reservation.txt",reservation_ID+'/'+reservation_person_ID+'/'+num+'/'+cancel+'\n')
    
def get_reservation_list():
    ticket_list=File_R("reservation.txt")
    return ticket_list
        
#user
def add_user(reservation_person_ID,password):
    File_A("reservation.txt",reservation_person_ID+'/'+password+'\n')
    
def get_user_list():
    user_list=File_R("reservation.txt")
    return user_list


def File_A(path,content):
    f = open(path,'a',encoding='utf-8')
    f.write(content)
    f.close()

def File_I(path,content):
    f = open(path,'w',encoding='utf-8')
    f.write(content)
    f.close()
    
def File_R(path):
    f = open(path,'r',encoding='utf-8')
    data_list=f.read()
    f.close()
    return data_parsing(data_list)

#base function
def data_parsing(array):
    parsed_data=[]
    for str in array:
        str.split('/')
        parsed_data.append(str)
    return parsed_data

def sort_data(data_list,index):
    return sorted(data_list,key=lambda x:x[index])

