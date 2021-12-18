import json
from pathlib import Path
import random
from pybooru import Danbooru
import urllib.request

class Ip:
    def __init__(self):
        self.__ip_list = []

        ip_filename = '../repository/ips.json'
        self.mod_path = Path(__file__).parent
        ip_file_path = (self.mod_path / ip_filename).resolve()
        with open(ip_file_path, 'r') as ip_file:
            self.__ip_list.extend(json.load(ip_file))

    def __update(self):
        ip_filename = '../repository/ips.json'
        ip_file_path = (self.mod_path / ip_filename).resolve()
        with open(ip_file_path, 'w') as ip_file:
            json.dump(self.__ip_list, ip_file)

    def get_all(self):
        return self.__ip_list

    def get_ip(self):
        """Gets a random ip from the list (with timesshown affecting priority)

        Returns:
            string: IP string
        """
        self.__ip_list.sort(key = lambda ip : ip[1]) # sort by number of times shown

        random_range = -1
        for i in range(len(self.__ip_list)-1):
            if self.__ip_list[i][1] < self.__ip_list[i+1][1]:
                random_range = i
                break
        if random_range == -1: random_range = len(self.__ip_list)

        random_index = random.randint(0, random_range)

        ip = self.__ip_list[random_index][0]
        self.__ip_list[random_index][1] += 1

        self.__update()
        return ip

class BooruTool:
    def __init__(self):
        self.booru = Danbooru('danbooru')
        self.image_directory = '../images/'
        self.mod_path = Path(__file__).parent
        self.image_directory_path = (self.mod_path / self.image_directory).resolve()

    def get_random(self, query):
        random_page = random.randint(1, 500)
        posts = self.booru.post_list(tags=query, page=random_page, limit=20)
        random_post = posts[random.randint(1, 20)]
        try:
            post_url = random_post['file_url']
        except:
            post_url = 'https://danbooru.donmai.us' + random_post['source']
        
        return post_url
        '''
        try:
            randomint = random.randint(1000, 10000000)
            print (self.image_directory_path)
            print (post_url)
            image_path = (self.image_directory_path / randomint + ".jpg")
            print (image_path)
            urllib.request.urlretrieve(post_url, image_path)
            return image_path
        except:
            print("could not download image")
        '''