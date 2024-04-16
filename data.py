#theater
def add_theater(ID,name):
    file_a("theater.txt",ID+'/'+name+'\n')
    
def get_theater_list():
    theater_list=file_r("theater.txt")
    return theater_list

#seat
def add_seat(seat_ID,theater_ID,seat_num):
    file_a("seat.txt",seat_ID+'/' +theater_ID+'/'+seat_num+'\n')
    
def get_seat_list():
    seat_list=file_r("seat.txt")
    return seat_list

#movie
def add_movie(ID,name,time):
    file_a("movie.txt",ID+'/'+name+'/'+time+'\n')
    
def get_movie_list():
    movie_list=file_r("movie.txt")
    return movie_list

#schedule
def add_schedule(timetable_ID,theater_ID,movie_ID,date,time):
    file_a("schedule.txt",timetable_ID+'/'+theater_ID+'/'+movie_ID+'/'+date+'/'+time+'\n')
    
def get_schedule_list():
    schedule_list=file_r("schedule.txt")
    return schedule_list

#ticket
def add_ticket(ticket_ID,reservation_ID,seat_ID,timetable_ID):
    file_a("ticket.txt",ticket_ID+'/'+reservation_ID+'/'+seat_ID+'/'+timetable_ID+'\n')
    
def get_ticket_list():
    ticket_list=file_r("ticket.txt")
    return ticket_list

#reservation
def add_reservation(reservation_ID,reservation_person_ID,num,cancel):
    file_a("reservation.txt",reservation_ID+'/'+reservation_person_ID+'/'+num+'/'+cancel+'\n')
    
def get_reservation_list():
    ticket_list=file_r("reservation.txt")
    return ticket_list
        
#user
def add_user(reservation_person_ID,password):
    file_a("reservation.txt",reservation_person_ID+'/'+password+'\n')
    
def get_user_list():
    user_list=file_r("reservation.txt")
    return user_list


def file_a(path,content):
    f = open(path,'a',encoding='utf-8')
    f.write(content)
    f.close()

def file_i(path,content):
    f = open(path,'w',encoding='utf-8')
    f.write(content)
    f.close()
    
def file_r(path):
    f = open(path,'r',encoding='utf-8')
    data_list=f.readlines()
    f.close()
    return data_parsing(data_list)

#base function
def data_parsing(array):
    parsed_data=[]
    for str in array:
        row = str.strip().split('/')
        parsed_data.append(row)
    return parsed_data

def sort_data(data_list,index):
    return sorted(data_list,key=lambda x:x[index])
