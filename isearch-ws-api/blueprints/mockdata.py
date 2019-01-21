verbose = 9 # all the debug prints

# use SerpAPI format for easy digest
data = {
    "search_metadata": {},
    "search_parameters": {},
    "search_information": {},
    "ads": [],
    "local_map": {},
    "local_results": [],
    "related_questions": [],
    "answer_box": {},
    "organic_results": [],
    "related_searches": [],
    "pagination": {}
    }

#mockdata[] = {}

mockDataKittens = {
    'search_metadata': {},
    'search_parameters': {'q': 'kittens'},
    'search_information': {'total_results': 'About 512,000,000 results'},
    'ads': [], 'local_map': {}, 'local_results': [],
    'related_questions': [], 'answer_box': {},
    'organic_results': [
      {'position': 0, 'title': 'How To Look After A Kitten | Purina', 'link': 'https://www.purina.com.au/kittens&sa=U&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QFgg3MAM&usg=AOvVaw1T4GNmMT3b2oQoB2Hn4SwQ', 'snippet': 'Purina Has Lots Of Vet Advice On Kitten Care, Including How To Feed And Train \nYour New Kitten, Designed To Help You And Your Kitten Live Happily Together.'},
      {'position': 1, 'title': 'Kittens Do Things For The First Time - YouTube', 'link': 'https://www.youtube.com/watch%3Fv%3Dc1c0a4fo1zo&sa=U&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QtwIIPTAE&usg=AOvVaw3_KNNoD4nPj1-jIO5G0apd', 'snippet': "Feb 26, 2015 - 1 min - Uploaded by BuzzFeedVideoCan you handle this level of cute? Check out Buzzfeed's new Cute Or Not app!  http://bit.ly ..."},
      {'position': 2, 'title': 'Kittens see / do things for the first time - Funny and cute cat ...', 'link': 'https://www.youtube.com/watch%3Fv%3DmmjlMgDSYFo&sa=U&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QtwIIQTAF&usg=AOvVaw3EQJOn9wSe-w9D3rUpwvUH', 'snippet': 'Apr 27, 2016 - 6 min - Uploaded by Tiger ProductionsPuppies see / do things for the first time - Funny and cute dog compilation : https:// www.youtube ...'},
      {'position': 3, 'title': 'News for kittens', 'link': '?q=kittens&hl=en&gl=us&ie=UTF-8&prmd=ivns&source=univ&tbm=nws&tbo=u&sa=X&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QqAIIRA', 'snippet': "What's being called the first-in-America kitten-only place to rest, relax and interact \nwith kittens between the ages of three-to-six months will open..."},
      {'position': 4, 'title': 'Why Adopt - Kitten Rescue', 'link': 'https://kittenrescue.org/adopt/&sa=U&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QFghNMAk&usg=AOvVaw0DQe-Py_NZ3-bZDtcKQ2XC', 'snippet': "Our work is most rewarding when we're able to adopt a cat or a kitten into a \nloving home. Adopting gives an animal a second chance at life."},
      {'position': 5, 'title': 'Kitten - Wikipedia', 'link': 'https://en.wikipedia.org/wiki/Kitten&sa=U&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QFghSMAo&usg=AOvVaw2D3pkMVRf1VyjdTccJZ-Ju', 'snippet': 'A kitten is a juvenile cat. After being born, kittens are totally dependent on their \nmother for survival and they do not normally open their eyes until after seven to...'},
      {'position': 6, 'title': 'Images for kittens', 'link': '?q=kittens&hl=en&gl=us&ie=UTF-8&prmd=ivns&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QsAQIWA', 'snippet': 'Kitten care and training information. ... Your new kitten deserves the best possible \nstart in life. ... Nutrition Tips for Kittens Kittens have special nutritional needs.'},
      {'position': 7, 'title': 'Healthy Cats Guide: Caring for Your Kitten - Healthy Pets - WebMD', 'link': 'https://pets.webmd.com/cats/guide/kitten-care&sa=U&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QFghkMBA&usg=AOvVaw2mP1n4nI57_Db_URP1dian', 'snippet': "(If you've been raising the kittens for a few weeks already, congratulations-the \nhardest part is over!) Kittens at this age will start weaning (meaning they'll slowly\n..."},
      {'position': 8, 'title': 'Alley Cat Allies | How Old Is That Kitten? Kitten Guide: Four Weeks', 'link': 'https://www.alleycat.org/resources/how-old-is-that-kitten-guide-four-weeks/&sa=U&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QFghpMBE&usg=AOvVaw1mZtemKX3mMpC0nQQqOvgm', 'snippet': "At about seven days old, kittens' ears will unfold and their eyes may start to open, \nthough their eyesight is still unfocused. They have doubled their birth weight to..."},
      {'position': 9, 'title': 'Alley Cat Allies | How Old Is That Kitten? Kitten Guide: One Week', 'link': 'https://www.alleycat.org/resources/how-old-is-that-kitten-guide-one-week/&sa=U&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QFghvMBI&usg=AOvVaw3qcxs_ZK2A03oNeq0EsqrP', 'snippet': ''}
    ],
    'related_searches': [
       {'query': 'kittens video', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=kittens+video&sa=X&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIdSgA'},
       {'query': 'kittens near me', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=kittens+near+me&sa=X&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIdigB'},
       {'query': 'kittens for sale', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=kittens+for+sale&sa=X&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIdygC'},
       {'query': 'kittens 2017', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=kittens+2017&sa=X&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIeCgD'},
       {'query': 'baby kittens', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=baby+kittens&sa=X&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIeSgE'},
       {'query': 'free kittens', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=free+kittens&sa=X&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIeigF'},
       {'query': 'kittens for adoption', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=kittens+for+adoption&sa=X&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIeygG'},
       {'query': 'lots of kittens', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=lots+of+kittens&sa=X&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIfCgH'}
    ],
    'pagination': {}
}

mockDataCats = {
          'search_metadata': {},
          'search_parameters': {'q': 'cats'},
          'search_information': {'total_results': 'About 5,030,000,000 results'},
          'ads': [], 'local_map': {}, 'local_results': [],
          'related_questions': [], 'answer_box': {},
          'organic_results': [
            {'position': 0, 'title': 'Cats the Musical - Official Website & Tickets', 'link': 'https://www.catsthemusical.com/&sa=U&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFggUMAA&usg=AOvVaw1tGzR0ChHcOE6VAFRtFUXl', 'snippet': "The official home of Andrew Lloyd Webber's world-famous, family-favourite \nmusical CATS - Tickets from $20 & NO booking fee!"},
            {'position': 1, 'title': 'Complete Guide to Caring for Cats | Cat Breed Information, Cat ...', 'link': 'http://www.vetstreet.com/cats/&sa=U&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFggZMAE&usg=AOvVaw3afMRFiGgWwZhhhwBzYnbi', 'snippet': "Your cat's online owners manual, featuring articles about breed information, cat \nselection, training, grooming and care for cats and kittens."},
            {'position': 2, 'title': 'Cat Breed Collection | Purina', 'link': 'https://www.purina.com/cats/cat-breeds&sa=U&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFggfMAI&usg=AOvVaw3Tg6RZQt3rYkusIsA-y-Bg', 'snippet': 'Trying to decide what type of cat is right for you and your family? Browse through \nour list of popular cat breeds, and find the best breed for your lifestyle.'},
            {'position': 3, 'title': 'News for cats', 'link': '?q=cats&hl=en&gl=us&ie=UTF-8&prmd=ivnsb&source=univ&tbm=nws&tbo=u&sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQqAIIJQ', 'snippet': 'A stray kitten appropriately named Loco started Mr. Chandoha on an unexpected \ncareer. By the time he died, he had taken some 90000 cat...'},
            {'position': 4, 'title': 'Cats | Animal Planet', 'link': 'http://www.animalplanet.com/pets/cats/&sa=U&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFgguMAY&usg=AOvVaw2U4ogL8tY1DG92EDQPkzQz', 'snippet': 'Explore our guide to cats, kittens and their habitats. Learn about over a hundred \ndifferent cat breeds and how to deal with troubled cats.'},
            {'position': 5, 'title': 'Cats: Adoption, Bringing A Cat Home and Care - Petfinder', 'link': 'https://www.petfinder.com/cats/&sa=U&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFgg0MAc&usg=AOvVaw0R_Hk5SBzL0yjJCg72g77j', 'snippet': 'Everything you need to know about how to adopt a cat, bringing your new cat \nhome, cat health and care and more!'},
            {'position': 6, 'title': 'Cats (musical) - Wikipedia', 'link': 'https://en.wikipedia.org/wiki/Cats_(musical)&sa=U&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFgg6MAg&usg=AOvVaw17khzwFW-gMi-s8RxuZRf_', 'snippet': "Cats is a sung-through musical composed by Andrew Lloyd Webber, based on \nOld Possum's Book of Practical Cats by T. S. Eliot. The musical tells the story of a\n..."},
            {'position': 7, 'title': 'Cat - Wikipedia', 'link': 'https://en.wikipedia.org/wiki/Cat&sa=U&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFghAMAk&usg=AOvVaw0QkzMUSua1IVxNeypH-8K4', 'snippet': 'The cat often referred to as the domestic cat to distinguish it from its wild relatives \nsuch as tigers, lions, and other felids and felines, is a small furry, carnivorous...'},
            {'position': 8, 'title': 'Cat Health Center | Cat Care and Information from WebMD', 'link': 'https://www.webmd.com/pets/cats/default.htm&sa=U&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFghGMAo&usg=AOvVaw19GXi0bR2FY7GvWIz4wGvy', 'snippet': 'WebMD veterinary experts provide comprehensive information about cat health \ncare, offer nutrition and feeding tips, and help you identify illnesses in cats.'},
            {'position': 9, 'title': 'Images for cats', 'link': '?q=cats&hl=en&gl=us&ie=UTF-8&prmd=ivnsb&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQsAQISw', 'snippet': ''}],
          'related_searches': [
            {'query': 'cats breeds', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=cats+breeds&sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIWCgA'},
            {'query': 'cute cats', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=cute+cats&sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIWSgB'},
            {'query': 'cats musical', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=cats+musical&sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIWigC'},
            {'query': 'facts about cats', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=facts+about+cats&sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIWygD'},
            {'query': 'cats broadway', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=cats+broadway&sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIXCgE'},
            {'query': 'c.a.t.s game', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=c.a.t.s+game&sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIXSgF'},
            {'query': 'cats for sale', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=cats+for+sale&sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIXigG'},
            {'query': 'cats movie', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=cats+movie&sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIXygH'}],
          'pagination': {}
        }

mockDataCars = {
          'search_metadata': {},
          'search_parameters': {'q': 'cars'},
          'search_information': {'total_results': 'About 11,000,000,000 results'},
          'ads': [], 'local_map': {}, 'local_results': [],
          'related_questions': [], 'answer_box': {},
          'organic_results': [
            {'position': 0, 'title': 'New Cars, Used Cars, Car Reviews and News | Cars.com', 'link': 'https://www.cars.com/&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQFggVMAA&usg=AOvVaw0pprhkLhExhjGt1J3H5Cuu', 'snippet': "Research and compare cars, find local dealers/sellers, calculate loan payments, \nfind your car's value, sell or trade your car, get a service estimate, and much\xa0..."},
            {'position': 1, 'title': 'Cars for Sale', 'link': 'https://www.cars.com/shopping/&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQjBAIHDAB&usg=AOvVaw2D3fPz3Vb3v2Of8c8f_9LY', 'snippet': 'Browse cars for sale on Cars.com. Shop the best deals near you ...'},
            {'position': 2, 'title': 'Sell Your Car', 'link': 'https://www.cars.com/sell/&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQjBAIHjAE&usg=AOvVaw1WScKS3NSObKItUiCtt3hc', 'snippet': 'Get offers from dealers and sell your car fast with Quick Offer ...'},
            {'position': 3, 'title': 'Advanced Search', 'link': 'https://www.cars.com/for-sale/advanced-search/&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQjBAIIDAC&usg=AOvVaw1dkVfLmYm2-w9gRoOAKVh0', 'snippet': 'Advanced search allows you to filter 4.9 million new & used cars ...'},
            {'position': 4, 'title': 'Sedans', 'link': 'https://www.cars.com/research/sedan/&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQjBAIIjAF&usg=AOvVaw1M6fPsd1ivUlHj6nFr5yi_', 'snippet': '2019 Toyota Camry\xa0- 2019 Dodge Charger\xa0- 2019 Honda Civic\xa0- ...'},
            {'position': 5, 'title': 'Research', 'link': 'https://www.cars.com/research/&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQjBAIJDAD&usg=AOvVaw1AaC1_Gv_JYHTPHUMSeZ10', 'snippet': 'Start your research for your next car by comparing popular ...'},
            {'position': 6, 'title': 'SUV or Crossovers', 'link': 'https://www.cars.com/research/suv/&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQjBAIJjAG&usg=AOvVaw2W9RNOoIMBl82mbBTxeeIp', 'snippet': '2019 Jeep Grand Cherokee\xa0- 2019 Jeep Cherokee\xa0- 2019 BMW X5'},
            {'position': 7, 'title': 'News for cars', 'link': '?q=cars&hl=en&gl=us&ie=UTF-8&prmd=ivns&source=univ&tbm=nws&tbo=u&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQqAIIKQ', 'snippet': 'After kick-starting the electric car market in America with its high-priced luxury \nvehicles, Tesla has been attempting to transition to the mass\xa0...'},
            {'position': 8, 'title': 'Images for cars', 'link': '?q=cars&hl=en&gl=us&ie=UTF-8&prmd=ivns&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQsAQIUg', 'snippet': 'Search for new and used cars at carmax.com. Use our car search or research \nmakes and models with customer reviews, expert reviews, and more.'},
            {'position': 9, 'title': 'Used Cars for Sale - CarMax', 'link': 'https://www.carmax.com/cars&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQFghcMBE&usg=AOvVaw1SvonetHYi-LqDrRlyNce_', 'snippet': 'Search new car listings to find the best local deals. We analyze millions of used \ncars daily.'},
            {'position': 10, 'title': 'New Cars For Sale. Find new cars in your area. - CarGurus', 'link': 'https://www.cargurus.com/Cars/new/&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQFghiMBI&usg=AOvVaw2QxLkhvaBOsIjZqaImsFh4', 'snippet': 'A hot-shot race-car named Lightning McQueen gets waylaid in Radiator Springs, where he finds the true meaning of friendship and family.\n ... John Lasseter, Joe Ranft (co-director)\n ... Star race car Lightning McQueen and his pal Mater head overseas to compete in the World Grand Prix race.'},
            {'position': 11, 'title': 'Cars (2006) - IMDb', 'link': 'https://www.imdb.com/title/tt0317219/&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQFghoMBM&usg=AOvVaw0Ro2X2ojHvAr5TyRD1c4lM', 'snippet': 'Find new cars and used cars for sale at Autotrader. With millions of cars, find your \nnext car at the most complete auto classifieds site online.'},
            {'position': 12, 'title': 'Search for Cars For Sale Online - Find a Car at Autotrader', 'link': 'https://www.autotrader.com/cars-for-sale/&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQFghuMBQ&usg=AOvVaw0ojI6n7YzzoPb9tEVzUFTv', 'snippet': ''}],
          'related_searches': [
            {'query': 'cars for sale', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=cars+for+sale&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIdCgA'},
            {'query': 'cars for sale near me', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=cars+for+sale+near+me&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIdSgB'},
            {'query': 'used cars', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=used+cars&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIdigC'},
            {'query': 'cars movie', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=cars+movie&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIdygD'},
            {'query': 'used cars for sale', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=used+cars+for+sale&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIeCgE'},
            {'query': 'cool cars', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=cool+cars&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIeSgF'},
            {'query': 'new cars', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=new+cars&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIeigG'},
            {'query': 'car guru', 'link': '/search?hl=en&gl=us&ie=UTF-8&q=car+guru&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIeygH'}],
          'pagination': {}
	}
