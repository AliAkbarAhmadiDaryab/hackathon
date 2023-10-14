import sqlite3


class MyDB:
    def __init__(self) -> None:
        # create self.connection by using object
        # to connect with hotel_data database
        self.connection = sqlite3.connect('afgid_hf.db')
        
        # query to create a table named FOOD1
        self.connection.execute(''' CREATE TABLE afgid
                (FIND INT PRIMARY KEY     NOT NULL,
                regions           TEXT    NOT NULL,
                province            TEXT     NOT NULL,
                total        INT,
                full INT,
                PARTIAL INT, 
                NONFUNCTIONAL INT);
                ''')
    def insert(self):
        # insert query to insert food  details in 
        # the above table
        self.connection.execute("INSERT INTO afgid VALUES (1, 'South', 'Kandahar', 64, 54, 10, 0)") 
        self.connection.execute("INSERT INTO afgid VALUES (2,	'South',	'Hemlmand',	78,	0,	77,	1)") 
        self.connection.execute("INSERT INTO afgid VALUES (3,	'South',	'Zabul',	47,	0,	47,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (4,	'South',	'Urozgan',	56,	0,	56,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (5,	'South',	'Nimroz',	18,	0,	18,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (6,	'East',	'Nangarhar',	132, 11,	120, 1)") 
        self.connection.execute("INSERT INTO afgid VALUES (7,	'East', 	'Laghman',	59,	7,	52,	0)") 

        self.connection.execute("INSERT INTO afgid VALUES (9,	'East',	'Nuristan',	37,	0,	20,	17	)") 
        self.connection.execute("INSERT INTO afgid VALUES (10,	'Central', 	'Kabul',	47,	0,	47,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (11,	'Central', 	'Kapisa',	50,	0,	50,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (12,	'Central' ,	'Parwan',	84,	0,	84,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (13, 'Central' ,	'Panjsher', 30,	0,	0,	30)") 
        self.connection.execute("INSERT INTO afgid VALUES (14,	'Central', 	'Logar', 	56,	53,	3,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (15,	'Central' ,	'Wardak',	77,	12,	65,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (16,	'Central' ,	'Bamian',	75,	75,	0,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (17,	'Central' ,	'Daikunid', 58,	52,	6,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (18,	'Southeast',	'Khost', 42, 0,	42,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (19,	'Southeast'	,'Paktika',	54,	0,	54,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (20,	'Southeast'	,'Paktya',	46,	0,	46,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (21,	'Southeast',	'Ghazni', 109, 0, 109,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (22,	'Northeast'	,'Badakhshan', 115, 115, 0,	0	)") 
        self.connection.execute("INSERT INTO afgid VALUES (23,	'Northeast',	'Takhar',	84,	0,	84,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (24,	'Northeast',	'Kunuz',	75,	0,	74,	1	)") 
        self.connection.execute("INSERT INTO afgid VALUES (25,	'Northeast',	'Baghlan',	80,	0,	80,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (26,	'Western',	'Herat', 113, 0, 113, 0	)") 
        self.connection.execute("INSERT INTO afgid VALUES (27,	'Western',	'Badghis',	50,	0,	50,	0	)") 
        self.connection.execute("INSERT INTO afgid VALUES (28,	'Western',	'Ghor',	91,	0,	91,	0		)") 
        self.connection.execute("INSERT INTO afgid VALUES (29,	'Western',	'Farah', 72, 0,	72,	0		)") 
        self.connection.execute("INSERT INTO afgid VALUES (30,	'Northern',	'Balkh', 116, 0, 112, 0	)") 
        self.connection.execute("INSERT INTO afgid VALUES (31,	'Northern',	'Samangan',	47,	1,	0,	46			)") 
        self.connection.execute("INSERT INTO afgid VALUES (32,	'Northern',	'Jozjan',	49,	0,	49,	0)") 
        self.connection.execute("INSERT INTO afgid VALUES (33,	'Northern',	'Faryab',	68,	0,	68,	0	)") 
        self.connection.execute("INSERT INTO afgid VALUES (34,	'Northern',	'Saripul',	71,	0,	71,	0	)")     

    def select_table(self, query):
        # create a cousor object for select query
        try:
            cursor = self.connection.execute(query)
            # display all data from hotel table
            for row in cursor:
                print(row)
        except:
            print("Check your query")        
            
            