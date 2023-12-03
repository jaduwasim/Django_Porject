from django.db import models

# Create your models here.
class Country(models.Model):
    '''This is Country Model which have two field id, name'''
    name = models.CharField(max_length=64, unique=True)
    class Meta:
        '''Her iam defining Table name for Country'''
        db_table = 'country'

    def __str__(self) -> str:
        return f'{self.name}'
    
class City(models.Model):
    '''This is City Model which is depend on Contry with foreign Key'''
    name = models.CharField(max_length=64, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()
    class Meta:
        '''Here we are Defining Table Name for City Table'''
        db_table = 'city'

    def __str__(self) -> str:
        return f'{self.name}'


# from django.db.models import Sum

# # Find Population from Each Country
# # Way First, Which is Always Recommended....
# data = City.objects.values('country__name').annotate(Sum('population'))

# # Way Second, Which not Recommended, but we can use
# for country in Country.objects.all():
#     result = City.objects.filter(country=country).aggregate(Sum('population'))
#     print('{}: {}'.format(country.name, result['population__sum']))


# Country.objects.bulk_create([
# Country(name='Brazil'),
# Country(name='Turkey'),
# Country(name='Italy'),
# Country(name='Bangladesh'),
# Country(name='Canada'),
# Country(name='France'),
# Country(name='Peru'),
# Country(name='Argentina'),
# Country(name='Nigeria'),
# Country(name='Australia'),
# Country(name='Iran'),
# Country(name='Singapore'),
# Country(name='China'),
# Country(name='Chile'),
# Country(name='Thailand'),
# Country(name='Germany'),
# Country(name='Spain'),
# Country(name='Philippines'),
# Country(name='Indonesia'),
# Country(name='United States'),
# Country(name='South Korea'),
# Country(name='Pakistan'),
# Country(name='Angola'),
# Country(name='Mexico'),
# Country(name='India'),
# Country(name='United Kingdom'),
# Country(name='Colombia'),
# Country(name='Japan'),
# Country(name='Taiwan')])



# For United States 
# country = Country.objects.get(name="United States")
# city_data = [
#     City(name="Chicago", country=country, population=2705994),
#     City(name="Houston", country=country, population=2320268),
#     City(name="Phoenix", country=country, population=1680992),
#     City(name="Philadelphia", country=country, population=1584064),
#     City(name="San Antonio", country=country, population=1552164),
#     City(name="San Diego", country=country, population=1425976),
#     City(name="Dallas", country=country, population=1343573),
#     City(name="San Jose", country=country, population=1030119),
#     City(name="Austin", country=country, population=978908),
#     City(name="Jacksonville", country=country, population=911507),
# ]
# City.objects.bulk_create(city_data)


# for japan
# country_japan = Country.objects.get(name="Japan")
# japan_city_data = [
#     City(name="Tokyo", country=country_japan, population=13929286),
#     City(name="Yokohama", country=country_japan, population=3726167),
#     City(name="Osaka", country=country_japan, population=2673880),
#     City(name="Nagoya", country=country_japan, population=2351689),
#     City(name="Sapporo", country=country_japan, population=1973115),
#     City(name="Fukuoka", country=country_japan, population=1538233),
#     City(name="Kobe", country=country_japan, population=1528478),
#     City(name="Kyoto", country=country_japan, population=1474570),
#     City(name="Kawasaki", country=country_japan, population=1472475),
#     City(name="Saitama", country=country_japan, population=1320088),
# ]
# City.objects.bulk_create(japan_city_data)


# for Brazil
# country_brazil = Country.objects.get(name="Brazil")  # Replace with the desired country name
# # Create a list of City instances for Brazil with the desired data
# brazil_city_data = [
#     City(name="Sao Paulo", country=country_brazil, population=12325232),
#     City(name="Rio de Janeiro", country=country_brazil, population=6747815),
#     City(name="Salvador", country=country_brazil, population=2886692),
#     City(name="Brasilia", country=country_brazil, population=3055149),
#     City(name="Fortaleza", country=country_brazil, population=2669342),
#     City(name="Belo Horizonte", country=country_brazil, population=2512070),
#     City(name="Manaus", country=country_brazil, population=2219580),
#     City(name="Curitiba", country=country_brazil, population=1933105),
#     City(name="Recife", country=country_brazil, population=1633697),
#     City(name="Porto Alegre", country=country_brazil, population=1484941),
#     # Add more City instances for Brazil as needed
# ]

# # Use the bulk_create method to insert all the cities for Brazil into the database efficiently
# City.objects.bulk_create(brazil_city_data)


# for Truky
# country_turkey = Country.objects.get(name="Turkey")  # Replace with the desired country name

# # Create a list of City instances for Turkey with the desired data
# turkey_city_data = [
#     City(name="Istanbul", country=country_turkey, population=15519267),
#     City(name="Ankara", country=country_turkey, population=5568623),
#     City(name="Izmir", country=country_turkey, population=4390706),
#     City(name="Bursa", country=country_turkey, population=2974963),
#     City(name="Adana", country=country_turkey, population=2258715),
#     City(name="Gaziantep", country=country_turkey, population=2019275),
#     City(name="Konya", country=country_turkey, population=2100411),
#     City(name="Antalya", country=country_turkey, population=2385141),
#     City(name="Mersin", country=country_turkey, population=1660780),
#     City(name="Diyarbakir", country=country_turkey, population=1437939),
#     # Add more City instances for Turkey as needed
# ]

# # Use the bulk_create method to insert all the cities for Turkey into the database efficiently
# City.objects.bulk_create(turkey_city_data)


# for Italy

# Find a country for which you want to insert cities (you can create a new one if needed)
# country_italy = Country.objects.get(name="Italy")  # Replace with the desired country name

# # Create a list of City instances for Italy with the desired data
# italy_city_data = [
#     City(name="Rome", country=country_italy, population=2870493),
#     City(name="Milan", country=country_italy, population=1399860),
#     City(name="Naples", country=country_italy, population=967069),
#     City(name="Turin", country=country_italy, population=877215),
#     City(name="Palermo", country=country_italy, population=663173),
#     City(name="Genoa", country=country_italy, population=586180),
#     City(name="Bologna", country=country_italy, population=388367),
#     City(name="Florence", country=country_italy, population=377207),
#     City(name="Venice", country=country_italy, population=260352),
#     City(name="Verona", country=country_italy, population=257353),
#     # Add more City instances for Italy as needed
# ]

# # Use the bulk_create method to insert all the cities for Italy into the database efficiently
# City.objects.bulk_create(italy_city_data)



# for Bangladesh
# Import the necessary models
# Find a country for which you want to insert cities (you can create a new one if needed)
# country_bangladesh = Country.objects.get(name="Bangladesh")  # Replace with the desired country name

# # Create a list of City instances for Bangladesh with the desired data
# bangladesh_city_data = [
#     City(name="Dhaka", country=country_bangladesh, population=8105445),
#     City(name="Chittagong", country=country_bangladesh, population=2637643),
#     City(name="Khulna", country=country_bangladesh, population=1556144),
#     City(name="Rajshahi", country=country_bangladesh, population=700133),
#     City(name="Sylhet", country=country_bangladesh, population=479837),
#     City(name="Barisal", country=country_bangladesh, population=328278),
#     City(name="Comilla", country=country_bangladesh, population=325013),
#     City(name="Narayanganj", country=country_bangladesh, population=210221),
#     City(name="Rangpur", country=country_bangladesh, population=285564),
#     City(name="Dinajpur", country=country_bangladesh, population=197110),
#     # Add more City instances for Bangladesh as needed
# ]
# # Use the bulk_create method to insert all the cities for Bangladesh into the database efficiently
# City.objects.bulk_create(bangladesh_city_data)



# For Canada
# Find a country for which you want to insert cities (you can create a new one if needed)
# country_canada = Country.objects.get(name="Canada")  # Replace with the desired country name

# # Create a list of City instances for Canada with the desired data
# canada_city_data = [
#     City(name="Toronto", country=country_canada, population=2731571),
#     City(name="Montreal", country=country_canada, population=1704694),
#     City(name="Vancouver", country=country_canada, population=631486),
#     City(name="Calgary", country=country_canada, population=1239220),
#     City(name="Edmonton", country=country_canada, population=979938),
#     City(name="Ottawa", country=country_canada, population=934243),
#     City(name="Winnipeg", country=country_canada, population=705244),
#     City(name="Quebec City", country=country_canada, population=542298),
#     City(name="Hamilton", country=country_canada, population=536917),
#     City(name="Kitchener", country=country_canada, population=417001),
#     # Add more City instances for Canada as needed
# ]

# # Use the bulk_create method to insert all the cities for Canada into the database efficiently
# City.objects.bulk_create(canada_city_data)

# For France
# country_france = Country.objects.get(name="France")  # Replace with the desired country name

# # Create a list of City instances for France with the desired data
# france_city_data = [
#     City(name="Paris", country=country_france, population=2140526),
#     City(name="Marseille", country=country_france, population=870018),
#     City(name="Lyon", country=country_france, population=515695),
#     City(name="Toulouse", country=country_france, population=479553),
#     City(name="Nice", country=country_france, population=342637),
#     City(name="Nantes", country=country_france, population=309346),
#     City(name="Strasbourg", country=country_france, population=284677),
#     City(name="Montpellier", country=country_france, population=275318),
#     City(name="Bordeaux", country=country_france, population=252040),
#     City(name="Lille", country=country_france, population=232787),
#     # Add more City instances for France as needed
# ]

# # Use the bulk_create method to insert all the cities for France into the database efficiently
# City.objects.bulk_create(france_city_data)


# for Peru
# Find a country for which you want to insert cities (you can create a new one if needed)
# country_peru = Country.objects.get(name="Peru")  # Replace with the desired country name

# # Create a list of City instances for Peru with the desired data
# peru_city_data = [
#     City(name="Lima", country=country_peru, population=9759046),
#     City(name="Arequipa", country=country_peru, population=1015414),
#     City(name="Trujillo", country=country_peru, population=821908),
#     City(name="Chiclayo", country=country_peru, population=734713),
#     City(name="Piura", country=country_peru, population=484475),
#     City(name="Iquitos", country=country_peru, population=437620),
#     City(name="Cusco", country=country_peru, population=435114),
#     City(name="Chimbote", country=country_peru, population=422287),
#     City(name="Huancayo", country=country_peru, population=370046),
#     City(name="Tacna", country=country_peru, population=318747),
#     # Add more City instances for Peru as needed
# ]

# # Use the bulk_create method to insert all the cities for Peru into the database efficiently
# City.objects.bulk_create(peru_city_data)


# # for Argentina
# # Find a country for which you want to insert cities (you can create a new one if needed)
# country_argentina = Country.objects.get(name="Argentina")  # Replace with the desired country name

# # Create a list of City instances for Argentina with the desired data
# argentina_city_data = [
#     City(name="Buenos Aires", country=country_argentina, population=2891082),
#     City(name="Cordoba", country=country_argentina, population=1541596),
#     City(name="Rosario", country=country_argentina, population=1358913),
#     City(name="Mendoza", country=country_argentina, population=1160277),
#     City(name="Tucuman", country=country_argentina, population=818190),
#     City(name="La Plata", country=country_argentina, population=765378),
#     City(name="Mar del Plata", country=country_argentina, population=614350),
#     City(name="Salta", country=country_argentina, population=535303),
#     City(name="Santa Fe", country=country_argentina, population=506282),
#     City(name="San Juan", country=country_argentina, population=474155),
#     # Add more City instances for Argentina as needed
# ]

# # Use the bulk_create method to insert all the cities for Argentina into the database efficiently
# City.objects.bulk_create(argentina_city_data)



# for Nigeria

# Find a country for which you want to insert cities (you can create a new one if needed)
# country_nigeria = Country.objects.get(name="Nigeria")  # Replace with the desired country name
# # Create a list of City instances for Nigeria with the desired data
# nigeria_city_data = [
#     City(name="Lagos", country=country_nigeria, population=16060303),
#     City(name="Kano", country=country_nigeria, population=3140000),
#     City(name="Ibadan", country=country_nigeria, population=3200000),
#     City(name="Kaduna", country=country_nigeria, population=1580000),
#     City(name="Port Harcourt", country=country_nigeria, population=1380000),
#     City(name="Benin City", country=country_nigeria, population=1125058),
#     City(name="Maiduguri", country=country_nigeria, population=1112449),
#     City(name="Zaria", country=country_nigeria, population=975153),
#     City(name="Aba", country=country_nigeria, population=897560),
#     City(name="Jos", country=country_nigeria, population=900000),
#     # Add more City instances for Nigeria as needed
# ]

# # Use the bulk_create method to insert all the cities for Nigeria into the database efficiently
# City.objects.bulk_create(nigeria_city_data)



# For Australia
# Find a country for which you want to insert cities (you can create a new one if needed)
# country_australia = Country.objects.get(name="Australia")  # Replace with the desired country name
# # Create a list of City instances for Australia with the desired data
# australia_city_data = [
#     City(name="Sydney", country=country_australia, population=5311900),
#     City(name="Melbourne", country=country_australia, population=5078191),
#     City(name="Brisbane", country=country_australia, population=2514184),
#     City(name="Perth", country=country_australia, population=2081445),
#     City(name="Adelaide", country=country_australia, population=1308737),
#     City(name="Gold Coast", country=country_australia, population=591473),
#     City(name="Newcastle", country=country_australia, population=308308),
#     City(name="Canberra", country=country_australia, population=447457),
#     City(name="Sunshine Coast", country=country_australia, population=345344),
#     City(name="Wollongong", country=country_australia, population=303635),
#     # Add more City instances for Australia as needed
# ]

# # Use the bulk_create method to insert all the cities for Australia into the database efficiently
# City.objects.bulk_create(australia_city_data)


# for Iran
# Find a country for which you want to insert cities (you can create a new one if needed)
# country_iran = Country.objects.get(name="Iran")  # Replace with the desired country name

# # Create a list of City instances for Iran with the desired data
# iran_city_data = [
#     City(name="Tehran", country=country_iran, population=8693706),
#     City(name="Mashhad", country=country_iran, population=3204000),
#     City(name="Isfahan", country=country_iran, population=1754700),
#     City(name="Karaj", country=country_iran, population=1592491),
#     City(name="Shiraz", country=country_iran, population=1563586),
#     City(name="Tabriz", country=country_iran, population=1558693),
#     City(name="Qom", country=country_iran, population=1111121),
#     City(name="Ahvaz", country=country_iran, population=1137542),
#     City(name="Kermanshah", country=country_iran, population=946651),
#     City(name="Urmia", country=country_iran, population=700465),
#     # Add more City instances for Iran as needed
# ]

# # Use the bulk_create method to insert all the cities for Iran into the database efficiently
# City.objects.bulk_create(iran_city_data)


# for Singapore
# # Find a country for which you want to insert cities (you can create a new one if needed)
# country_singapore = Country.objects.get(name="Singapore")  # Replace with the desired country name

# # Create a list of City instances for Singapore with the desired data
# singapore_city_data = [
#     City(name="Singapore", country=country_singapore, population=5698000),
#     # Add more City instances for Singapore as needed
# ]

# # Use the bulk_create method to insert all the cities for Singapore into the database efficiently
# City.objects.bulk_create(singapore_city_data)



# for China
# Find a country for which you want to insert cities (you can create a new one if needed)
# country_china = Country.objects.get(name="China")  # Replace with the desired country name

# # Create a list of City instances for China with the desired data
# china_city_data = [
#     City(name="Beijing", country=country_china, population=21516000),
#     City(name="Shanghai", country=country_china, population=24256800),
#     City(name="Guangzhou", country=country_china, population=14043500),
#     City(name="Shenzhen", country=country_china, population=12528300),
#     City(name="Chengdu", country=country_china, population=16350000),
#     City(name="Hangzhou", country=country_china, population=9875057),
#     City(name="Xi'an", country=country_china, population=12350000),
#     City(name="Chongqing", country=country_china, population=30900000),
#     City(name="Wuhan", country=country_china, population=11119000),
#     City(name="Nanjing", country=country_china, population=8472080),
#     # Add more City instances for China as needed
# ]

# # Use the bulk_create method to insert all the cities for China into the database efficiently
# City.objects.bulk_create(china_city_data)


# for Chile

# Find a country for which you want to insert cities (you can create a new one if needed)
# country_china = Country.objects.get(name="China")  # Replace with the desired country name

# # Create a list of City instances for China with the desired data
# china_city_data = [
#     City(name="Beijing", country=country_china, population=21516000),
#     City(name="Shanghai", country=country_china, population=24256800),
#     City(name="Guangzhou", country=country_china, population=14043500),
#     City(name="Shenzhen", country=country_china, population=12528300),
#     City(name="Chengdu", country=country_china, population=16350000),
#     City(name="Hangzhou", country=country_china, population=9875057),
#     City(name="Xi'an", country=country_china, population=12350000),
#     City(name="Chongqing", country=country_china, population=30900000),
#     City(name="Wuhan", country=country_china, population=11119000),
#     City(name="Nanjing", country=country_china, population=8472080),
#     # Add more City instances for China as needed
# ]

# # Use the bulk_create method to insert all the cities for China into the database efficiently
# City.objects.bulk_create(china_city_data)


# for Thailand
# Find a country for which you want to insert cities (you can create a new one if needed)
# country_thailand = Country.objects.get(name="Thailand")  # Replace with the desired country name

# # Create a list of City instances for Thailand with the desired data
# thailand_city_data = [
#     City(name="Bangkok", country=country_thailand, population=8248444),
#     City(name="Nonthaburi", country=country_thailand, population=270609),
#     City(name="Chiang Mai", country=country_thailand, population=131091),
#     City(name="Udon Thani", country=country_thailand, population=148217),
#     City(name="Nakhon Ratchasima", country=country_thailand, population=174999),
#     City(name="Hat Yai", country=country_thailand, population=159151),
#     City(name="Pattaya", country=country_thailand, population=107406),
#     City(name="Phuket", country=country_thailand, population=94238),
#     City(name="Krabi", country=country_thailand, population=53715),
#     City(name="Ayutthaya", country=country_thailand, population=56834),
#     # Add more City instances for Thailand as needed
# ]

# # Use the bulk_create method to insert all the cities for Thailand into the database efficiently
# City.objects.bulk_create(thailand_city_data)



# FOR Germany
# Find a country for which you want to insert cities (you can create a new one if needed)
# country_germany = Country.objects.get(name="Germany")  # Replace with the desired country name

# # Create a list of City instances for Germany with the desired data
# germany_city_data = [
#     City(name="Berlin", country=country_germany, population=3748148),
#     City(name="Hamburg", country=country_germany, population=1841179),
#     City(name="Munich", country=country_germany, population=1484226),
#     City(name="Cologne", country=country_germany, population=1080394),
#     City(name="Frankfurt", country=country_germany, population=753056),
#     City(name="Stuttgart", country=country_germany, population=628032),
#     City(name="Dusseldorf", country=country_germany, population=620961),
#     City(name="Dortmund", country=country_germany, population=586181),
#     City(name="Essen", country=country_germany, population=583109),
#     City(name="Leipzig", country=country_germany, population=593145),
#     # Add more City instances for Germany as needed
# ]

# # Use the bulk_create method to insert all the cities for Germany into the database efficiently
# City.objects.bulk_create(germany_city_data)


# for Spain
# Find a country for which you want to insert cities (you can create a new one if needed)
# country_spain = Country.objects.get(name="Spain")  # Replace with the desired country name

# # Create a list of City instances for Spain with the desired data
# spain_city_data = [
#     City(name="Madrid", country=country_spain, population=3266126),
#     City(name="Barcelona", country=country_spain, population=1621537),
#     City(name="Valencia", country=country_spain, population=814208),
#     City(name="Seville", country=country_spain, population=688711),
#     City(name="Zaragoza", country=country_spain, population=666058),
#     City(name="Malaga", country=country_spain, population=574654),
#     City(name="Murcia", country=country_spain, population=461246),
#     City(name="Palma", country=country_spain, population=422049),
#     City(name="Las Palmas de Gran Canaria", country=country_spain, population=381847),
#     City(name="Bilbao", country=country_spain, population=345821),
#     # Add more City instances for Spain as needed
# ]

# # Use the bulk_create method to insert all the cities for Spain into the database efficiently
# City.objects.bulk_create(spain_city_data)


# for Philippines
# # Find a country for which you want to insert cities (you can create a new one if needed)
# country_philippines = Country.objects.get(name="Philippines")  # Replace with the desired country name

# # Create a list of City instances for the Philippines with the desired data
# philippines_city_data = [
#     City(name="Manila", country=country_philippines, population=1780148),
#     City(name="Quezon City", country=country_philippines, population=2761720),
#     City(name="Davao City", country=country_philippines, population=1691464),
#     City(name="Cebu City", country=country_philippines, population=922611),
#     City(name="Zamboanga City", country=country_philippines, population=861799),
#     City(name="Taguig City", country=country_philippines, population=804915),
#     City(name="Antipolo", country=country_philippines, population=776386),
#     City(name="Pasig City", country=country_philippines, population=755300),
#     City(name="Cagayan de Oro", country=country_philippines, population=675950),
#     City(name="Parañaque", country=country_philippines, population=665822),
#     # Add more City instances for the Philippines as needed
# ]

# # Use the bulk_create method to insert all the cities for the Philippines into the database efficiently
# City.objects.bulk_create(philippines_city_data)
