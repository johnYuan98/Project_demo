class Video:
    def __init__(self, title, director, producer, video_type):
        self.title = title
        self.director = director
        self.producer = producer
        self.video_type = video_type
        self.is_rented = False

    def __str__(self):
        return f"{self.title} ({self.video_type}) by {self.director}, produced by {self.producer}{' (rented)' if self.is_rented else ''}"


class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.rented_videos = []

    def __str__(self):
        return f"{self.name} (Address: {self.address}, Phone: {self.phone})"


class VideoStore:
    def __init__(self):
        self.customers = []
        self.videos = []

    def add_video(self, video):
        self.videos.append(video)
        print("Video added successfully!")

    def delete_video(self, title):
        for video in self.videos:
            if video.title == title:
                if video.is_rented:
                    print("This video is currently rented and cannot be deleted!")
                    return
                self.videos.remove(video)
                print("Video deleted successfully!")
                return
        print("Video not found!")

    def add_customer(self, customer):
        self.customers.append(customer)
        print("Customer added successfully!")

    def delete_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                if customer.rented_videos:
                    print("This customer has rented videos and cannot be deleted!")
                    return
                self.customers.remove(customer)
                print("Customer deleted successfully!")
                return
        print("Customer not found!")

    def check_video_in_store(self, title):
        for video in self.videos:
            if video.title == title:
                if video.is_rented:
                    print("This video is currently rented.")
                else:
                    print("This video is available in store.")
                return
        print("Video not found!")

    def checkout_video(self, customer_name, title):
        for customer in self.customers:
            if customer.name == customer_name:
                for video in self.videos:
                    if video.title == title:
                        if video.is_rented:
                            print("This video is currently rented.")
                            return
                        video.is_rented = True
                        customer.rented_videos.append(video)
                        print(f"{video.title} rented to {customer.name} successfully!")
                        return
                print("Video not found!")
                return
        print("Customer not found!")

    def checkin_video(self, title):
        for customer in self.customers:
            for video in customer.rented_videos:
                if video.title == title:
                    video.is_rented = False
                    customer.rented_videos.remove(video)
                    print(f"{video.title} checked in successfully!")
                    return
        print("Video not found!")

    def print_all_customers(self):
        if not self.customers:
            print("No customers found!")
            return
        for customer in self.customers:
            print(customer)

    def print_all_videos(self):
        if not self.videos:
            print("No videos found!")
            return
        for video in self.videos:
            print(video)

    def print_in_store_videos(self):
        in_store_videos = [video for video in self.videos if not video.is_rented]
        if not in_store_videos:
            print("No in store videos found!")
            return
        for video in in_store_videos:
            print(video)

    def print_rent_videos(self):
        rent_videos = [video for video in self.videos if video.is_rented]
        if not rent_videos:
            print("No rent videos found!")
            return
        for video in rent_videos:
            print(video)

    def print_videos_rent_by_customer(self, customer_name):
        for customer in self.customers:
            if customer.name == customer_name:
                if not customer.rented_videos:
                    print("This customer has not rented any videos!")
                    return
                for video in customer.rented_videos:
                    print(video)
                return
        print("Customer not found!")


def main():
    video_store = VideoStore()
    while True:
        print("Select one of the following:")
        print("1: To add a video")
        print("2: To delete a video")
        print("3: To add a customer")
        print("4: To delete a customer")
        print("5: To check if a particular video is in store")
        print("6: To check out a video")
        print("7: To check in a video")
        print("8: To print all customers")
        print("9: To print all videos")
        print("10: To print in store videos")
        print("11: To print all rent videos")
        print("12: To print the videos rent by a customer")
        print("13: To exit")
        option = int(input())

        if option == 1:
            title = input("Please enter the video title: ")
            director = input("Please enter the video director: ")
            producer = input("Please enter the video producer: ")
            video_type = input("Please enter the video type (VHS, DVD, Blu-ray): ")
            video = Video(title, director, producer, video_type)
            video_store.add_video(video)
        elif option == 2:
            title = input("Please enter the video title: ")
            video_store.delete_video(title)
        elif option == 3:
            name = input("Please enter the customer name: ")
            address = input("Please enter the customer address: ")
            phone = input("Please enter the customer phone: ")
            customer = Customer(name, address, phone)
            video_store.add_customer(customer)
        elif option == 4:
            name = input("Please enter the customer name: ")
            video_store.delete_customer(name)
        elif option == 5:
            title = input("Please enter the video title: ")
            video_store.check_video_in_store(title)
        elif option == 6:
            name = input("Please enter the customer name: ")
            title = input("Please enter the video title: ")
            video_store.checkout_video(name, title)
        elif option == 7:
            title = input("Please enter the video title: ")
            video_store.checkin_video(title)
        elif option == 8:
            video_store.print_all_customers()
        elif option == 9:
            video_store.print_all_videos()
        elif option == 10:
            video_store.print_in_store_videos()
        elif option == 11:
            video_store.print_rent_videos()
        elif option == 12:
            name = input("Please enter the customer name: ")
            video_store.print_videos_rent_by_customer(name)
        elif option == 13:
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


main()
