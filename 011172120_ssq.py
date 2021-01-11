import numpy as np


class SSQ:
    def __init__(self, option, till=6):  # Initialization
        np.random.seed(0)
        self.interarrivals = list(np.random.exponential(1.2, 100))
        self.service_times = list(np.random.exponential(1.3, 100))

        self.clock = 0.0

        self.next_arrival = self.interarrivals.pop(0)
        self.next_departure1 = float('inf')
        self.next_departure2 = float('inf')

        self.num_in_queue = 0
        # store times of arrivals who are waiting in the queue
        self.times_of_arrivalqueue = []
        # store service times of waiting customers in the queue
        self.service_times_in_queue = []

        self.total_delay = 0.0
        self.num_of_delays = 0.0
        self.area_under_q = 0.0
        self.area_under_b1 = 0.0
        self.area_under_b2 = 0.0

        self.server1_status = 0  # 0 for IDLE , 1 for BUSY
        self.server2_status = 0
        self.last_event_time = 0.0  # we will need to store last event clock time
        self.option = option
        self.prev_num_q = 0
        self.prev_srvr1_stat = 0
        self.prev_srvr2_stat = 0
        self.till = till

    def start(self):
        while self.num_of_delays < self.till:
            self.timing()

    def timing(self):
        # First set clock to minimum time of next event
        self.clock = min(self.next_arrival,
                         self.next_departure1, self.next_departure2)
        self.update_register()
        if self.next_arrival <= self.next_departure1 and self.next_arrival <= self.next_departure2:
            self.arrival()
            #print("Arrival at Clock:" +str(self.clock))

        elif self.next_departure1 <= self.next_arrival and self.next_departure1 <= self.next_departure2:
            self.departure1()
            #print("Departure at "+str(self.clock))

        else:
            self.departure2()
        #print("Next Arrival Time: "+str(self.next_arrival))
        #print("Next Departure Time of sever 1: "+str(self.next_departure1))
        #print("Next Departure Time of sever 2: "+str(self.next_departure2))
        #print("Server 1 Status:"+str(self.server1_status))
        #print("Server 2 Status:"+str(self.server2_status))
        #print("Times of arrivals in Queue: "+ str(self.times_of_arrivalqueue))
        #print("Service times in Queue: "+str(self.service_times_in_queue))
        #print("Total Delay:" +str(self.total_delay))
        #print("Number of customers delayed: ",self.num_of_delays)
        #print(" ")

    def arrival(self):
        # Schedule next arrival , new_arrival = previous_arrival + inter_arrival time of next customer
        self.next_arrival = self.next_arrival + self.interarrivals.pop(0)

        if self.server1_status == 0:  # server is idle
            self.server1_status = 1  # make server BUSY
            delay = 0.0  # so delay is zero
            self.total_delay += delay
            self.num_of_delays += 1  # increase the number of customers delayed

            # schedule next departure, pop the first element of service_times list to get service time of this customer
            self.next_departure1 = self.clock + self.service_times.pop(0)

        elif self.server2_status == 0:  # server is idle  ***change*****
            self.server2_status = 1  # make server BUSY
            delay = 0.0  # so delay is zero
            self.total_delay += delay
            self.num_of_delays += 1  # increase the number of customers delayed

            # schedule next departure, pop the first element of service_times list to get service time of this customer
            self.next_departure2 = self.clock + self.service_times.pop(0)

        else:  # Server is BUSY
            # increase queue length, this customer will have to wait in the queue
            self.num_in_queue += 1

            # store the arrival time and service time of this customer in seperate lists
            self.times_of_arrivalqueue.append(self.clock)
            self.service_times_in_queue.append(self.service_times.pop(0))

    def departure1(self):  # depart from server-1
        # check number of customers in the queue
        if self.num_in_queue == 0:  # if no customer in the queue
            # make server IDLE
            self.server1_status = 0
            # schedule next departure= infinity
            self.next_departure1 = float('inf')

        else:
            # if queue not empty, pop one customer, decrease queue length
            self.num_in_queue -= 1
            self.num_of_delays += 1
            # AS FIFO, pop first arrival and service time from the queue. IF LIFO we have to pop last arrival and service time
            # For SJF, finf the index of minimum service time from  service_times_in_queue list.
            # Then pop the arrival of that index from times_of_arrivalqueue for delay count and others.
            if self.option == 1:
                arrival = self.times_of_arrivalqueue.pop(0)
                dpt = self.service_times_in_queue.pop(0)    # ***change****
            elif self.option == 2:
                arrival = self.times_of_arrivalqueue.pop(-1)
                dpt = self.service_times_in_queue.pop(-1)
            elif self.option == 3:
                min_ind = self.service_times_in_queue.index(
                    min(self.service_times_in_queue))
                arrival = self.times_of_arrivalqueue.pop(min_ind)
                dpt = self.service_times_in_queue.pop(min_ind)

            delay = self.clock - arrival
            self.total_delay += delay
            self.next_departure1 = self.clock + dpt  # ***change***

    def departure2(self):  # depart from server-2
        # check number of customers in the queue
       # check number of customers in the queue
        if self.num_in_queue == 0:  # if no customer in the queue
            # make server IDLE
            self.server2_status = 0
            # schedule next departure= infinity
            self.next_departure2 = float('inf')

        else:
            # if queue not empty, pop one customer, decrease queue length
            self.num_in_queue -= 1
            self.num_of_delays += 1
            # AS FIFO, pop first arrival and service time from the queue. IF LIFO we have to pop last arrival and service time
            # For SJF, finf the index of minimum service time from  service_times_in_queue list.
            # Then pop the arrival of that index from times_of_arrivalqueue for delay count and others.
            if self.option == 1:
                arrival = self.times_of_arrivalqueue.pop(0)
                dpt = self.service_times_in_queue.pop(0)
            elif self.option == 2:
                arrival = self.times_of_arrivalqueue.pop(-1)
                dpt = self.service_times_in_queue.pop(-1)
            elif self.option == 3:
                min_ind = self.service_times_in_queue.index(
                    min(self.service_times_in_queue))
                arrival = self.times_of_arrivalqueue.pop(min_ind)
                dpt = self.service_times_in_queue.pop(min_ind)

            delay = self.clock - arrival
            self.total_delay += delay
            self.next_departure2 = self.clock + dpt

    def update_register(self):
        time_difference = self.clock - self.last_event_time
        # print(self.prev_num_q)
        self.area_under_q += time_difference * self.prev_num_q
        self.area_under_b1 += time_difference * self.prev_srvr1_stat
        self.area_under_b2 += time_difference * self.prev_srvr2_stat
        self.last_event_time = self.clock
        self.prev_num_q = self.num_in_queue
        self.prev_srvr1_stat = self.server1_status
        self.prev_srvr2_stat = self.server2_status


option = [1, 2, 3]
num_delays = [10, 30, 60]
for i in num_delays:
    for j in option:
        s = SSQ(j, i)
        s.start()
        print("for {} delay and {} option".format(i, j))
        #print(s.area_under_q, s.area_under_b1, s.area_under_b2, s.last_event_time)
        print("Avg delay: ", s.total_delay/s.num_of_delays)
        print("Expected num in queue: ", s.area_under_q/s.clock)
        print("Expected util of server 1: ", s.area_under_b1/s.clock)
        print("Expected util of server 2: ", s.area_under_b2/s.clock)
        print()
